from flask import Flask, request
from prometheus_client import make_wsgi_app, Counter, Histogram
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from src.models.contact import User
from src.routes.routes import user_bp
from src.models.register import Register
import time

# Métricas personalizadas
REQUEST_COUNT = Counter(
    'app_requests_total', 
    'Total de solicitudes por endpoint', 
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'app_request_latency_seconds', 
    'Latencia de las solicitudes por endpoint',
    ['method', 'endpoint']
)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Crear tablas a través de los modelos
    User.create_table()
    Register.create_table()

    # Registrar rutas
    app.register_blueprint(user_bp)

    # Middleware de Prometheus
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    # Middleware para rastrear métricas
    @app.before_request
    def before_request():
        request.start_time = time.time()

    @app.after_request
    def after_request(response):
        latency = time.time() - request.start_time
        REQUEST_COUNT.labels(
            method=request.method, 
            endpoint=request.path, 
            http_status=response.status_code
        ).inc()
        REQUEST_LATENCY.labels(
            method=request.method, 
            endpoint=request.path
        ).observe(latency)
        return response

    return app
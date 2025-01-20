# Proyecto Salud y Bienestar

## Descripción

**Salud y Bienestar** es una plataforma integral diseñada para promover el bienestar y la salud de los usuarios. A través de esta herramienta, los usuarios pueden gestionar su información de salud y bienestar de manera eficiente, segura y accesible. Utilizando tecnologías avanzadas y un enfoque modular, se facilita la integración con otros sistemas y aplicaciones de salud, mejorando la experiencia del usuario y brindando un entorno completo para el seguimiento de métricas de salud.

El proyecto está orientado tanto a usuarios individuales como a instituciones de salud, permitiendo el seguimiento de indicadores de bienestar y salud, así como la integración con sistemas de monitoreo en tiempo real.

## Características principales

- **Gestión de datos personales de salud**: Los usuarios pueden registrar, actualizar y consultar su información de salud de forma segura y privada, asegurando el control total sobre sus datos.
- **Monitoreo de indicadores de bienestar**: Permite el seguimiento de parámetros clave como actividad física, nutrición, calidad del sueño y salud mental, ayudando a los usuarios a llevar un estilo de vida saludable.
- **Recomendaciones personalizadas**: Basadas en los datos proporcionados, la plataforma genera recomendaciones personalizadas para mejorar la salud y el bienestar, además de permitir el seguimiento de metas.
- **Interfaz de usuario intuitiva**: Un diseño limpio y accesible, adaptado a usuarios de todas las edades, para garantizar una experiencia fluida y amigable.
- **Integración con sistemas de monitoreo**: Utilizando herramientas como Prometheus, se realiza un monitoreo detallado del estado del sistema y la recolección de métricas en tiempo real, asegurando una gestión proactiva de posibles problemas.

## Tecnologías utilizadas

- **Frontend**: Desarrollado con tecnologías web modernas como HTML, CSS y JavaScript, junto con frameworks como React o Vue.js para crear una experiencia interactiva y atractiva.
- **Backend**: Implementado en Python para manejar la lógica del servidor, con un enfoque en el procesamiento eficiente de datos y la gestión de usuarios.
- **Base de datos**: Se utiliza MariaDB como base de datos SQL para almacenar de manera segura los datos de los usuarios y sus métricas de salud.
- **Docker**: La aplicación está contenerizada usando Docker, lo que permite una implementación más ágil y escalable, con facilidad para crear, ejecutar y distribuir los servicios.
- **Prometheus**: Utilizado para el monitoreo y la recolección de métricas en tiempo real, permitiendo realizar un análisis detallado del rendimiento y detectar posibles cuellos de botella o fallos.
- **Grafana**: Herramienta de visualización de métricas que permite una representación gráfica clara y comprensible de las estadísticas del sistema.
- **Nginx**: Utilizado como servidor web para gestionar las solicitudes entrantes y servir la aplicación de forma eficiente.

## Puertos utilizados

A continuación, se detallan los puertos utilizados por cada uno de los servicios en el proyecto:

- **API (backend)**: No expone puertos directamente al exterior (utiliza contenedores internos).
- **Nginx**: Puerto **80** (HTTP).
- **Nginx Exporter**: Puerto **9113** (para métricas de Nginx).
- **Base de datos (MariaDB)**: Puerto **3306** (para conexiones MySQL).
- **MariaDB Exporter**: Puerto **9104** (para métricas de MariaDB).
- **Prometheus**: Puerto **9090** (interfaz de Prometheus).
- **Grafana**: Puerto **3000** (interfaz de Grafana).
- **Elasticsearch**: Puertos **9200** (HTTP) y **9300** (interno para nodos).
- **Logstash**: Puertos **5044** (entrada de logs) y **9600** (interfaz de configuración).
- **Kibana**: Puerto **5601** (interfaz de Kibana).

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

- **`backend/`**: Contiene el código relacionado con el servidor, la lógica de negocio y la gestión de APIs y base de datos.
- **`frontend/`**: Archivos para la creación de la interfaz de usuario (HTML, CSS, JavaScript), así como los recursos gráficos y de visualización.
- **`iac/`**: Infraestructura como código para implementar la solución en la nube, automatizando el despliegue y la configuración de los servicios.
- **`docker-compose.yaml`**: Configuración para levantar todos los servicios necesarios mediante contenedores Docker.
- **`nginx.conf`**: Archivo de configuración del servidor Nginx para gestionar las solicitudes y servir la aplicación.

## Instalación

Para comenzar con el proyecto, sigue estos pasos:

1. Clona este repositorio en tu máquina local:
    ```bash
    git clone https://github.com/HectorCRZBQ/salud_y_bienestar.git
    ```

2. Navega al directorio del proyecto:
    ```bash
    cd salud_y_bienestar
    ```

3. Instala Docker en tu sistema si aún no lo tienes. Consulta la [guía oficial de Docker](https://docs.docker.com/get-docker/) para instalar Docker y Docker Compose en tu máquina.

4. Levanta los contenedores utilizando Docker Compose:
    ```bash
    docker-compose up --build
    ```

5. Accede a la aplicación desde tu navegador utilizando la siguiente URL:
    ```
    http://localhost:8080
    ```

6. ¡Listo! Ahora podrás interactuar con la plataforma y comenzar a explorar sus características.

## Contribuciones

Si deseas contribuir al proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección.
3. Realiza los cambios y asegúrate de que el código esté debidamente documentado.
4. Ejecuta las pruebas unitarias o de integración para garantizar que todo funcione correctamente.
5. Realiza un pull request detallando los cambios realizados.

## Colaboradores

Este proyecto ha sido desarrollado con la valiosa colaboración de los siguientes miembros del equipo:

- **[josesuarez03](https://github.com/josesuarez03)**: Responsable del despliegue en la nube, la implementación de infraestructura como código (IaC) y la configuración de los servicios en el stack ELK (Elasticsearch, Logstash, Kibana). Se encargó de asegurar la correcta integración y monitoreo del sistema en entornos de producción.
  
- **[Alvaro5473](https://github.com/Alvaro5473)**: Encargado del desarrollo del frontend y el diseño de la interfaz de usuario. Se centró en crear una experiencia de usuario visualmente atractiva y fácil de usar.

- **[HectorCRZBQ](https://github.com/HectorCRZBQ)**: Responsable del desarrollo del backend, la configuración del archivo `docker-compose` y la implementación de herramientas de monitoreo como **Prometheus** y **Grafana**. Se encargó de optimizar el rendimiento del sistema y asegurar su estabilidad mediante el monitoreo continuo.

Gracias a su esfuerzo y colaboración, este proyecto ha alcanzado un alto nivel de calidad y funcionalidad.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

Este README proporciona una guía detallada para la instalación, ejecución y contribución al proyecto **Salud y Bienestar**. ¡Esperamos que disfrutes de la plataforma y encuentres valor en ella!

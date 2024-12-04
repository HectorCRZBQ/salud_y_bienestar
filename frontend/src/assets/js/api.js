document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const apiUrl = "http://127.0.0.1:5000/api/users/";

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Evita el envío predeterminado del formulario
            
        // Capturar los datos del formulario
        const name = document.getElementById("demo-name").value.trim();
        const email = document.getElementById("demo-email").value.trim();
        const category = document.getElementById("demo-category").value;
        const priority = document.querySelector("input[name='demo-priority']:checked")?.id === "demo-priority-low" ? "Low" : "High";
        const message = document.getElementById("demo-message").value.trim();

        // Validaciones básicas
        if (!name || !email || !category || !message) {
            alert("Por favor, completa todos los campos obligatorios.");
            return;
        }

        // Preparar datos para la solicitud
        const formData = {
            nombre: name,
            email: email,
            categoria: category,
            prioridad: priority,
            mensaje: message
        };

        try {
            // Enviar solicitud a la API
            const response = await fetch(apiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok) {
                alert("Formulario enviado con éxito: " + result.message);
                form.reset(); // Limpiar el formulario
            } else {
                alert("Error al enviar el formulario: " + (result.error || "Error desconocido."));
            }
        } catch (error) {
            alert("Hubo un problema al conectarse con la API: " + error.message);
        }
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Zona Clientes Form
    const zonaClientesForm = document.querySelector("#zona-clientes form");
    const zonaClientesApiUrl = "/api/users/register";

    if (zonaClientesForm) {
        zonaClientesForm.addEventListener("submit", async (event) => {
            event.preventDefault();
            const email = zonaClientesForm.querySelector("#email").value.trim();
            const password = zonaClientesForm.querySelector("#password").value.trim();

            console.log("Email:", email, " password:", password);

            const validationErrors = validateZonaClientesForm(email, password);
            if (validationErrors.length > 0) {
                displayErrors(zonaClientesForm, validationErrors);
                return;
            }

            const formData = { email: email, password: password };
            await sendPostRequest(zonaClientesApiUrl, formData, zonaClientesForm, "Usuario registrado con éxito");
        });
    }

    // Atención al Cliente Form
    const atencionClienteForm = document.querySelector("#atencion-al-cliente form");
    const atencionClienteApiUrl = "/api/users/contact";

    if (atencionClienteForm) {
        atencionClienteForm.addEventListener("submit", async (event) => {
            event.preventDefault();
            const name = atencionClienteForm.querySelector("#name").value.trim();
            const email = atencionClienteForm.querySelector("#email").value.trim();
            const message = atencionClienteForm.querySelector("#message").value.trim();

            const validationErrors = validateAtencionClienteForm(name, email, message);
            if (validationErrors.length > 0) {
                displayErrors(atencionClienteForm, validationErrors);
                return;
            }

            const formData = { name: name, email: email, message: message };
            await sendPostRequest(atencionClienteApiUrl, formData, atencionClienteForm, "Mensaje enviado con éxito");
        });
    }

    function validateZonaClientesForm(email, password) {
        const errors = [];
        if (!email || !emailRegex.test(email)) {
            errors.push("Por favor, ingrese un correo electrónico válido.");
        }
        if (!password || password.length < 6) {
            errors.push("La contraseña debe tener al menos 6 caracteres.");
        }
        return errors;
    }

    function validateAtencionClienteForm(name, email, message) {
        const errors = [];
        if (!name || name.length < 2) {
            errors.push("El nombre debe tener al menos 2 caracteres.");
        }
        if (!email || !emailRegex.test(email)) {
            errors.push("Por favor, ingrese un correo electrónico válido.");
        }
        if (!message || message.length < 10) {
            errors.push("El mensaje debe tener al menos 10 caracteres.");
        }
        return errors;
    }

    function displayErrors(form, errors) {
        const existingErrors = form.querySelectorAll('.form-error');
        existingErrors.forEach(el => el.remove());

        const errorContainer = document.createElement('div');
        errorContainer.className = 'form-error text-danger';

        const errorList = document.createElement('ul');
        errors.forEach(error => {
            const li = document.createElement('li');
            li.textContent = error;
            errorList.appendChild(li);
        });

        errorContainer.appendChild(errorList);

        const submitButton = form.querySelector('input[type="submit"]');
        submitButton.parentNode.insertBefore(errorContainer, submitButton);
    }

    async function sendPostRequest(apiUrl, formData, form, successMessage) {
        try {
            const response = await fetch(apiUrl, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData),
            });

            const result = await response.json();

            if (response.ok) {
                alert(successMessage);
                form.reset();
                const errorContainer = form.querySelector('.form-error');
                if (errorContainer) errorContainer.remove();
            } else {
                throw new Error(result.error || "Error en el envío.");
            }
        } catch (error) {
            displayErrors(form, [error.message]);
        }
    }
});

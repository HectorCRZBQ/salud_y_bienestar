document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#atencion-al-cliente form");
    const apiUrl = "/api/users/contact";  

    // Email validation regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Function to validate form inputs
    function validateForm(name, email, message) {
        const errors = [];

        // Name validation
        if (!name || name.trim().length < 2) {
            errors.push("El nombre debe tener al menos 2 caracteres.");
        }

        // Email validation
        if (!email || !emailRegex.test(email.trim())) {
            errors.push("Por favor, ingrese un correo electrónico válido.");
        }

        // Message validation
        if (!message || message.trim().length < 10) {
            errors.push("El mensaje debe tener al menos 10 caracteres.");
        }

        return errors;
    }

    // Function to display errors
    function displayErrors(errors) {
        // Remove any existing error messages
        const existingErrors = document.querySelectorAll('.form-error');
        existingErrors.forEach(el => el.remove());

        // Create error container
        const errorContainer = document.createElement('div');
        errorContainer.className = 'form-error text-danger';
        
        // Create error list
        const errorList = document.createElement('ul');
        errors.forEach(error => {
            const li = document.createElement('li');
            li.textContent = error;
            errorList.appendChild(li);
        });

        errorContainer.appendChild(errorList);

        // Insert error container before the submit button
        const submitButton = form.querySelector('input[type="submit"]');
        submitButton.parentNode.insertBefore(errorContainer, submitButton);
    }

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // Prevent default form submission

        // Capture form data
        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const message = document.getElementById("message").value.trim();

        // Validate form inputs
        const validationErrors = validateForm(name, email, message);

        // If there are validation errors, display them and stop
        if (validationErrors.length > 0) {
            displayErrors(validationErrors);
            return;
        }

        // Prepare data for API request
        const formData = {
            name: name,
            email: email,
            message: message
        };

        try {
            // Send request to API
            const response = await fetch(apiUrl, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok) {
                // Success handling
                alert("Mensaje enviado con éxito");
                form.reset(); // Clear the form
                
                // Remove any previous error messages
                const errorContainer = form.querySelector('.form-error');
                if (errorContainer) {
                    errorContainer.remove();
                }
            } else {
                // Error handling
                throw new Error(result.error || "Error al enviar el mensaje");
            }
        } catch (error) {
            // Network or server error handling
            displayErrors([error.message]);
        }
    });
});
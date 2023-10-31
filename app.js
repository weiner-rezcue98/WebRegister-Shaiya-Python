document.addEventListener('DOMContentLoaded', function () {
    const registrationForm = document.getElementById('registration-form');
    const message = document.getElementById('message');

    registrationForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(registrationForm);
        const userData = {};
        formData.forEach((value, key) => {
            userData[key] = value;
        });

        // Envia os dados do formulário para o servidor
        fetch('/register', {
            method: 'POST',
            body: JSON.stringify(userData),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            message.innerText = data.message;
        })
        .catch(error => {
            message.innerText = 'Erro ao processar o registro.';
        });
    });
});

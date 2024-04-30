function submitForm(event) {
    event.preventDefault(); // Предотвратить переход на другую страницу

    var form = document.getElementById("myForm");
    var formData = new FormData(form);

    fetch('/profile', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        console.log(data); // Показать результат от сервера
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}
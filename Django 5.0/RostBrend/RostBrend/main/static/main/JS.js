document.querySelectorAll('input[type="checkbox"][name="fact"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        document.querySelectorAll('input[type="checkbox"][name="fact"]').forEach(otherCheckbox => {
            if (otherCheckbox !== this) {
                otherCheckbox.checked = false;
            }
        });
    });
});

document.getElementById('check-facts').addEventListener('click', function() {
    const selectedFact = document.querySelector('input[type="checkbox"][name="fact"]:checked');

    if (selectedFact && selectedFact.value === '2') {
        document.getElementById('feedback').innerText = 'Угадал!';
        // Добавьте код для подсветки чекбокса зеленым
    } else {
        document.getElementById('feedback').innerText = 'Не угадал!';
        // Добавьте код для подсветки чекбокса красным
    }
});

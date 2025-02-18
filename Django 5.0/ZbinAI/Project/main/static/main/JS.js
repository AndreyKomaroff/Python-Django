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

    if (selectedFact && selectedFact.value === '4') {
        document.getElementById('feedback').innerHTML = '<img src="data:image/svg+xml,%3Csvg%20width=\'24\'%20height=\'24\'%20viewBox=\'0%200%2024%2024\'%20fill=\'none\'%20xmlns=\'http://www.w3.org/2000/svg\'%3E%3Cpath%20d=\'M18%206L7%2017L2%2012\'%20stroke=\'url(%23paint0_linear_2055_38)\'%20stroke-width=\'2\'%20stroke-linecap=\'round\'%20stroke-linejoin=\'round\'/%3E%3Cpath%20d=\'M22%2010L14.5%2017.5L13%2016\'%20stroke=\'url(%23paint1_linear_2055_38)\'%20stroke-width=\'2\'%20stroke-linecap=\'round\'%20stroke-linejoin=\'round\'/%3E%3Cdefs%3E%3ClinearGradient%20id=\'paint0_linear_2055_38\'%20x1=\'2.39053\'%20y1=\'-5.96491\'%20x2=\'18.1036\'%20y2=\'-5.84327%27%20gradientUnits=\'userSpaceOnUse\'%3E%3Cstop%20stop-color=\'%23F39200\'/%3E%3Cstop%20offset=\'1\'%20stop-color=\'%23E05F02\'/%3E%3C/linearGradient%3E%3ClinearGradient%20id=\'paint1_linear_2055_38\'%20x1=\'13.2197\'%20y1=\'1.8421\'%20x2=\'22.0584\'%20y2=\'1.89856\'%20gradientUnits=\'userSpaceOnUse\'%3E%3Cstop%20stop-color=\'%23F39200\'/%3E%3Cstop%20offset=\'1\'%20stop-color=\'%23E05F02\'/%3E%3C/linearGradient%3E%3C/defs%3E%3C/svg%3E" alt="Галочка"> Верно! Чтоб я потратила на рекламу столько денег, да ни за что! Я же гуру партизанского маркетинга.';
        // Добавьте код для подсветки чекбокса зеленым
    } else {
        document.getElementById('feedback').innerText = 'Это правда!';
        // Добавьте код для подсветки чекбокса красным
    }
});

const cards = document.querySelectorAll('.about-bottom__cards-inner');

cards.forEach(card => {
    card.addEventListener('click', function() {
        this.classList.toggle('active');
    });
});  // Этот JavaScript код добавляет обработчик события click к каждому элементу с классом about-bottom__cards-inner. Когда происходит клик на элементе, выполняется функция, которая переключает класс active для этого элемента. Таким образом, при каждом клике на элементе, его классы будут переключаться между about-bottom__cards-inner и about-bottom__cards-inner active, что приведет к применению CSS стиля и созданию эффекта поворота.


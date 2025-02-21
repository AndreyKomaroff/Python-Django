const cards = document.querySelectorAll('.about-bottom__cards-inner');

cards.forEach(card => {
    card.addEventListener('click', function() {
        this.classList.toggle('active');
    });
});  // Этот JavaScript код добавляет обработчик события click к каждому элементу с классом about-bottom__cards-inner. Когда происходит клик на элементе, выполняется функция, которая переключает класс active для этого элемента. Таким образом, при каждом клике на элементе, его классы будут переключаться между about-bottom__cards-inner и about-bottom__cards-inner active, что приведет к применению CSS стиля и созданию эффекта поворота.


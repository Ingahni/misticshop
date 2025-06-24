const btn = document.getElementById('expandBtn');

  btn.addEventListener('click', (e) => {
    e.preventDefault(); // зупиняємо стандартну поведінку на випадок форми
    btn.classList.add('expanded');
    btn.innerText = 'ALL PRODUCTS';

    // Затримка перед переходом — щоб показати анімацію
    setTimeout(() => {
      window.location.href = '/catalog.html'; // змініть на ваш шлях
    }, 500); // 0.5 секунди
  });
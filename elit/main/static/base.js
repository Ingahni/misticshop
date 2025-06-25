const link = document.getElementById('expandLink');

link.addEventListener('click', function (e) {
  e.preventDefault(); // зупиняємо миттєвий перехід
  link.classList.add('expanded');
  link.innerText = 'ALL PRODUCTS';

  setTimeout(() => {
    window.location.href = link.getAttribute('href');
  }, 500); // 0.5 секунди для анімації
});

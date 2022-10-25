//Initial slick slider
$(document).ready(function () {
  $('.slick-4').slick({
    infinite: false,
    slidesToShow: 4,
    slidesToScroll: 4,
    adaptiveHeight: true,
    speed: 1000,
  });
});

// Search dropdown
const searchDropdown = document.querySelector('#banner__search-form-dropdown');
const inputField = document.querySelector('#banner__search-form-input input');

inputField.addEventListener('focus', function () {
  searchDropdown.classList.add('show-search-dropdown');
});

window.addEventListener('click', function (event) {
  if (
    !event.target.matches('#banner__search-form-dropdown') &&
    !event.target.matches('#banner__search-form-input input') &&
    searchDropdown.classList.contains('show-search-dropdown')
  )
    searchDropdown.classList.remove('show-search-dropdown');
});

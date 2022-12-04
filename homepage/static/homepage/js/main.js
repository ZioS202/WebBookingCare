'use strict';

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

$('.lazy').slick({
  lazyLoad: 'ondemand',
});

// Search dropdown
const searchDropdown = document.querySelector('#banner__search-form-dropdown');
const inputField = document.querySelector('#id_query');

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

// inputField.addEventListener('blur', function () {
//   searchDropdown.classList.remove('show-search-dropdown');
// });

/* * Homepage search feature
 */

const csrfmiddlewaretoken = document.querySelector(
  '#search_form input:first-child'
).value;
const searchForm = document.querySelector('#search_form');
const submitBtn = document.getElementById('submit-btn');

function refresh_dropdown() {
  if (searchDropdown.innerHTML) searchDropdown.innerHTML = '';
}

function add_to_dropdown(h3, url, data) {
  searchDropdown.insertAdjacentHTML('beforeend', `<h3>${h3}</h3>`);
  Object.entries(data).forEach(entry => {
    const [key, value] = entry;
    const html = `
      <a href="${url + key}">
        <i style="background: transparent
        url(${value.avatar}) center center no-repeat;"></i>
        <h4>${value.name}</h4>
      </a>`;
    searchDropdown.insertAdjacentHTML('beforeend', html);
  });
}

searchForm.onsubmit = async function (e) {
  e.preventDefault();
  refresh_dropdown();

  if (!searchDropdown.classList.contains('show-search-dropdown'))
    searchDropdown.classList.add('show-search-dropdown');

  let query = inputField.value;
  const specialists = await search_specialist(csrfmiddlewaretoken, query);
  const clinics = await search_clinic(csrfmiddlewaretoken, query);
  const doctors = await search_doctor(csrfmiddlewaretoken, query);

  add_to_dropdown('Chuyên khoa', '/specialist/specialistDetail/', specialists);
  add_to_dropdown('Cơ sở y tế', '/clinic/clinicDetail/', clinics);
  add_to_dropdown('Bác sĩ', '/doctor/doctorDetail/', doctors);
};

// Search onclick icon search
document.querySelector('#search_submit').addEventListener('click', () => {
  submitBtn.click();
});

//Refresh dropdown when empty input
inputField.addEventListener('input', e => {
  if (!e.target.value) searchDropdown.innerHTML = '';
});

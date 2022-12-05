'use strict';

const searchForm = document.querySelector('#search_form');
const inputField = document.querySelector('#id_query');
const submitBtn = document.getElementById('submit-btn');
const csrfmiddlewaretoken = document.querySelector(
  '#search_form input:first-child'
).value;
const divContent = document.querySelector('.content');

const defaultValue_divContent = divContent.innerHTML;

function show_result(data) {
  Object.entries(data).forEach(entry => {
    const [key, value] = entry;
    const html = `
      <table>
        <tr>
          <td>
            <a href="/clinic/clinicDetail/${key}">
              <img src="${value.avatar}" alt="${value.name}" loading="lazy">
            </a>
          </td>
          <td style="text-align:left;width: 90%;">
            <a href="/clinic/clinicDetail/${key}">
              <h3>${value.name}</h3>
            </a>
          </td>
        </tr>
      </table>
      <hr>`;
    divContent.insertAdjacentHTML('beforeend', html);
  });
}

searchForm.onsubmit = async function (e) {
  e.preventDefault();

  let query = inputField.value;
  const specialists = await search_clinic(csrfmiddlewaretoken, query);

  //Refresh list specialist
  divContent.innerHTML = `<h3 style="font-weight:bold">Thông tin các bệnh viện, phòng khám nổi bật:</h3>`;

  show_result(specialists);
};

//Return default value of list specialist when empty input
inputField.addEventListener('input', e => {
  if (!e.target.value) divContent.innerHTML = defaultValue_divContent;
});
'use strict';

dayjs.locale('vi');

const select = document.querySelector('#selectDate');
const searchScheduleForm = document.querySelector('#search_schedule');
const csrfmiddlewaretoken = document.querySelector(
  '#search_schedule input:first-child'
).value;
const submitBtn = document.getElementById('submit-btn');
const choiceTime = document.querySelector('.choiceTime');

function get_day_of_week(day) {
  switch (day) {
    case 1:
      return 'Thứ hai';
      break;
    case 2:
      return 'Thứ ba';
      break;
    case 3:
      return 'Thứ tư';
      break;
    case 4:
      return 'Thứ năm';
      break;
    case 5:
      return 'Thứ sáu';
      break;
    case 6:
      return 'Thứ bảy';
      break;
    default:
      return 'Chủ nhật';
  }
}

//Add options for select tag
for (let i = 0; i < 6; i++) {
  const day = 4 + i;
  const month = 12;
  const year = 2022;
  const obj = dayjs(`${year}-${month}-${day}`);
  const html = `
  <option value="${obj.format('YYYY-MM-DD')}">
    ${get_day_of_week(obj.day())} - ${obj.format('DD/MM')}
  </option>`;
  select.insertAdjacentHTML('beforeend', html);
}

function showTimeslot() {
  submitBtn.click();
}

function show_schedule(url, data) {
  Object.entries(data).forEach(entry => {
    const [key, value] = entry;
    const html = `<a href="${url + key}">${value.time_slot}</a>`;
    choiceTime.insertAdjacentHTML('beforeend', html);
  });
}

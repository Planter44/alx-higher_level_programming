'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    const Staff = document.createElement('li');

    Staff.textContent = 'Item';
    $('UL.my_list').append(Staff);
  });
});

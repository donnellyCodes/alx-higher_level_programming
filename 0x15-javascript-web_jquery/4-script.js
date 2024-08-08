// toogles the class of header element when
// user clicks on DIV#toggle_header
// the class must update to green

$('DIV#toggle_header').click(function () {
  $('header').toogleclass('red green');
});

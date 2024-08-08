// printing hellow world depending on language

$('document').ready(function () {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (enter) {
      if (enter.keycode === 13) {
        translate();
      }
    });
  });
});
function transtlate () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function (data) {
    $('DIV#hello').html(data.hello);
  });
}

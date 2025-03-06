$(document).ready(function () {
  $('a, p, h1, h2, h3, h4, h5, h6, span, b, label, button, table,td').hover(function () {
    var url = window.location.pathname;
    lang = $('html').attr('lang');
    // console.log('current-lang', lang);
    if ($('.on').hasClass('active')) {
      if (lang == "uz" || lang == "oz" || lang == "ru") {
        responsiveVoice.speak($(this).text(), "Russian Female");
      } else {
        responsiveVoice.speak($(this).text(), "UK English Female");
      }
    }
  });

  $('#onOf').click(function (e) {
    e.preventDefault();
    $(this).toggleClass('active');
  });



  // var originalSize = $('div').css('font-size');
  // // reset        
  // $(".resetMe").click(function () {
  //   $('div').css('font-size', originalSize);
  // });

  // Increase Font Size          
  $("#f_inc").click(function () {
    var currentSize = $('a, p, h1, h2, h3, h4, h5, h6, span, b, label, button, table,td').css('font-size');
    var currentSize = parseFloat(currentSize) * 1.2;
    $('div').css('font-size', currentSize);
    return false;
  });

  // Decrease Font Size       
  $("#f_dec").click(function () {
    var currentFontSize = $('a, p, h1, h2, h3, h4, h5, h6, span, b, label, button, table,td').css('font-size');
    var currentSize = $('div').css('font-size');
    var currentSize = parseFloat(currentSize) * 0.8;
    $('div').css('font-size', currentSize);
    return false;
  });
});
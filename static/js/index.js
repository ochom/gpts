$(document).ready(function () {
  $('.nav-link').click(function () {
    var offset = -50; // <-- change the value here
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html, body').animate({
          scrollTop: target.offset().top + offset
        }, 1000);

        $('.nav-link').removeClass('active');
        $(this).addClass('active');

        return false;
      }
    }
  });

  sal();

})

$("#formContactUs").submit(function (e) {
  e.preventDefault();
  $.ajax({
    type: 'post',
    url: '/contactus/api',
    data: $('#formContactUs').serialize(),
    success: function (res) {
      if (res.includes("success")) {
        location.href = "/success";
      } else {
        location.href = "/error";
      }
    },
    error: function (err) {
      location.href = "/error";
      console.log(err);
    }
  });
})

$("#formSubscribe").submit(function (e) {
  e.preventDefault();
  $.ajax({
    type: 'post',
    url: '/subscribe/api',
    data: $('#formSubscribe').serialize(),
    success: function (res) {
      console.log(res);
      if (res.includes("success")) {
        location.href = "/success";
      } else {
        location.href = "/error";
      }
    },
    error: function (err) {
      location.href = "/error";
      console.log(err);
    }
  });
})
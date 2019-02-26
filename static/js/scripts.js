$(document).ready(function() {
    /*global $*/
    $('.collapsible').collapsible();
    $('select').material_select();
    $(".button-collapse").sideNav();
});

$('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
});

var btn = $('#the-top');

$(window).scroll(function() {
    if($(window).scrollTop() > 300){
        btn.addClass('show');
    } else{
        btn.removeClass('show');
    }
});

btn.on('click', function(e) {
    e.preventDefault();
    $('html, body').animate({scrollTop:0},
    '300');
});

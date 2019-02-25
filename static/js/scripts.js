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

//Scroll to top button
// var scrollTop = $("#scrollTop");

// $(scrollTop).click(function() {
//     $('html, body').animate({
//         scrollTop: 0
//     }, 800);
//     return false;

// });

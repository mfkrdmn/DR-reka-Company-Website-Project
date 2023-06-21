// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: false,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: false,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 4
        },
        600: {
            items: 4
        },
        1000: {
            items: 4
        }
    }
});




/**
    alert
*/

function myAlertTop(){
    $(".myAlert-top").show();
    setTimeout(function(){
      $(".myAlert-top").hide(); 
    }, 19000);
}
  
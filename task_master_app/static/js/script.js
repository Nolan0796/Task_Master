$('.header a').hover(function() {
    $(this).css('background-color', 'white').css('opacity', '60%').css('border-style', 'outset')
}, function() {
    $(this).css('background-color', 'transparent').css('opacity', '100%').css('border-style', 'none')
})

$('.button-link').hover(function() {
    $(this).css('background-color', 'transparent').css('color', 'rgba(18,90,133,1)')
}, function() {
    $(this).css('background-color', 'rgba(18,90,133,1)').css('color', 'whitesmoke')
})

var nav = document.querySelector('.header');

window.addEventListener('scroll', function() {
    if(window.pageYOffset > 130) {
        nav.classList += ' small';
    } else {
        nav.classList = 'header';
    }
})
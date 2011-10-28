$(function() {
    //random image for header background
    bgImageTotal = 7;
    randomNumber = Math.round(Math.random() * (bgImageTotal - 1)) + 1;
    imgPath = ('/static/img/banners/' + randomNumber + '.png');
    $('.banners').css('background-image', ('url("' + imgPath + '")'));
});

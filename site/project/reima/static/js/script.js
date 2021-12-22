var s = 0;
var showtime = 5000;

function slideshow(){
    slide = document.getElementsByClassName('imgslide');
    for (let i = 0; i < slide.length; i++) {
        slide[i].style.display = 'none';

    }
    s++;
    if(s> slide.length) { s = 1;}
    slide[s-1].style.display = "block";
    setTimeout("slideshow()", showtime);
}
window.onload = slideshow;
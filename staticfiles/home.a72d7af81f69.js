const slideImages = document.querySelectorAll('.img-container');
let currentIndex = 0;

function slideNext() {
    slideImages[currentIndex].style.opacity = '0';
    currentIndex++;
    if (currentIndex >= slideImages.length) {
        currentIndex = 0;
    }
    slideImages[currentIndex].style.opacity = '1';
}

function startSlideshow() {
    slideImages[currentIndex].style.opacity = '1';
    setInterval(slideNext, 5000);
}

startSlideshow();

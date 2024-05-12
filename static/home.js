const slideImages = document.querySelectorAll('.img-container');
let currentIndex = 0;

function slideNext() {
    // Hide the current image
    slideImages[currentIndex].style.opacity = '0';

    // Move to the next image
    currentIndex++;
    if (currentIndex >= slideImages.length) {
        currentIndex = 0; // Reset index to loop back to the first image
    }

    // Show the next image
    slideImages[currentIndex].style.opacity = '1';
}

function startSlideshow() {
    // Initially show the first image
    slideImages[currentIndex].style.opacity = '1';

    // Start sliding to the next image after 5 seconds
    setInterval(slideNext, 5000);
}

// Start the slideshow
startSlideshow();





const wrapper = document.querySelector('.wrapper')

let pressed = false
let startX = 0

wrapper.addEventListener('mousedown', function (e) {
  pressed = true
  startX = e.clientX
  this.style.cursor = 'grabbing'
})

wrapper.addEventListener('mouseleave', function (e) {
  pressed = false
})

window.addEventListener('mouseup', function (e) {
  pressed = false
  wrapper.style.cursor = 'grab'
})

wrapper.addEventListener('mousemove', function (e) {
  if(!pressed) {
    return
  }

  this.scrollLeft += startX - e.clientX
})
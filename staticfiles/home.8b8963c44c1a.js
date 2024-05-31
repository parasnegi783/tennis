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

const wrapper = document.querySelector('.wrapper');

let startX = 0;
let isTextHovered = false;

wrapper.addEventListener('mousedown', function (e) {
    if (!isTextHovered) {
        startX = e.clientX;
        wrapper.style.cursor = 'grabbing';
    }
});

wrapper.addEventListener('mouseleave', function () {
    wrapper.style.cursor = 'grab';
});

window.addEventListener('mouseup', function () {
    wrapper.style.cursor = 'grab';
});

wrapper.addEventListener('mousemove', function (e) {
    if (!isTextHovered) {
        const moveX = startX - e.clientX;
        wrapper.scrollLeft += moveX;
        startX = e.clientX;
    }
});

// Detect if the mouse is over text within the cards
wrapper.addEventListener('mouseover', function (e) {
    if (e.target.tagName === 'UL' || e.target.tagName === 'LI') {
        isTextHovered = true;
    } else {
        isTextHovered = false;
    }
});

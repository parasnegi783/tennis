document.addEventListener('DOMContentLoaded', function () {
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

    wrapper.addEventListener('mouseover', function (e) {
        if (e.target.tagName === 'UL' || e.target.tagName === 'LI') {
            isTextHovered = true;
        } else {
            isTextHovered = false;
        }
    });
});

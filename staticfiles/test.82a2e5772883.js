document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, {
        indicators: false,
        height: 400, // You can set a default height
        duration: 300,
        interval: 3000
    });

    // Check if images are loaded
    instances[0].$slides.each(function() {
        var img = $(this).find('img').first();
        if (!img.complete || img.naturalWidth === 0) {
            console.error('Image not loaded:', img.attr('src'));
        }
    });
});

// scripts.js

document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, {
        format: 'yyyy-mm-dd',
        showClearBtn: true,
        autoClose: true,
        maxDate: new Date(),
        yearRange: 100
    });
});

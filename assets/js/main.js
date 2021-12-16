$(document).ready(function() {
    if ($("#dev-warning").length == 1) {
        console.log('This is the local development version of the website.');
    }

    // Enable all poppers in the document
    setTimeout(function () {
        $('[data-toggle="popover"]').popover();
    }, 500);
});

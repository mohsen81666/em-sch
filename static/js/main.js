
$(document).ready(function () {

    const currentPath = window.location.pathname;

    $(".navbar-nav .nav-link").each(function () {
        const $link = $(this);

        if ($link.attr("href") === currentPath) {
            $link.addClass("active");
        } else {
            $link.removeClass("active");
        }
    });

});

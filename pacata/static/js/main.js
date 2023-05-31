$(document).ready(function() {

    $(".btn-group-toggle .btn").click(function() {
        $(".btn-group-toggle .btn").removeClass('active');
        $(this).addClass('active');
    });
});

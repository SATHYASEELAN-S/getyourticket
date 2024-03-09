


$(document).ready(function () {
    $('#loginbutton').on('click', function () {
        $('#offcanvasNavbar').offcanvas('hide');
        var registerModal = new bootstrap.Modal(document.getElementById('registermodal'));
        $("#register").addClass("d-none");
        $("#login").removeClass("d-none");
        $("#register-image").addClass("d-none");
        $("#login-image").removeClass("d-none");


        $(".btn-login").addClass("underline-text");
        $(".btn-register").removeClass("underline-text");
        registerModal.show();
    });
    $('#registerbutton').on('click', function () {
        $('#offcanvasNavbar').offcanvas('hide');
        var registerModal = new bootstrap.Modal(document.getElementById('registermodal'));
        $("#login").addClass("d-none");
        $("#register").removeClass("d-none");
        $("#register-image").removeClass("d-none");
        $("#login-image").addClass("d-none");


        
    $(".btn-register").addClass("underline-text");
    $(".btn-login").removeClass("underline-text");
        registerModal.show();
    });

    
});
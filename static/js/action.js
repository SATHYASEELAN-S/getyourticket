
$(document).ready(function () {

  $("#register").addClass("d-none");
  $("#login").removeClass("d-none");



  $("#register-image").addClass("d-none");
  $("#login-image").removeClass("d-none");



  $(".btn-login").addClass("underline-text");
  $(".btn-register").removeClass("underline-text");

    $(".form-btn").on("click", function () {
      var targetId = $(this).data("target");
        console.log(targetId);

        if (targetId==="login")
        {
          $("#register-image").addClass("d-none");
          $("#login-image").removeClass("d-none");
       
        }else if (targetId==="register")
        {
          $("#register-image").removeClass("d-none");
          $("#login-image").addClass("d-none");
         
        
        }

      $(".form").addClass("d-none");
      $("." + targetId).removeClass("d-none");
      
      $(".form-btn").removeClass("underline-text");
  
      $(this).addClass("underline-text");
    });
  });
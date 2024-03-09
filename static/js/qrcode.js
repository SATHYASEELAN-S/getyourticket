


$(document).ready(function()
{
    var scanner;
    $('.qrscanner').on("click",function(){
    $(".search-content").addClass("d-none");
  $(".qrcontent").removeClass("d-none");
  scanner =new Html5QrcodeScanner('reader', {
    qrbox:{
        width:250,
        height:250,
    },
    fps:20,
   
  

   });
//    $(".html5-qrcode-element").addClass("btn btn-primary");
   scanner.render(success,error);
   function success(result){
    
    window.location.href = `${result}`;

    scanner.clear();
    document.getElementById('reader').remove();

   }

   function error(err)
   {
    consloe.log(err);
   }

    });

    $('.searchs').on("click",function(){


        $(".qrcontent").addClass("d-none");
  $(".search-content").removeClass("d-none");
  scanner.clear();
    });
    $('.cancelbtn').on("click",function(){

        scanner.clear();
        
        
    });
});



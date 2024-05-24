$(document).ready(function () {
    var scanner;

    // Function to get CSRF cookie value
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('.qrscanner').on("click", function () {
        $(".search-content").addClass("d-none");
        $(".qrcontent").removeClass("d-none");

        scanner = new Html5QrcodeScanner('reader', {
            qrbox: {
                width: 250,
                height: 250,
            },
            fps: 20,
        });

        scanner.render(success, error);

        function success(result) {
            window.location.href = `${result}`;
            scanner.clear();
            document.getElementById('reader').remove();
        }

        function error(err) {
            console.log(err);
        }
    });

    $('.searchs').on("keyup", function () {
        var busNo = $(this).val();
        sendDataToDjango(busNo);
    });

    function sendDataToDjango(busNo) {
        var csrftoken = getCookie('csrftoken'); // Get CSRF token from cookie

        $.ajax({
            url:'search_results/',
            type: 'POST',
            data: {
                'busno': busNo
            },
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader('X-CSRFToken', csrftoken); // Include CSRF token in request headers
            },
            success: function (response) {
                console.log('Data sent successfully');
                console.log('Response:', response);
            
                // Check if bus_info is defined and not empty
                if (response.bus_info && response.bus_info.length > 0) {
                    $(".search-card").removeClass("d-none");
                    const busInfoArray = JSON.parse(response.bus_info);
                    const travelinfo = JSON.parse(response.travel);
                    console.log("reverse",typeof(travelinfo[0].fields.reverse));
                    $('#bus_no').text(busInfoArray[0].fields.bus_no );
                    $('#busname').text(busInfoArray[0].fields.bus_name || 'N/A');

                    if (travelinfo[0].fields.reverse===false)
                    {
                    $('#startplace').text(travelinfo[0].fields.start_place || 'N/A');
                    $('#destination').text(travelinfo[0].fields.destination || 'N/A');
                    }else{
                        
                    $('#startplace').text(travelinfo[0].fields.destination  || 'N/A');
                    $('#destination').text(travelinfo[0].fields.start_place || 'N/A');
                    }
                
                    var bookingPageUrl = '/bus/';
                    var busno=busInfoArray[0].fields.bus_no;
                    // Add busNo as a query parameter to the booking page URL
                    var bookingUrlWithParams = bookingPageUrl + '?busno=' + encodeURIComponent(busno);
                
                    // Update the href attribute of the <a> tag with the booking URL
                    $('.search-card').attr('href', bookingUrlWithParams);
                } else {
                    
                    $(".search-card").addClass("d-none");
                    
                }
            },
            
            error: function (error) {
                console.error('Error sending data:', error);
            }
        });
    }

    $('.cancelbtn').on("click", function () {
        if (scanner) {
            scanner.clear();
        }
    });
});

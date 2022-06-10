/* HEAD*/
$(document).ready(function(){
    $('#send').click(function() {
        if ($('#phone').val().length != 9 || isNaN($('#phone').val())) {
            $('#phone').css('border-color','#FF0000');
            alert('El número de teléfono debe tener al menos 9 números.');
            return false;
        }
        else {
            alert('OK');
        }
    });
});
/*=======**/

/* LOGIN*/

$(document).ready(
    function()
    {
        /*ACA VA EL CODIGO*/


    }
)
/* 1b7c0a97a251a699cfed182a66909cb7a7d94776*/

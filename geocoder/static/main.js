$(document).ready(function() {
       const successHandler = function(resultDiv) {
           return function(result) {
                $.each(result, function(i, field){
                    $(resultDiv).html(field);
                })
           }
       }

       const failHandler = function(resultDiv) {
           return function(jqXHR, textStatus, errorThrown) {
                var msg = '';
                if (jqXHR.status === 0) {
                    msg = 'Not connect.\n Verify Network.';
                } else if (jqXHR.status == 404) {
                    msg = 'Requested page not found. [404]';
                } else if (jqXHR.status == 401) {
                    console.log(jqXHR)
                    msg = jqXHR.responseJSON.error;
                } else if (jqXHR.status == 500) {
                    msg = 'Internal Server Error [500].';
                } else {
                    msg = 'Uncaught Error.\n' + jqXHR.responseText;
                }
                $(resultDiv).html(msg);
           }
        }

    $("#geocode-form").submit(function(){
        $.getJSON("/geocode",
            {'address': document.getElementById('address').value},
        )
        .done(successHandler("#geocode_result"))
        .fail(failHandler("#geocode_result"));

        return false
    });

    $("#reverse-form").submit(function(){
        $.getJSON("/reverse",
            {'lat': document.getElementById('lat').value,
             'lng': document.getElementById('lng').value},
        )
        .done(successHandler("#reverse_result"))
        .fail(failHandler("#reverse_result"));

        return false
    });

    $("#geodistance-form").submit(function(){
        $.getJSON("/geodistance",
            {'lat1': document.getElementById('lat1').value,
             'lng1': document.getElementById('lng1').value,
             'lat2': document.getElementById('lat2').value,
             'lng2': document.getElementById('lng2').value},
        )
        .done(successHandler("#geodistance_result"))
        .fail(failHandler("#geodistance_result"));

        return false
    });

    $("#address-geodistance-form").submit(function(){
        $.getJSON("/address_geodistance",
            {'address1': document.getElementById('address1').value,
             'address2': document.getElementById('address2').value}
        )
        .done(successHandler("#address_geodistance_result"))
        .fail(failHandler("#address_geodistance_result"));

        return false
    });
});

$(document).ready(function() {
    $("#geocode-form").submit(function(){
        $.getJSON("/geocode",
            {'address': document.getElementById('address').value},
            function(result){
                $.each(result, function(i, field){
                    $("#geocode_result").append(field + " ");
                });
            });
        return false
    });
});


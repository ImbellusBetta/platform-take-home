$(document).ready(function() {

    $('#geocode_form').submit(function (e) {
      e.preventDefault();

      $.get('/geocode', {address: document.getElementById('geocode_address').value}
      )
      .done(function(response) {
        result = 'Latitude: ' + parseFloat(response.lat).toFixed(4) + ', Longitude: ' + parseFloat(response.lng).toFixed(4);
        $('#geocode_output').removeClass('alert-danger hide').addClass('alert-success').text(result);
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        var msg = jqXHR.status + ' error: ' + jqXHR.responseJSON.Error;
        $('#geocode_output').removeClass('alert-success hide').addClass('alert-danger').text(msg);
      });

    });

    $('#reverse_form').submit(function (e) {
      e.preventDefault();

      $.get('/reversegeocode', {lat: document.getElementById('latitude').value,
                                lng: document.getElementById('longitude').value}
      )
      .done(function(response) {
        $('#reverse_output').removeClass('alert-danger hide').addClass('alert-success').text(response);
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        var msg = jqXHR.status + ' error: ' + jqXHR.responseJSON.Error;
        $('#reverse_output').removeClass('alert-success hide').addClass('alert-danger').text(msg);
      });

    });

    $('#distance_form').submit(function (e) {
      e.preventDefault();
      var unit = $("input[name='mi_or_km']:checked").val();
      $.get('/distance', {lat1: document.getElementById('latitude1').value,
                          lng1: document.getElementById('longitude1').value,
                          lat2: document.getElementById('latitude2').value,
                          lng2: document.getElementById('longitude2').value,
                          unit: unit
                         }
      )
      .done(function(response) {
        result = parseFloat(response.distance).toFixed(2);
        $('#distance_output').removeClass('alert-danger hide').addClass('alert-success').text(result + ' ' + unit);
      })
      .fail(function(jqXHR, textStatus, errorThrown) {
        console.log(jqXHR);
        var msg = jqXHR.status + ' error: ' + jqXHR.responseJSON.Error;
        $('#distance_output').removeClass('alert-success hide').addClass('alert-danger').text(msg);
      });

    });
});

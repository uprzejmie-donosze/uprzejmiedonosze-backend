function initAutocomplete() {
  var input = document.querySelector('.js-address-autocomplete');
  var autocomplete = new google.maps.places.Autocomplete(input);

  autocomplete.addListener('place_changed', function() {
    var place = autocomplete.getPlace();
    input.value = place.formatted_address.replace(', Polska', '');
  });
}
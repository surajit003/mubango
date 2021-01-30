function initMap() {
    const address = {
        lat: $('#addr_latitude').val(),
        lng: $('#addr_longtitude').val()
    };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: address,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: address,
        map: map,
    });
}

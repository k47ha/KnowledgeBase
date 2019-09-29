function initMap() {
    // set view Canada
    var mymap = L.map('mapid').setView([56.1304, -106.3468], 4);

    // initialize map
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'pk.eyJ1IjoiazQ3aGEiLCJhIjoiY2sxNHk2cmU2MG42dDNkcHlxdG5vMndwaSJ9.JCFRrLYlYnAtUXwpaqXKtw'
    }).addTo(mymap);
}

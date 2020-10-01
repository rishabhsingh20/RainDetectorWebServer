var x = document.getElementById("demo");
function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
  checkres(position);
}

function checkres(position){
    var x1= 28.4089;
    var y1= 77.3178;
    var x2= position.coords.latitude;
    var y2=position.coords.longitude;
    var c = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
    var dis = Math.sqrt(c) * 111;
    var res = document.getElementById("dist");
    res.innerHTML = dis;
    postes(dis);
}

function postes(dis){
    var a = document.getElementById("postres");
    if(dis>10){
        a.innerHTML = "You are out of Range right now"
    }
    /*else{

    }*/
}

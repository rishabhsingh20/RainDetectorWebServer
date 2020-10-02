var x = document.getElementById("demo");
var username=localStorage.getItem("name");
console.log(username);
var email=localStorage.getItem("email");
var user = document.getElementById("user");
console.log(email);
user.innerHTML= username;
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
    var x1= 28.595403;
    var y1= 77.215292;
    var x2= position.coords.latitude;
    var y2=position.coords.longitude;
    var c = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
    var dis = Math.sqrt(c) * 111;
    var res =  document.getElementById("dist") ;
    res.innerHTML = "You are approximately "+ dis + " km far away from the sensor";
    postes(dis);
}

function postes(dis){
    var a = document.getElementById("postres");
    if(dis>10){
        a.innerHTML = "You are out of Range right now";
    }
    else{
      a.innerHTML = "Getting Output Sensor Values...";
      getSensorData();
      makeForm();
    }
}

function getSensorData(){
  var humid = document.getElementById("Humid");
  var temp = document.getElementById("Temp");
  var humidVal = document.getElementById("HumidVal");
  var tempVal = document.getElementById("TempVal");

  humid.style.opacity = 1;
  temp.style.opacity = 1;
  humidVal.style.opacity=1;
  tempVal.style.opacity=1;
}

function makeForm(){
  var form_state = document.getElementById('Secret_Form');
  var inst_state = document.getElementById('Secret_inst');
  form_state.style.opacity=1;
  inst_state.style.opacity=1;
}

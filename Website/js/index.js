function func()
{
var user =  document.getElementById("username").value ;
console.log(user);
localStorage.setItem("name", user);
var email = document.getElementById("email").value;
localStorage.setItem("email", email);
}
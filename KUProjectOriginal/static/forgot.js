function validate() {
  var var1 = document.getElementById('two').value;
  var var2 = document.getElementById('three').value;
  if (var1 != var2) {
    alert("Passwords doesn't match");
    return false;
  }
  return true;
}
function myFunction() {
  var x = document.getElementById("two");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
function openSignIn() {
  document.getElementById('signInPopup').style.display = "block";
}

function closeSignIn() {
  document.getElementById('signInPopup').style.display = "none";
}

function openSignUp() {
  document.getElementById('signInPopup').style.display = "none";
  document.getElementById('signUpPopup').style.display = "block";
}

function closeSignUp() {
  document.getElementById('signUpPopup').style.display = "none";
  document.getElementById('signInPopup').style.display = "block";
}

setTimeout(function() {
  document.getElementById('messages').style.display = 'none';
}, 4000);

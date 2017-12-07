let userBox = document.getElementById('userNameTextBox')
let passBox = document.getElementById('passwordBox')
let loginButton = document.getElementById('login')
let rememberBox = document.getElementById('rememberMe')
let displayUser=document.getElementById("displayUserInfo")

loginButton.addEventListener("click", function() {
  displayUser.innerHTML=userBox.value + ":" + passBox.value
  if (rememberBox.checked) {
    alert("Credentials will be saved!")
  } else {
    alert("Your credentials will not be saved.")
  }
})

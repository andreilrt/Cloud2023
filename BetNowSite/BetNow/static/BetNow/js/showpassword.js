const passwordInput = document.querySelector('#password');
const showPasswordCheckbox = document.querySelector('#show-password');

showPasswordCheckbox.addEventListener('click', function() {
  if (showPasswordCheckbox.checked) {
    passwordInput.type = 'text';
  } else {
    passwordInput.type = 'password';
  }
});
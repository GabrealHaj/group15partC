


const validateFirstName= () => {
    const firstname = document.getElementById('edit-first_name').value.trim();
    const a = /^[a-zA-Z]+$/;
    const message = document.getElementById('firstnameMessage');
    if (!a.test(firstname)) {
               return message.innerText=("First name should contain only letters.");
    }
    else{
        return message.innerText = ('')
    }
}
const validateLastName= () => {
    const lastname = document.getElementById('edit-last_name').value.trim() ;
    const a = /^[a-zA-Z]+$/;
    const message = document.getElementById('lastnameMessage');
    if (!a.test(lastname)) {
          return message.innerText=("Last name should contain only letters.");
    }
    else{
        return message.innerText = ('')
    }
}

function validatePhoneNumber() {
    const phone = document.getElementById('edit-phone_number').value ;
    const a = /^05\d{8}$/;
    const message = document.getElementById('phoneMessage');
    if (!a.test(phone)){
        return message.innerText=('wrong phone number')
    }
    else{
        return message.innerText = ('')
    }
}

function validateBirthDate() {
    const inputDate =new Date(document.getElementById('edit-birth_date').value) ;
    const currentDate = new Date();
    const eighteenYearsAgo = new Date(currentDate.getFullYear() - 18, currentDate.getMonth(), currentDate.getDate());
    const message = document.getElementById('birthdateMessage');
    if  (inputDate >= eighteenYearsAgo){
        return message.innerText = ('should be at least 18 years old')
    }
    else{
        return message.innerText = ('')
    }
}

///password requirements
    //At least 8 characters long
    // Contains at least one digit (0-9)
    // Contains at least one lowercase letter (a-z)
    // Contains at least one uppercase letter (A-Z)
function validatePassword() {
    const password = document.getElementById('edit-password').value;
    const message = []
    const passwordMessage = document.getElementById('passwordMessage');

      if (password.length < 8) {
        message.push('At least 8 characters long');
      }
      if (!/\d/.test(password)) {
        message.push('Contains at least one digit (0-9)');
      }
      if (!/[a-z]/.test(password)) {
        message.push('Contains at least one lowercase letter (a-z)');
      }
      if (!/[A-Z]/.test(password)) {
        message.push('Contains at least one uppercase letter (A-Z)');
      }
  if (message.length > 0) {
    passwordMessage.innerText = message.join('  \n ');
    return false;
  }
  else {
    passwordMessage.innerText = message.join('Password Succeeded');
    return true;
  }
}

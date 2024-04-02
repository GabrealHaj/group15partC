
// /////////////// Validation functions  ////////////////


const validateFirstName= () => {
    const firstname = document.getElementById('reg-first_name').value.trim();
    const a = /^[a-zA-Z]+$/;
    const message = document.getElementById('firstnameMessage');
    if (!a.test(firstname)|| firstname==='') {
               return message.innerText=("First name is required, and should contain only letters.");
    }
    else{
        return message.innerText = ('')
    }
}
const validateLastName= () => {
    const lastname = document.getElementById('reg-last_name').value.trim() ;
    const a = /^[a-zA-Z]+$/;
    const message = document.getElementById('lastnameMessage');
    if (!a.test(lastname)|| lastname==='') {
          return message.innerText=("Last name is required, and should contain only letters.");
    }
    else{
        return message.innerText = ('')
    }
}

function validatePhoneNumber() {
    const phone = document.getElementById('reg-phone_number').value ;
    const a = /^05\d{8}$/;
    const message = document.getElementById('phoneMessage');
    if (!a.test(phone)|| phone===''){
        return message.innerText=('wrong phone number')
    }
    else{
        return message.innerText = ('')
    }
}

function validateBirthDate() {
    const inputDate =new Date(document.getElementById('reg-birth_date').value) ;
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
    const password = document.getElementById('reg-password').value;
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













//
//
//
//
//
//
// ////////////////////////////////  new customer object  ////////////////////////////////////////
// // Initialize the allCustomers list
// const allCustomers = [];
//
// // Create the Customer object
//  class Customer {
//     constructor(email, firstName, lastName, phoneNumber, birthDate, accountPassword, healthCertification) {
//         this.email = email;
//         this.firstName = firstName;
//         this.lastName = lastName;
//         this.phoneNumber = phoneNumber;
//         this.birthDate = new Date(birthDate);
//         this.accountPassword = accountPassword;
//         this.healthCertification = healthCertification;
//     }
//
//     // Getters and setters
//     getFullName() {
//         return `${this.firstName} ${this.lastName}`
//     }
//     getFirstName() {
//         return `${this.firstName} `
//     }
//     getLastName() {
//         return `${this.lastName}`
//     }
//     getPassword() {
//         return `${this.accountPassword}`
//     }
// }
// /////////////////// some objects fot checking if the system woks well ////////////////////
// const customer1 = new Customer('john.doe@example.com', 'John', 'Doe', '0534567890', '2000-01-01', 'password123', 'healthCertification1.pdf');
// const customer2 = new Customer('jan.doe@example.com', 'Jan', 'Doe', '0587654321', '1990-02-02', 'password456', 'healthCertification2.pdf');
// const customer3 = new Customer('bob.smith@example.com', 'Bob', 'Smith', '0576543210', '1985-03-03', 'password789', 'healthCertification3.pdf');
//
// allCustomers.push(customer1, customer2, customer3);
//
//
//
// /////////////// Validation functions  ////////////////
//         function validateEmail(email) {
//             const a = /^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$/;
//             return a.test(email);
//         }
//         function emailAlreadyExists(email, allCustomers) {
//             for (const customer of allCustomers) {
//                     if (customer.email === email) {
//                         return true;
//                     }
//             }
//                 return false;
//         }
//
//         function validateFirstLastName(firstName,lastName){
//                 const regex = /^[a-zA-Z]+$/;
//             if (!regex.test(firstName)) {
//                 window.alert("First name should contain only letters.");
//                 return false;
//                 }
//             else if(!regex.test(lastName)) {
//                 window.alert("Last name should contain only letters.");
//                 return false;
//             }
//             else {
//                 return true;
//             }
//         }
//
// ///////////// when submit registering we  add a new customer for my All Customers list ///////
// function submitRegistration(event) {
//     event.preventDefault(); // Prevent the form from submitting
//
//     // Get form inputs
//     const email = document.getElementById("reg-email").value;
//     const firstName = document.getElementById("reg-first_name").value;
//     const lastName = document.getElementById("reg-last_name").value;
//     const phoneNumber = document.getElementById("reg-phone_number").value;
//     const birthDate = document.getElementById("reg-birth_date").value;
//     const password = document.getElementById("reg-password").value;
//     const healthCertification = document.getElementById("reg-health_certification").value;
//
//     // 1- check the email if exists
//     // 2- check if all inputs are full
//     // 3- if all inputs are valid so do the registration event
//
//     if (email === '' || firstName === '' || lastName === '' || phoneNumber === ''
//              || birthDate === '' || password === '' || healthCertification === '' ){
//             return window.alert("Please fill in all the input fields.");
//     }
//     else if (validateEmail(email) && validatePassword(password)
//             && validateBirthDate(birthDate)
//             && validatePhoneNumber(phoneNumber)
//             && validateHealthCertification(healthCertification)
//             && validateFirstLastName(firstName,lastName)) {
//
//         // Create a customer object
//         let customer = {
//             email: email,
//             firstName: firstName,
//             lastName: lastName,
//             phoneNumber: phoneNumber,
//             birthDate: birthDate,
//             password: password,
//             healthCertification: healthCertification
//         };
//
//         // Add the customer object to the list of customers
//         allCustomers.push(customer);
//
//         //  success message in the console
//         console.log("Customer added:", customer);
//
//         // change button color for 3 second
//         event.target.style.background = 'green'
//         event.target.innerText = 'Succeeded'
//         setTimeout(function() {
//             event.target.style.background = '';
//             event.target.innerText = 'CREATE ACCOUNT';
//             }, 3000);
//
//         // Clear the form
//         document.getElementById("registrationForm").reset();
//
//         console.log(allCustomers)
//     }
//
// }
// // Add event listener to form submission
// document.getElementById("registrationForm").addEventListener("submit", submitRegistration);
//
// window.console.log(allCustomers)
// //allCustomers.pop()
//
//
//






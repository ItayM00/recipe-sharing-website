document.querySelector("#signupForm").addEventListener("submit", function (event) {
    let con_pass = document.querySelector("#confirm_password_entry").value;
    let pass = document.querySelector("#password_entry").value;
    let username = document.querySelector("#username_entry").value;
    let email = document.querySelector("#email_entry").value;
    let date = document.querySelector("#date_entry").value;

    let usernamePattern = /^[A-Za-z0-9]+$/;
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex

    if (pass !== con_pass) {
        alert("Passwords must be the same.");
        event.preventDefault();
        return;
    }
    if (pass.length < 8) {
        alert("Password should be at least 8 characters long.");
        event.preventDefault();
        return;
    }
    if (!usernamePattern.test(username)) {
        alert("Username can only contain letters and numbers.");
        event.preventDefault();
        return;
    }
    if (!emailPattern.test(email)) {
        alert("Not a valid email address.");
        event.preventDefault();
        return;
    }
    if (!isDateValid(date)) {
        event.preventDefault();
        return;
    }
});

function isDateValid(input){

    if (!input) {
        alert("please fill your date of birth!")
        return false;
    }

    const dob = new Date(input);
    const minDate = new Date("1950-01-01");
    const maxDate = new Date();

    if (dob < minDate || dob > maxDate) {
        alert("Date out of allowed range.");
        return false
    }

    return true;
}

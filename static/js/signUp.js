document.querySelector("#signupForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(this);

    let res = checkFieldsInput();
    if(!res) return;

    try {
        const response = await fetch('/signUp', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if(response.ok){
            console.log('Redirecting to:', result.redirect_url);
            window.location.href = result.redirect_url;
        }
        else{
            alert(result.message);
        }
    } catch (error) {
        console.error("error: " + error);
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

function checkFieldsInput(){
let con_pass = document.querySelector("#confirm_password_entry").value;
    let pass = document.querySelector("#password_entry").value;
    let username = document.querySelector("#username_entry").value;
    let email = document.querySelector("#email_entry").value;
    let date = document.querySelector("#date_entry").value;

    let usernamePattern = /^[A-Za-z0-9]+$/;
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex

    if (pass !== con_pass) {
        alert("Passwords must be the same.");
        return false;
    }
    if (pass.length < 8) {
        alert("Password should be at least 8 characters long.");
        return false;
    }
    if (!usernamePattern.test(username)) {
        alert("Username can only contain letters and numbers.");
        return false;
    }
    if (!emailPattern.test(email)) {
        alert("Not a valid email address.");
        return false;
    }
    if (!isDateValid(date)) {
        return false;
    }
    return true;
}

document.querySelector("#signupForm").addEventListener("submit", function (event) {
    let con_pass = document.querySelector("#confirm_password_entry").value;
    let pass = document.querySelector("#password_entry").value;
    let username = document.querySelector("#username_entry").value;
    let email = document.querySelector("#email_entry").value;

    let usernamePattern = /^[A-Za-z0-9]+$/;
    let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email regex

    if (pass !== con_pass) {
        alert("Passwords must be the same.");
        event.preventDefault();
    }
    if (pass.length < 8) {
        alert("Password should be at least 8 characters long.");
        event.preventDefault();
    }
    if (!usernamePattern.test(username)) {
        alert("Username can only contain letters and numbers.");
        event.preventDefault();
    }
    if (!emailPattern.test(email)) {
        alert("Not a valid email address.");
        event.preventDefault();
    }
});

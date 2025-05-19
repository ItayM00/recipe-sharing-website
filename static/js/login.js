document.getElementById('login-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const formData = new FormData(this);

    try {
        const response = await fetch('/login', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if(response.ok){
            console.log('Redirecting to:', result.redirect_url);
            window.location.href = result.redirect_url;
        }
        else{
            document.querySelector(".error-div").style.display = 'flex';
            document.getElementById('message').innerHTML = result.message;
        }
    } catch (error) {
        console.error("error: " + error);
    }
});
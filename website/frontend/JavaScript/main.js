const buttonSignIn = document.getElementById("buttonSignIn");

buttonSignIn.addEventListener("click", () => {
    fetch("http://127.0.0.1:8000/authorization")
        .then(res => res.json())
        .then(data => {
            console.log('Users: ', data);
        } )
        .catch(error => {
            console.log('Error: ', error);
        })
})
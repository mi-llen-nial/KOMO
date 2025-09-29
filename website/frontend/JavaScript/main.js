const buttonSignIn = document.getElementById("buttonSignIn");

buttonSignIn.addEventListener("click", () => {
    const userName = document.getElementById("user_name");
    const userPassword = document.getElementById("user_password")
    try {
        async function userData() {
            const response = await fetch("http://127.0.0.1:8000/authorization", {
                method: "POST", 
                headers: {
                    "Content-type": "application/json"
                }, 
                body: JSON.stringify({
                    'userName': userName,
                    'userPassword': userPassword
                })
            });
            const data = await response.json();
            console.log("Users", data);
            catch(error) {
                console.log("Error", error);
            }
        }
    }   
});
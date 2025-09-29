const buttonSignIn = document.getElementById("buttonSignIn");

buttonSignIn.addEventListener("click", () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/authorization", {
            method: "POST", 
            headers: {
                "Content-type": "applicatoin/json"
            }, 
            body: JSON.stringify({
                user_name: "user_name",
                user_password: "user_password"
            })
        });
        const data = await response.json();
        console.log("Users", data);
        catch(error) {
            console.log("Error", error);
        }
    }   
});
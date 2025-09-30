const buttonSignIn = document.getElementById("buttonSignIn");

buttonSignIn.addEventListener("click", () => {
    const userNameIn = document.getElementById("user_name_in").value;
    const userPasswordIn = document.getElementById("user_password_in").value;

    async function userDataIn() {
        try {
            const response = await fetch("http://127.0.0.1:8000/authorization", {
                method: "POST", 
                headers: {
                    "Content-type": "application/json"
                }, 
                body: JSON.stringify({
                    'userNameIn': userNameIn,
                    'userPasswordIn': userPasswordIn
                })
            });
            const data = await response.json();
            console.log("Users", data);
        } 
        catch(error) {
            console.log("Error", error);
        }
    }
    userDataIn();
});


const buttonSignUp = document.getElementById("buttonSignUp");

buttonSignUp.addEventListener("click", () => {
    const userNameUp = document.getElementById("user_name_up").value;
    const userEmailUp = document.getElementById("user_email_up").value;
    const userPasswordUp = document.getElementById("user_password_up").value;

    async function userDataUp() {
        try {
            const response = await fetch("http://127.0.0.1:8000/authorization", {
                method: "POST", 
                headers: {
                    "Content-type": "application/json"
                }, 
                body: JSON.stringify({
                    'userNameUp': userNameUp,
                    'userEmailUp': userEmailUp,
                    'userPasswordUp': userPasswordUp
                })
            });
            const data = await response.json();
            console.log("Users", data);
        } 
        catch(error) {
            console.log("Error", error);
        }
    }
    userDataUp();
});
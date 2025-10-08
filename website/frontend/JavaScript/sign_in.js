const formIn = document.getElementById("signInForm");

formIn.addEventListener("submit", async(event) => {
    event.preventDefault();

    const userNameIn = document.getElementById("user_name_in").value;
    const userPasswordIn = document.getElementById("user_password_in").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/sign_in", {
            method: "POST", 
            headers: {
                "Content-type": "application/json"
            }, 
            body: JSON.stringify({
                userNameIn, 
                userPasswordIn
            })
        });

        const data = await response.json();
        if(data.ok){
            localStorage.setItem("userNameUp", data.userNameIn);
            localStorage.setItem("userId", data.id);
            window.location.replace("index.html");
        }
        else{
            alert(error, "Error else" || error.detail);
        }

    }
    catch(error) {
        console.log("error", error);
        alert(error);
    };
});

document.addEventListener("DOMContentLoaded", () => {
    const user = localStorage.getItem("userName");
    if(user){
        window.location.replace("index.html");
    }
});



// const buttonSignIn = document.getElementById("buttonSignIn");
// if (buttonSignIn) {
//     buttonSignIn.addEventListener("click", () => {
//         const userNameIn = document.getElementById("user_name_in").value;
//         const userPasswordIn = document.getElementById("user_password_in").value;

//         async function userDataIn() {
//             try {
//                 const response = await fetch("http://127.0.0.1:8000/sign_in", {
//                     method: "POST",
//                     headers: { "Content-Type": "application/json" },
//                     body: JSON.stringify({
//                         userNameIn,
//                         userPasswordIn
//                     })
//                 });
//                 const data = await response.json();
//                 console.log("Users", data);
//             } catch (error) {
//                 console.log("Error", error);
//             }
//         }
//         userDataIn();
//     });
// }
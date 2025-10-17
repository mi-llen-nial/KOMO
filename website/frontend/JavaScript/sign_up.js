const formUp = document.getElementById("signUpForm");
const remeber = document.getElementById("remember");

formUp.addEventListener("submit", async(event) => {
    event.preventDefault();

    const userNameUp = document.getElementById("user_name_up").value;
    const userEmailUp = document.getElementById("user_email_up").value;
    const userPasswordUp = document.getElementById("user_password_up").value;

    try {
        const response = await fetch("https://KOMO.up.railway.app/sign_up", {
            method: "POST", 
            headers: {
                "Content-type": "application/JSON"
            },
            body: JSON.stringify({
                userNameUp,
                userEmailUp,
                userPasswordUp
            })
        });

        const data = await response.json();
        if(data.ok){
            localStorage.setItem("userName", userNameUp);
            window.location.replace("index.html")
        }
        else{
            alert(data.detail || "Error Sign Up");
        }

    }  
    catch(error) {
        console.log("Error catch: ", error);
        alert("is not connected");
    } 
});

window.addEventListener("load", function(){
    const userSave = localStorage.getItem("userNameUp");
    if(userSave){
        userNameUp.value = userSave;
        remeber.checked = true;
    }
})

if(remeber.checked){
    localStorage.setItem(userNameUp, "userNameUp");
}
else{
    localStorage.removeItem("userNameUp");
}



// const buttonSignUp = document.getElementById("buttonSignUp");
// if (buttonSignUp) {
//     buttonSignUp.addEventListener("click", () => {
//         const userNameUp = document.getElementById("user_name_up").value;
//         const userEmailUp = document.getElementById("user_email_up").value;
//         const userPasswordUp = document.getElementById("user_password_up").value;

//         async function userDataUp() {
//             try {
//                 const response = await fetch("http://127.0.0.1:8000/sign_up", {
//                     method: "POST",
//                     headers: { "Content-Type": "application/json" },
//                     body: JSON.stringify({
//                         userNameUp,
//                         userEmailUp,
//                         userPasswordUp
//                     })
//                 });
//                 const data = await response.json();
//                 console.log("Users", data);
//             } catch (error) {
//                 console.log("Error", error);
//             }
//         }
//         userDataUp();
//     });
// }
document.addEventListener("DOMContentLoaded", async() => {
    const user = localStorage.getItem("userName");
    if(!user){
        window.location.replace("sign_in.html");
    }
});
function reveal_password(){
    var password_element = document.getElementById("password");
    var reveal_button = document.getElementById("reveal");

    if (password_element.getAttribute("type") === 'password'){
        password_element.setAttribute('type', 'text');
        reveal_button.textContent = "Hide";
    } else {
        password_element.setAttribute('type', 'password');
        reveal_button.textContent = "Reveal";
    }
}

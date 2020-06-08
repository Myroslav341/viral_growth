function checkPasswordTheSame(){
    var e = document.getElementById("sign_up_button");

    if (document.getElementById("password").value == document.getElementById("confirm_password").value){
        e.removeAttribute("disabled");
        remove_message();
    } else {
        e.setAttribute("disabled", "");
        create_message();
    }
}

function remove_message(){
    var message_added = document.getElementById("message");
    message_added.remove();
}

function create_message(){
    var message_added = document.getElementById("message");

    if (message_added){
        return
    }

    var element = document.createElement("div");
    var text = document.createTextNode("Password does not match");
    var messages = document.getElementById("messages");

    element.style.color = "red";
    element.style.textAlign = "center";
    element.style.paddingBottom = "8px";
    element.id = "message";

    element.appendChild(text);
    messages.appendChild(element);
}

function reveal_password_signup(){
    var password_element = document.getElementById("password");
    var reveal_button = document.getElementById("reveal_password");

    if (password_element.getAttribute("type") === 'password'){
        password_element.setAttribute('type', 'text');
        reveal_button.textContent = "Hide";
    } else {
        password_element.setAttribute('type', 'password');
        reveal_button.textContent = "Reveal";
    }
}

function reveal_confirm_password_signup(){
    var password_element = document.getElementById("confirm_password");
    var reveal_button = document.getElementById("reveal_confirm_password");

    if (password_element.getAttribute("type") === 'password'){
        password_element.setAttribute('type', 'text');
        reveal_button.textContent = "Hide";
    } else {
        password_element.setAttribute('type', 'password');
        reveal_button.textContent = "Reveal";
    }
}

document.getElementById("password").addEventListener('change', checkPasswordTheSame);
document.getElementById("confirm_password").addEventListener('change', checkPasswordTheSame);
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

document.getElementById("password").addEventListener('change', checkPasswordTheSame);
document.getElementById("confirm_password").addEventListener('change', checkPasswordTheSame);
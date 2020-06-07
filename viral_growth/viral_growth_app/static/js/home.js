function ready(){
    var avatar = document.getElementById("avatar");

    avatar.style.height = avatar.width + "px";
    avatar.style.width = avatar.width + "px";
}

function change_uploaded_avatar(){
    var element = document.getElementById("chosen_file")
    var file_path = document.getElementById("avatar_upload").value.split('\\')

    element.textContent = file_path[file_path.length - 1];
}

function change_uploaded_photo(){
    var element = document.getElementById("chosen_file_2")
    var file_path = document.getElementById("photo_upload").value.split('\\')

    element.textContent = file_path[file_path.length - 1];
}

function modal_create(){
    var user_info = document.getElementsByClassName("overflow")[0].outerText;
    var text_input = document.getElementById("message-text");

    text_input.value = user_info;
}


document.getElementById("avatar_upload").addEventListener('change', change_uploaded_avatar);
document.getElementById("photo_upload").addEventListener('change', change_uploaded_photo);
document.addEventListener("DOMContentLoaded", ready);

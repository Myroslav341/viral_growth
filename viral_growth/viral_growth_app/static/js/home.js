function ready(){
    var avatar = document.getElementById("avatar");

    avatar.style.height = avatar.width + "px";
    avatar.style.width = avatar.width + "px";
}

function change_text(){
    var element = document.getElementById("chosen_file")
    var file_path = document.getElementById("avatar_upload").value.split('\\')
    element.textContent = file_path[file_path.length - 1];
}

document.getElementById("avatar_upload").addEventListener('change', change_text);
document.addEventListener("DOMContentLoaded", ready);
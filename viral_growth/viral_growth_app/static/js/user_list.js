function ready(){
    var avatars = document.getElementsByClassName("avatar");

    for (avatar_number in avatars) {
        avatars[avatar_number].style.height = avatars[avatar_number].width + "px";
        avatars[avatar_number].style.width = avatars[avatar_number].width + "px";
    }
}


document.addEventListener("DOMContentLoaded", ready);

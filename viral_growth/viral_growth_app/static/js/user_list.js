function ready(){
    var avatars = document.getElementsByClassName("avatar");

    for (avatar in avatars) {
        avatars[avatar].style.height = avatars[avatar].width + "px";
        avatars[avatar].style.width = avatars[avatar].width + "px";
    }
}


document.addEventListener("DOMContentLoaded", ready);

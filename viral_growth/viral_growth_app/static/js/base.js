function check() {
    fetch("generate-invitation-link/")
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            updateClipboard(data["invitation_link"])
        });

    var x = parseInt(event.clientX) + 12;
    var y = parseInt(event.clientY) + 12;

    create_flash(x, y);
}

function create_flash(x, y) {
    var flash_element = document.getElementById("flash");

    if (flash_element){
        return
    }

    var element = document.createElement("div");
    var text = document.createTextNode("Invitation link was copied to clipboard");
    var flash_elements = document.getElementById("flash_elements");

    element.style.paddingLeft = "15px";
    element.style.paddingRight = "15px";
    element.style.position = "absolute";
    element.style.top = y + "px";
    element.style.left = x + "px";
    element.style.color = "white";
    element.style.backgroundColor = "black";
    element.style.borderRadius = "6px";
    element.id = "flash";
    element.classList.add("none_selectable");

    element.appendChild(text);
    flash_elements.appendChild(element);

    var step = 0.05;
    var opacity = 1;

    setTimeout(() => {
        var timer = setInterval(function () {
            if (opacity <= 0){
                clearInterval(timer);
                element.remove();
            }

            element.style.opacity = opacity;
            element.style.filter = 'alpha(opacity=' + opacity * 100 + ")";
            opacity -= step;
        }, 50);
    }, 1000);
}

function updateClipboard(newClip) {
    navigator.clipboard.writeText(newClip).then(function() {
        /* clipboard successfully set */
    }, function() {
        alert("clipboard copy error");
    });
}

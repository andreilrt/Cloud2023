var dropdown = document.querySelector(".dropdown-opciones-usuario");
var avatar = document.getElementById("user-avatar");

avatar.addEventListener("mouseover", function() {
    dropdown.style.display = "block";
});

document.addEventListener("mouseover", function(e) {
    if (!dropdown.contains(e.target) && !avatar.contains(e.target)) {
        dropdown.style.display = "none";
    }
});
var dropdown = document.querySelector(".dropdown-opciones-usuario");
var avatar = document.getElementById("user-avatar");
var timeoutId;

avatar.addEventListener("mouseover", function() {
    dropdown.style.display = "block";
});

avatar.addEventListener("mouseout", function() {
    timeoutId = setTimeout(function() {
        dropdown.style.display = "none";
    }, 1500);
});

dropdown.addEventListener("mouseover", function() {
    clearTimeout(timeoutId);
});

dropdown.addEventListener("mouseout", function() {
    timeoutId = setTimeout(function() {
        dropdown.style.display = "none";
    }, 100);
});

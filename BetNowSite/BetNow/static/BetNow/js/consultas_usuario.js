document.getElementById("salir-button").addEventListener("click", function() {
    const inicioUrl = this.getAttribute("data-url");
    window.location.href = inicioUrl;
});

$(document).ready(function () {

    // Function for handling payment-method change
    $("#payment-method").on("change", function () {
        var selectedPaymentMethod = $(this).val();
        //bank
        $("#colombian-banks").prop("required", false);
        $("#account-name").prop("required", false);
        $("#account-number").prop("required", false);
        $("#account-type").prop("required", false);
        //pse
        $("#pse-bank").prop("required", false);
        $("#pse-account-type").prop("required", false);
        $("#pse-document-type").prop("required", false);
        $("#pse-document-number").prop("required", false);
        $("#pse-first-name").prop("required", false);
        $("#pse-last-name").prop("required", false);
        $("#pse-email").prop("required", false);
        //card
        $("#cardholder-name").prop("required", false);
        $("#card-number").prop("required", false);
        $("#month").prop("required", false);
        $("#year").prop("required", false);
        $("#cvv").prop("required", false);
        // Hide all panels
        $(".payment-panel").hide();
        //Show panels
        if (selectedPaymentMethod === "banks") {
            // Show the banks panel
            $("#colombian-banks").prop("required", true);
            $("#account-name").prop("required", true);
            $("#account-number").prop("required", true);
            $("#account-type").prop("required", true);
            $("#banks-panel").show();
        } else if (selectedPaymentMethod === "pse") {
            // Show the PSE panel
            $("#pse-bank").prop("required", true);
            $("#pse-account-type").prop("required", true);
            $("#pse-document-type").prop("required", true);
            $("#pse-document-number").prop("required", true);
            $("#pse-first-name").prop("required", true);
            $("#pse-last-name").prop("required", true);
            $("#pse-email").prop("required", true);
            $("#pse-panel").show();
        } else if (selectedPaymentMethod === "card") {
            // Show the card panel
            $("#cardholder-name").prop("required", true);
            $("#card-number").prop("required", true);
            $("#month").prop("required", true);
            $("#year").prop("required", true);
            $("#cvv").prop("required", true);
            $("#card-panel").show();
        }
    });
    
    $("#month, #year").on("blur", function () {
        var monthInput = $("#month").val();
        var yearInput = $("#year").val();
        var pattern = /^(0[1-9]|1[0-2])$/;
        var yearPattern = /^\d{2}$/;
        var currentDate = new Date();
        var currentYear = currentDate.getFullYear().toString().substr(-2);

        if (!pattern.test(monthInput) || !yearPattern.test(yearInput)) {
            $("#month, #year").addClass("invalid");
            $(".invalid-feedback").text("La fecha de vencimiento debe estar en formato MM/YY.");
        } else if (yearInput < currentYear || (yearInput == currentYear && monthInput < currentDate.getMonth() + 1)) {
            $("#month, #year").addClass("invalid");
            $(".invalid-feedback").text("La fecha de vencimiento debe ser posterior a la fecha actual.");
        } else {
            $("#month, #year").removeClass("invalid");
            $(".invalid-feedback").empty();
        }
    });

    document.addEventListener("DOMContentLoaded", function() {
        const avatar = document.querySelector(".user-avatar");
        const optionsContainer = document.querySelector(".user-options-container");
        
        avatar.addEventListener("click", function() {
          optionsContainer.classList.toggle("active");
        });
    });

});
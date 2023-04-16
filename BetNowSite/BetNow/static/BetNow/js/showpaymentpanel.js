$(document).ready(function () {
    // Function for handling payment-method change
    $("#payment-method").on("change", function () {
        var selectedPaymentMethod = $(this).val();
        // Hide all panels
        $(".payment-panel").hide();
        if (selectedPaymentMethod === "banks") {
            // Show the banks panel
            $("#banks-panel").show();
        } else if (selectedPaymentMethod === "pse") {
            // Show the PSE panel
            $("#pse-panel").show();
        } else if (selectedPaymentMethod === "card") {
            // Show the card panel
            $("#card-panel").show();
        }
    });

    // Function for handling colombian-banks change
    $("#colombian-banks").on("change", function () {
        // Check if a valid bank is selected
        if ($(this).val()) {
            // Show the bank account information input fields
            $("#bank-account-info").show();
        } else {
            // Hide the bank account information input fields
            $("#bank-account-info").hide();
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
});



document.addEventListener('DOMContentLoaded', function () {
    // Materialize Initialization
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});

    var datePickers = document.querySelectorAll('.datepicker');
    var instancesDate = M.Datepicker.init(datePickers, {
        format: 'yyyy-mm-dd'
    });

    var nameInput = document.getElementById('name');
    if (nameInput) {
        if (nameInput.readOnly) {
            // Participant is registered, do nothing as the field is already populated
        } else {
            // Participant is not registered, allow them to fill in their name
            // You can add any additional logic here if needed
        }
    }

    // Form Field Validation
    function validatePhoneNumber(phone) {
        const regex = /^\+?\d{1,3}?\d{9,}$/;
        return regex.test(phone);
    }

    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    function validateName(name) {
        const regex = /^[a-zA-Z\s]+$/;
        return regex.test(name);
    }

    document.getElementById("whatsapp_number").addEventListener("blur", function () {
        const phone = this.value;

        if (!validatePhoneNumber(phone)) {
            alert("Invalid phone number format! Please enter a valid mobile number.");
            return;
        }
    });

    document.getElementById("email").addEventListener("blur", function () {
        const email = this.value;

        if (!validateEmail(email)) {
            alert("Invalid email format! Please enter a valid email address.");
            return;
        }
    });

    document.getElementById("name").addEventListener("blur", function () {
        const name = this.value;

        if (!validateName(name)) {
            alert("Invalid name format! Please enter a valid name.");
            return;
        }
    });
});


<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

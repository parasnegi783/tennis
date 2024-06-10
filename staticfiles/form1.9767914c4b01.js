
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, {
        format: 'yyyy-mm-dd',
        yearRange: [1800, 2024], // Set the year range from 1800 to 2024
        defaultDate: new Date(2000, 0, 1),
        setDefaultDate: true,
        i18n: {
            done: 'Select'
        }
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

    document.getElementById("backButton").onclick = function () {
        window.location.href = "home";
    };

    function saveDraft() {
        var draftData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            date_of_birth: document.getElementById('date_of_birth').value,
            whatsapp_number: document.getElementById('whatsapp_number').value,
            city: document.getElementById('city').value,
            indian_tree_tshirt_size: document.getElementById('indian_tree_tshirt_size').value,
            indian_tree_shorts_size: document.getElementById('indian_tree_shorts_size').value,
            food_preference: document.getElementById('food_preference').value,
            stay_arrangement: document.getElementById('stay_arrangement').value,
            first_event_category: document.getElementById('first_event_category').value,
            first_event: document.getElementById('first_event').value,
            second_event_category: document.getElementById('second_event_category').value,
            second_event: document.getElementById('second_event').value
        };
        localStorage.setItem('draftData', JSON.stringify(draftData));
        alert("Your Data is Saved Now...");
    }

    function loadDraft() {
        var draftData = localStorage.getItem('draftData');
        if (draftData) {
            draftData = JSON.parse(draftData);
            document.getElementById('name').value = draftData.name;
            document.getElementById('email').value = draftData.email;
            document.getElementById('date_of_birth').value = draftData.date_of_birth;
            document.getElementById('whatsapp_number').value = draftData.whatsapp_number;
            document.getElementById('city').value = draftData.city;

            var tshirtSizeSelect = document.getElementById('indian_tree_tshirt_size');
            if (tshirtSizeSelect) {
                tshirtSizeSelect.value = draftData.indian_tree_tshirt_size;
            }

            var shortsSizeSelect = document.getElementById('indian_tree_shorts_size');
            if (shortsSizeSelect) {
                shortsSizeSelect.value = draftData.indian_tree_shorts_size;
            }

            var foodPreferenceSelect = document.getElementById('food_preference');
            if (foodPreferenceSelect) {
                foodPreferenceSelect.value = draftData.food_preference;
            }

            var stayArrangementSelect = document.getElementById('stay_arrangement');
            if (stayArrangementSelect) {
                stayArrangementSelect.value = draftData.stay_arrangement;
            }

            var firstEventCategorySelect = document.getElementById('first_event_category');
            if (firstEventCategorySelect) {
                firstEventCategorySelect.value = draftData.first_event_category;
            }

            var firstEventSelect = document.getElementById('first_event');
            if (firstEventSelect) {
                firstEventSelect.value = draftData.first_event;
            }

            var secondEventCategorySelect = document.getElementById('second_event_category');
            if (secondEventCategorySelect) {
                secondEventCategorySelect.value = draftData.second_event_category;
            }

            var secondEventSelect = document.getElementById('second_event');
            if (secondEventSelect) {
                secondEventSelect.value = draftData.second_event;
            }

            M.updateTextFields();
            M.FormSelect.init(document.querySelectorAll('select'));
        }
    }

    document.addEventListener('DOMContentLoaded', function () {
        M.FormSelect.init(document.querySelectorAll('select'));
    });

    function clearDraft() {
        localStorage.removeItem('draftData');
    }

});





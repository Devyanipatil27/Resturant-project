document.addEventListener('DOMContentLoaded', function() {
    // Example: Form validation or interactive features
    const reservationForm = document.querySelector('form');
    
    if (reservationForm) {
        reservationForm.addEventListener('submit', function(event) {
            // Perform form validation
            const name = document.querySelector('input[name="name"]').value;
            const email = document.querySelector('input[name="email"]').value;

            if (!name || !email) {
                alert('Please fill out all required fields.');
                event.preventDefault();
            }
        });
    }
});

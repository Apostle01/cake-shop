// static/js/script.js

// Example: Add a simple alert when the page loads
document.addEventListener("DOMContentLoaded", function () {
    console.log("Cake Shop is ready!");
});

// Example: Add a click event listener to all cake cards
document.querySelectorAll(".cake-card").forEach((card) => {
    card.addEventListener("click", () => {
        alert("You clicked on a cake card!");
    });
});
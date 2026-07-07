// Function to copy text from a specific code block
function copyCode(elementId, button) {
    // 1. Get the text content from the target code block
    const textToCopy = document.getElementById(elementId).innerText;

    // 2. Write the text to the system clipboard
    navigator.clipboard.writeText(textToCopy).then(() => {
        // 3. Change button text and add white text class to indicate success
        button.innerText = "Copied!";
        button.classList.add("text-white");

        // 4. Revert the button back to its original state after 2 seconds (2000ms)
        setTimeout(() => {
            button.innerText = "Copy";
            button.classList.remove("text-white");
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy text: ', err);
    });
}
// Function to copy text from a specific code block.
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
document.getElementById('scanForm').addEventListener('submit', function (e) {
    const urlInput = document.getElementById('urlInput');
    const customError = document.getElementById('customError');
    const inputContainer = document.getElementById('inputContainer');

    if (!urlInput.value || !urlInput.checkValidity()) {
        e.preventDefault();
        customError.classList.remove('d-none');
        inputContainer.style.borderColor = '#ff6b6b';
        inputContainer.style.boxShadow = '0 0 15px rgba(220, 53, 69, 0.3)';
    }
});

document.getElementById('urlInput').addEventListener('input', function () {
    document.getElementById('customError').classList.add('d-none');
    document.getElementById('inputContainer').style.borderColor = 'rgba(13, 202, 240, 0.4)';
    document.getElementById('inputContainer').style.boxShadow = 'none';
});
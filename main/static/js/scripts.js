// static/js/scripts.js

// Function to toggle the visibility of text
function toggleText(link) {
    // Get the previous sibling element, which contains the text to show/hide.
    const moreText = link.previousElementSibling;

    // Check if the element has the 'd-none' class, which hides the element.
    if (moreText.classList.contains('d-none')) {
        // If the element is hidden, remove the 'd-none' class to show it.
        moreText.classList.remove('d-none');
        // Update the link text to indicate that clicking will hide the text.
        link.textContent = '...less';
    } else {
        // If the element is visible, add the 'd-none' class to hide it.
        moreText.classList.add('d-none');
        // Update the link text to indicate that clicking will show more text.
        link.textContent = '...more';
    }
}



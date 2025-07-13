function loadMarkdown(elementId, markdownPath) {
  fetch(markdownPath)
    .then(response => response.text())
    .then(text => {
      document.getElementById(elementId).innerHTML = marked.parse(text);
    })
    .catch(error => {
      document.getElementById(elementId).innerHTML = '<p class="text-danger">Failed to load content.</p>';
      console.error('Error loading markdown:', error);
    });
}

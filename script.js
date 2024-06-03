document.addEventListener("DOMContentLoaded", function() {
    fetch('/messages')
    .then(response => response.json())
    .then(data => {
        const messageFeed = document.getElementById('message-feed');
        data.forEach(message => {
            const listItem = document.createElement('li');
            listItem.classList.add('message');
            listItem.innerHTML = `<p>${message.text}</p>`;
            messageFeed.appendChild(listItem);
        });
    })
    .catch(error => console.error('Errore nel recupero dei messaggi:', error));
});

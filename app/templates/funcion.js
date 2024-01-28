function sendMessage() {
    var userInput = document.getElementById("user-input").value;
    document.getElementById("chat-box").innerHTML += "<div>You: " + userInput + "</div>";
    document.getElementById("user-input").value = "";

    // Envía el mensaje al servidor Python para procesarlo
    fetch('/send-message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chat-box").innerHTML += "<div>Chatbot: " + data.message + "</div>";
    });
}
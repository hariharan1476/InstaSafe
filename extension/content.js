function checkMessage(message) {
    fetch("http://localhost:3000/predict", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        if (data.label === 'abusive') {
            alert("⚠️ Abusive content detected!");
        }
    });
}

// Example DOM watch (mock, must adjust for Instagram)
setInterval(() => {
    let dmText = document.querySelector(".some-ig-dm-class");
    if (dmText) {
        checkMessage(dmText.innerText);
    }
}, 5000);

function sendMessage() {
    const input = document.getElementById("messageInput");
    const chatBox = document.getElementById("chatBox");

    if (input.value.trim() === "") return;

    // buat elemen pesan
    const message = document.createElement("div");
    message.classList.add("message", "me");
    message.innerText = input.value;

    // masukkan ke chat-box
    chatBox.appendChild(message);

    // auto scroll ke bawah
    chatBox.scrollTop = chatBox.scrollHeight;

    // hapus teks input
    input.value = "";
}
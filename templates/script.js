// Reemplaza con la URL de tu backend en Render
const BACKEND_URL = "https://test-n7vw.onrender.com";

async function sendMessage() {
    const response = await fetch(BACKEND_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "Hola, DeepSeek!" })
    });
    // ... resto del código
}
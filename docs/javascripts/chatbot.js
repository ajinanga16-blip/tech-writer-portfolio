document.addEventListener("DOMContentLoaded", () => {

    // Floating button
    const button = document.createElement("button");

    button.innerHTML = "💬";

    button.style.position = "fixed";
    button.style.bottom = "20px";
    button.style.right = "20px";
    button.style.width = "60px";
    button.style.height = "60px";
    button.style.borderRadius = "50%";
    button.style.border = "none";
    button.style.background = "#1976d2";
    button.style.color = "white";
    button.style.fontSize = "26px";
    button.style.cursor = "pointer";
    button.style.zIndex = "9999";
    button.style.boxShadow = "0 4px 12px rgba(0,0,0,0.3)";

    document.body.appendChild(button);

    // Chat container
    const chat = document.createElement("div");

    chat.innerHTML = `
        <div id="chat-window" style="
            display:none;
            position: fixed;
            bottom: 90px;
            right: 20px;
            width: 360px;
            height: 520px;
            background: white;
            border-radius: 16px;
            overflow: hidden;
            z-index: 9999;
            box-shadow: 0 8px 30px rgba(0,0,0,0.25);
            font-family: Arial, sans-serif;
            border: 1px solid #ddd;
        ">

            <div style="
    background:#1976d2;
    color:white;
    padding:16px;
    font-size:18px;
    font-weight:bold;
    display:flex;
    align-items:center;
    gap:10px;
">
    <span style="font-size:22px;">🤖</span>
    <div>
        Docs AI Assistant
        <div style="
            font-size:12px;
            font-weight:normal;
            opacity:0.9;
            margin-top:2px;
        ">
            Ask anything about documentation
        </div>
    </div>
</div>

            <div id="chat-messages" style="
                height:380px;
                overflow-y:auto;
                padding:15px;
                background:#f7f9fc;
                font-size:14px;
                line-height:1.6;
            "></div>

            <div style="
                padding:12px;
                border-top:1px solid #ddd;
                background:white;
            ">

                <input
                    id="chat-input"
                    type="text"
                    placeholder="Ask about documentation..."
                    style="
                        width:100%;
                        padding:12px;
                        border:1px solid #ccc;
                        border-radius:10px;
                        font-size:14px;
                        outline:none;
                    "
                />
            </div>
        </div>
    `;

    document.body.appendChild(chat);

    const windowBox = document.getElementById("chat-window");
    const input = document.getElementById("chat-input");
    const messages = document.getElementById("chat-messages");
    messages.innerHTML = `
    <div style="
        background:white;
        padding:12px 14px;
        border-radius:12px;
        border:1px solid #ddd;
        margin-bottom:16px;
        line-height:1.6;
    ">
        👋 Welcome to the Docs AI Assistant.<br><br>

        Ask questions about:
        <ul style="padding-left:18px; margin-top:8px;">
            <li>User Guides</li>
            <li>API Documentation</li>
            <li>Forecasting workflows</li>
            <li>Documentation metrics</li>
        </ul>
    </div>
`;

    // Toggle widget
    button.addEventListener("click", () => {

        if (windowBox.style.display === "none") {
            windowBox.style.display = "block";
        } else {
            windowBox.style.display = "none";
        }
    });

    // Send question
    input.addEventListener("keypress", async (e) => {

        if (e.key === "Enter") {

            const question = input.value;

            if (!question.trim()) return;

            messages.innerHTML += `
                <div style="
                    margin-bottom:12px;
                    text-align:right;
                ">
                    <div style="
                        display:inline-block;
                        background:#1976d2;
                        color:white;
                        padding:10px 14px;
                        border-radius:12px;
                        max-width:80%;
                    ">
                        ${question}
                    </div>
                </div>
            `;

            input.value = "";

            try {

                const response = await fetch("http://127.0.0.1:8000/ask", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        question: question
                    })
                });

                const data = await response.json();

                let formattedAnswer = data.answer;

// Convert markdown links into clickable links
formattedAnswer = formattedAnswer.replace(
    /\[(.*?)\]\((https?:\/\/[^\s]+)\)/g,
    '<a href="$2" target="_blank" style="color:#1976d2; font-weight:600; text-decoration:none;">🔗 $1</a>'
);

// Line breaks
formattedAnswer = formattedAnswer.replace(/\n/g, "<br>");

// Headings
formattedAnswer = formattedAnswer.replace(
    /### (.*?)(<br>|$)/g,
    '<h3 style="margin-top:12px;">$1</h3>'
);

formattedAnswer = formattedAnswer.replace(
    /#### (.*?)(<br>|$)/g,
    '<h4 style="margin-top:10px;">$1</h4>'
);

messages.innerHTML += `
    <div style="
        margin-bottom:18px;
    ">
        <div style="
            display:inline-block;
            background:white;
            padding:12px 14px;
            border-radius:12px;
            border:1px solid #ddd;
            max-width:90%;
            line-height:1.7;
            font-size:14px;
        ">
            ${formattedAnswer}
        </div>
    </div>
`;

                messages.scrollTop = messages.scrollHeight;

            } catch (error) {

                messages.innerHTML += `
                    <p>Error connecting to AI assistant.</p>
                `;
            }
        }
    });
});
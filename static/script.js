
const chatContainer = document.getElementById('chat-container');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Auto-resize textarea
userInput.addEventListener('input', function () {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
});

// Send on Enter (Shift+Enter for new line)
userInput.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // 1. Add User Message
    addMessage(text, 'user-message');
    userInput.value = '';
    userInput.style.height = 'auto';

    // 2. Add Loading State
    const loadingId = addLoadingMessage();

    try {
        // 3. Call Backend
        const response = await fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: text })
        });

        const data = await response.json();

        // 4. Remove Loading
        removeMessage(loadingId);

        // 5. Render Response
        if (data.error) {
            addMessage(`Error: ${data.error}`, 'system-message');
        } else if (data.test_cases && data.test_cases.length > 0) {
            renderTestCases(data.test_cases);
        } else {
            addMessage("No test cases generated. Try refining your description.", 'system-message');
        }

    } catch (err) {
        removeMessage(loadingId);
        addMessage(`Network Error: ${err.message}`, 'system-message');
    }
}

function addMessage(htmlOrText, className) {
    const div = document.createElement('div');
    div.className = `message ${className}`;
    div.innerHTML = htmlOrText; // Warning: Ensure inputs are sanitized if real HTML
    chatContainer.appendChild(div);
    scrollToBottom();
    return div;
}

function addLoadingMessage() {
    const id = 'loading-' + Date.now();
    const div = document.createElement('div');
    div.id = id;
    div.className = 'message system-message';
    div.innerHTML = '<span class="loader"></span> Generating Test Cases...';
    chatContainer.appendChild(div);
    scrollToBottom();
    return id;
}

function removeMessage(id) {
    const el = document.getElementById(id);
    if (el) el.remove();
}

function renderTestCases(testCases) {
    let tableHtml = `
        <div style="font-weight:600; margin-bottom:10px;">Generated Test Cases:</div>
        <div style="overflow-x:auto;">
        <table class="tc-table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Steps</th>
                    <th>Expected Result</th>
                    <th>Priority</th>
                </tr>
            </thead>
            <tbody>
    `;

    testCases.forEach(tc => {
        tableHtml += `
            <tr>
                <td>${tc.id || '-'}</td>
                <td>${tc.title || '-'}</td>
                <td style="white-space: pre-line;">${tc.steps || '-'}</td>
                <td>${tc.expected_result || '-'}</td>
                <td class="tc-priority-${tc.priority}">${tc.priority || '-'}</td>
            </tr>
        `;
    });

    tableHtml += `</tbody></table></div>`;

    addMessage(tableHtml, 'system-message');
}

function scrollToBottom() {
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

# 💬 Chat Message History Manager (Python)

A simple **Chat Message History Manager** implemented in Python.  
This project simulates a chat application where you can **send messages, undo/redo actions, and track timestamps**.  

---

## 📌 Overview
The Chat Manager allows you to:
- Store messages in a queue before sending.
- Keep a history of sent messages.
- Undo the last sent message.
- Redo undone messages.
- Track **timestamps** for each sent message.

---

## ✨ Features
- 📥 **Queue for Incoming Messages** – Manages messages before sending.  
- 📤 **Stack for Sent Messages** – Keeps a history of sent messages.  
- ↩️ **Undo Last Message** – Remove the most recent message from history.  
- 🔁 **Redo Message** – Restore the last undone message.  
- ⏱ **Timestamps** – Every message shows the time it was sent.  
- 📜 **View Chat History** – Display all messages in order.  

---

## 🛠 Data Structures Used
- **Queue (deque)** → To temporarily hold incoming messages.  
- **Stack (list)** → To store sent messages.  
- **Stack (list)** → To manage undo/redo functionality.  

---

## ▶️ How It Runs
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/chat-history-manager.git
   cd chat-history-manager


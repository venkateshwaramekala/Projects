import time
from collections import deque

class Message:
    def __init__(self, text):
        self.text = text
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def __str__(self):
        return f"[{self.timestamp}] {self.text}"


class ChatHistoryManager:
    def __init__(self):
        self.incoming_queue = deque()   # Queue for incoming messages
        self.sent_stack = []            # Stack for sent messages
        self.undo_stack = []            # Stack for undone messages

    def send_message(self, text):
        """Send a new message (enqueue, push to sent stack)."""
        msg = Message(text)
        self.incoming_queue.append(msg)  # Add to incoming queue
        sent_msg = self.incoming_queue.popleft()  # Dequeue and send
        self.sent_stack.append(sent_msg)  # Push to sent stack
        print(f"✅ Sent: {sent_msg}")

    def undo_message(self):
        """Undo the last sent message (pop from sent stack, push to undo stack)."""
        if not self.sent_stack:
            print("⚠️ No message to undo!")
            return
        last_msg = self.sent_stack.pop()
        self.undo_stack.append(last_msg)
        print(f"↩️ Undo: {last_msg}")

    def redo_message(self):
        """Redo the last undone message (pop from undo stack, push back to sent stack)."""
        if not self.undo_stack:
            print("⚠️ No message to redo!")
            return
        msg = self.undo_stack.pop()
        self.sent_stack.append(msg)
        print(f"🔁 Redo: {msg}")

    def show_history(self):
        """Display all sent messages in order."""
        if not self.sent_stack:
            print("💬 Chat is empty.")
            return
        print("\n📜 Chat History:")
        for msg in self.sent_stack:
            print(f"   {msg}")
        print()


# Example Run
if __name__ == "__main__":
    chat = ChatHistoryManager()

    chat.send_message("Hello!")
    time.sleep(1)
    chat.send_message("How are you?")
    time.sleep(1)
    chat.send_message("Let's meet tomorrow.")

    chat.show_history()

    chat.undo_message()
    chat.show_history()

    chat.redo_message()
    chat.show_history()


import json
import os

class MemoryStore:
    def __init__(self, file_path="memory/communication_history.json"):
        self.file_path = file_path
        self.history = self.load_memory()

    def load_memory(self):
        """Load stored interactions from JSON file."""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return json.load(file)
        return []

    def save_memory(self):
        """Save interactions back to JSON."""
        with open(self.file_path, "w") as file:
            json.dump(self.history, file, indent=4)

    def record_interaction(self, agent1_id, agent2_id, message, response):
        """Store a new communication event."""
        interaction = {
            "agent1": agent1_id,
            "agent2": agent2_id,
            "message": message,
            "response": response
        }
        self.history.append(interaction)
        self.save_memory()

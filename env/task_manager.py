class TaskManager:
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks else self.default_tasks()

    def default_tasks(self):
        """Defines basic tasks for agents to complete using language."""
        return [
            {"task": "describe an object", "expected_format": "adjective-noun"},
            {"task": "ask for help", "expected_format": "verb-noun"},
            {"task": "negotiate an item trade", "expected_format": "noun-price"},
        ]

    def assign_task(self, agent):
        """Assigns a random task to an agent."""
        return random.choice(self.tasks)

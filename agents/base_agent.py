class BaseAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.memory = []  # Stores past interactions

    def observe(self, input_data):
        """Process input from the environment or other agents."""
        raise NotImplementedError

    def act(self):
        """Decide on an action (speaking, learning, etc.)."""
        raise NotImplementedError

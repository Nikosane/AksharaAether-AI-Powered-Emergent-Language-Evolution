from .base_agent import BaseAgent
import random

class LanguageAgent(BaseAgent):
    def __init__(self, agent_id):
        super().__init__(agent_id)
        self.vocabulary = {}  # Stores the agent’s evolving language

    def observe(self, input_data):
        """Process communication from other agents."""
        return self.vocabulary.get(input_data, "Unknown")

    def act(self):
        """Generate a response based on current vocabulary."""
        if not self.vocabulary:
            return "???"  # Placeholder for an unformed language
        return random.choice(list(self.vocabulary.keys()))

    def learn_new_word(self, word, meaning):
        """Expand the vocabulary dynamically."""
        self.vocabulary[word] = meaning

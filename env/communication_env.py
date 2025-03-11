import random

class CommunicationEnv:
    def __init__(self, agents):
        self.agents = agents  # List of LanguageAgent instances
        self.history = []  # Stores interactions

    def step(self):
        """Simulate an interaction between two agents."""
        agent1, agent2 = random.sample(self.agents, 2)
        message = agent1.act()
        response = agent2.observe(message)

        self.history.append((agent1.agent_id, agent2.agent_id, message, response))

        # Learning happens here
        agent2.learn_new_word(message, response)

        return (agent1.agent_id, agent2.agent_id, message, response)

    def reset(self):
        """Resets the environment for a fresh simulation."""
        self.history = []
        for agent in self.agents:
            agent.vocabulary = {}

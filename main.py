import random
from agents.language_agent import LanguageAgent
from env.communication_env import CommunicationEnv
from env.task_manager import TaskManager
from utils.logger import Logger
from utils.config import Config
from memory.memory_store import MemoryStore

# Initialize Logger
logger = Logger()

# Initialize Memory Store
memory = MemoryStore()

# Create Agents
agents = [LanguageAgent(agent_id=f"Agent_{i}") for i in range(Config.NUM_AGENTS)]

# Create Environment
env = CommunicationEnv(agents)

# Create Task Manager
task_manager = TaskManager()

# Simulation Loop
for step in range(Config.MAX_TRAINING_STEPS):
    agent1, agent2, message, response = env.step()

    # Log Interaction
    logger.log_interaction(agent1, agent2, message, response)
    memory.record_interaction(agent1, agent2, message, response)

    # Assign Tasks Randomly
    if random.random() < 0.3:  # 30% chance to assign a task
        task = task_manager.assign_task(agent1)
        logger.log(f"Task Assigned: {agent1.agent_id} → {task['task']}")

print("Simulation Complete. Logs and memory saved.")

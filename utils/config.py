class Config:
    # Simulation Parameters
    NUM_AGENTS = 10
    MAX_TRAINING_STEPS = 1000

    # Language Model Settings (Deepseek R1 1.5)
    USE_DEEPSEEK = True
    MODEL_NAME = "deepseek-r1-1.5b"

    # File Paths
    MEMORY_FILE = "memory/communication_history.json"
    LOG_FILE = "logs/agent_activity.log"

    # Reinforcement Learning Parameters
    LEARNING_RATE = 0.001
    REWARD_SUCCESSFUL_COMMUNICATION = 1.0
    PENALTY_MISUNDERSTANDING = -0.5

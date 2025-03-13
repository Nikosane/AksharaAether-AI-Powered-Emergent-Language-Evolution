import logging
import os

class Logger:
    def __init__(self, log_file="logs/agent_activity.log"):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        self.logger = logging.getLogger()

    def log(self, message):
        """Logs a message to the log file."""
        self.logger.info(message)

    def log_interaction(self, agent1, agent2, message, response):
        """Logs an agent-to-agent communication."""
        log_message = f"{agent1} → {agent2} | Msg: '{message}' | Resp: '{response}'"
        self.logger.info(log_message)

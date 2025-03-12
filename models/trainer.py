import torch
import torch.optim as optim
import torch.nn.functional as F

class Trainer:
    def __init__(self, model, learning_rate=0.001):
        self.model = model
        self.optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    def train_step(self, input_sequence, target_word):
        self.optimizer.zero_grad()
        output = self.model(input_sequence)
        loss = F.cross_entropy(output, target_word)
        loss.backward()
        self.optimizer.step()
        return loss.item()

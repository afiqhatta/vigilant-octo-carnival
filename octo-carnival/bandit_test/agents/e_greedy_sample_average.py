import numpy as np
from bandit_test.test_bed import stat_gaussian_testbed
from bandit_test.agents.test_epsilon_greedy import *

class Agent:
    """
    Agent learning using epsilon greedy method with sample average.

    """
    def __init__(self, arms, epsilon):
        self.arms = arms
        self.action_estimates = np.zeros(arms)
        self.action_numbers = np.zeros(arms)
        self.epsilon = epsilon

    def __reset__(self): # reinitialise values of the learning agent
        self.action_estimates = np.zeros(self.arms)
        self.action_numbers = np.zeros(self.arms)

    def determine_move(self):
        move = np.random.binomial(1,self.epsilon)
        if move == 1:  # rare action
            return 1
        else:
            return 0

    def pick_random(self):
        return

    def pick_greedy(self):
        return

    def epsilon_greedy_learn(self, steps, epsilon, time_steps):

        # configure slot machine
        machine = stat_gaussian_testbed.Slot_Machine(self.arms, 0, 1)
        machine.__configure__()




move = np.random.binomial(1,0)
print(move)
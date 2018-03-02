import numpy as np

class Slot_Machine:

    """
    This is a model of a randomly generated k-armed test bed. Each instance of this class will generate k arms
    corresponding to random means and unit variance. The reward distribution is with this random mean and unit
    variance.
    """
    def __init__(self, arms, time_steps=None):
        self.arms = arms
        self.time_steps = time_steps
        self.reward_means = np.zeros(arms)  # empty array of k reward means.

    def __configure__(self):
        """
        Configure each new slot machine with this function
        :return: a random k vector of reward averages
        """
        self.reward_means = np.random.normal(0,1,self.arms)

    def give_reward(self, action):
        """
        :return: A reward based on which arm is selected, normally distributed with mean
        (assigned reward value at configuration)
        """
        return np.random.normal(self.reward_means[action], 1)

class Test_Bed:

    """
    Class for the testing agent learning methods.
    """

    def __init__(self, number):
        self.number = number

    def run_test(self):
        pass

    def __results__(self):
        pass









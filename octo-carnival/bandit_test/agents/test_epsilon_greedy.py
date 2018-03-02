import numpy as np
from bandit_test.test_bed.stat_gaussian_testbed import Slot_Machine
"""
Testing the epsilon greedy method 
"""

def generate_move(epsilon):
    random_generator = np.random.binomial(1, epsilon)  #here 1 denotes a rare move
    if random_generator == 1:
        return 1
    else:
        return 0

def random_selection(estimates):
    random_generator = np.random.randint(0, len(estimates))
    return random_generator

def greedy_pick(estimates):
    return(np.argmax(estimates))

def epsilon_greedy(epsilon, time_steps, rewards):
    """
    This is an epsilon-greedy method for picking rewards from a stationary reward distribution

    :param epsilon: learning rate
    :param time_steps: how many trials
    :param rewards: a vector of rewards
    :return: a vector of reward estimates!
    """
    estimates = np.zeros(len(rewards))
    picks = np.zeros(len(rewards))

    for i in range(time_steps):

        """Generate action and output choice in the form of an index"""
        move = generate_move(epsilon)
        if move == 1:
            action = random_selection(estimates)
        else:
            action = greedy_pick(estimates)

        """Generate reward"""

        reward = rewards[action]

        """Update estimates"""
        picks[action] = picks[action] + 1
        estimates[action] = estimates[action] + (1/picks[action])*(reward-estimates[action])

        print(str(move) + ' ' + str(action) + ' ' + str(reward))

    return estimates

def epsilon_greedy_random(epsilon, time_steps, arms):
    """
        This is an epsilon-greedy method for picking rewards from a stationary reward distribution

        :param epsilon: learning rate
        :param time_steps: how many trials
        :param arms: how many arms of reward we are dealing with
        :return: a vector of reward estimates!
        """
    reward_machine = Slot_Machine(arms)
    reward_machine.__configure__()
    real_reward_vector = reward_machine.reward_means
    estimates = np.zeros(len(real_reward_vector))
    picks = np.zeros(len(real_reward_vector))

    print("Reward averages for each arm: %s ", real_reward_vector)

    for i in range(time_steps):

        """Generate action and output choice in the form of an index"""
        move = generate_move(epsilon)
        if move == 1:
            action = random_selection(estimates)
        else:
            action = greedy_pick(estimates)

        """Generate reward"""
        reward = reward_machine.give_reward(action)

        """Update estimates"""
        picks[action] = picks[action] + 1
        estimates[action] = estimates[action] + (1 / picks[action]) * (reward - estimates[action])

        print(str(move) + ' ' + str(action) + ' ' + str(reward))

    print("Estimates for each arm: %s", estimates)
    return estimates


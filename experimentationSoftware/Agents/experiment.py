import gym
import time

class Experiment(gym.Env):

    def __init__(self, title:str, env, resultsManager):
        self.title = title
        self.resultsManager = resultsManager
        self.gameMonitorFile = resultsManager.appenderGameMonitorFile(self.title)
        self.env = env

        self.cumulativeReward = 0
        self.cumulativeNoOp = self.env.noOpRedo()

        # Define action and observation spaces for the AI gym
        self.action_space = env.action_space
        self.observation_space = env.observation_space

    def __str__(self):
        return self.title

    def step(self, incentives):
        state, reward, done, info = self.env.step(incentives)
        self.cumulativeReward += reward
        return state, reward, done, info

    def reset(self):
        budget = str(self.env.getBudget())
        self.gameMonitorFile.write(("%.3f,%.3f,%s\n" % (self.cumulativeReward, self.cumulativeNoOp, budget)))
        self.cumulativeReward = 0
        return self.env.reset()

    def render(self, mode='human'):
        self.env.render(mode)

    def close(self):
        self.gameMonitorFile.close()
        self.env.close()

class ExperimentResult:

    def __init__(self, title, reward, noOp):
        self.title = title
        self.reward = reward
        self.noOp = noOp

    def __str__(self):
        return "{title}\n\t{reward} |X| {noOp}".format(
            title=self.title, reward=self.reward, noOp=self.noOp)

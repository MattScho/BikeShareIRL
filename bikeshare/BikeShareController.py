import gym
from gym import spaces
import numpy as np
from bikeshare.SpatialManagers.system_manager import SystemManager
from environment_build.environment_definition import EnvironmentDefinition

class BikeShareController(gym.Env):
    """
    Gym environment implementation to simulate a BikeShare system
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, experimentDefinition:EnvironmentDefinition):
        self.initialBikeLayout = experimentDefinition.getBikeLayout()
        self.users = experimentDefinition.getUsers()
        self.budget = experimentDefinition.getBudget()
        self.systemSize = experimentDefinition.getSystemSize()

        self.numberOfBikes = len(self.initialBikeLayout)
        self.turns = 0

        # Define action and observation spaces for the AI gym
        self.action_space = spaces.Box(0, 5, shape=(self.systemSize,), dtype=np.float32)
        self.observation_space = spaces.Box(0.0, self.systemSize, shape=(self.systemSize,), dtype=np.float32)

        # Create game
        self.game = SystemManager(self.systemSize,  self.budget, self.users.copy(), self.initialBikeLayout.copy())

    def step(self, incentives):
        self.turns += 1
        unservice, noOp = self.game.runWithIncentive(incentives, 60, self.turns)
        return self.getState(), 1.0-unservice, self.turns == 24, {"noOp": 1-noOp}

    def getState(self):
        layout = self.game.getCounts()
        state = np.array(layout)
        return state

    def reset(self):
        self.turns = 0
        self.game = SystemManager(self.systemSize,  self.budget, self.users.copy(), self.initialBikeLayout.copy())
        return self.getState()

    def close(self):
        self.reset()

    def render(self, mode='human'):
        print("\t" + str(self.game.getCounts()))

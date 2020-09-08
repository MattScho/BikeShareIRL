from bikeshare.utils.distributions.distribution import Distribution
import random

class UniformDistribution(Distribution):

    def __init__(self, min:int, max:int):
        super().__init__(min, max)

    def generate(self):
        return random.uniform(self.min, self.max)
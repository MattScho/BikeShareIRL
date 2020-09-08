from bikeshare.utils.distributions.distribution import Distribution
import random

class TriangularDistribution(Distribution):

    def __init__(self, min: int, max: int):
        super().__init__(min, max)

    def generate(self):
        return random.triangular(self.min, self.max)

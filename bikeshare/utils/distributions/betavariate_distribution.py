from bikeshare.utils.distributions.distribution import Distribution
import random

class BetaVariateDistribution(Distribution):

    def __init__(self, min: int, max: int, alpha:float=2, beta:float=5):
        '''
        Recommended parameters:
        ID,a,B
        1, a=.5, B=.5
        2, a=5, B=1
        3, a=1, B=3
        4, a=2, B=2
        5, a=2, B=5

        :param min: system minimum
        :param max: system maximum
        :param alpha: alpha parameter in Betavariate distribution
        :param beta: beta parameter in Betavariate distribution
        '''
        super().__init__(min, max)
        self.alpha = alpha
        self.beta = beta

    def generate(self) -> float:
        '''
        Generates a random value using the defined betavariate distribution
        within the defined bounds

        :return: float generated from betavariate distribution within defined bounds
        '''
        return random.betavariate(self.alpha, self.beta) * (self.max - self.min) + self.min

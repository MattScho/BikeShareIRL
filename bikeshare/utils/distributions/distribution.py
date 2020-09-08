class Distribution:
    """
    Abstract class to implement distributions in a controlled way
    """

    def __init__(self, min:int, max:int):
        self.min = min
        self.max = max

    def getMin(self) -> int:
        '''
        Defined lower boundary of the distribution

        :return: defined lower bound
        '''
        return self.min

    def getMax(self) -> int:
        '''
        Defined upper boundary of the distribution

        :return: defined upper bound
        '''
        return self.max

    def generate(self) -> float:
        '''
        Abstract method
        Generate a value from the distribution

        :return: a value generated from the distribution
        '''
        pass

    def isInbounds(self, value):
        '''
        Check if a value is in bounds

        :param value: value to test
        :return: boolean whether or not the value is in bounds
        '''
        return self.min <= value <= self.max

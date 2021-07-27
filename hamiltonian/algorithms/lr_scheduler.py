import math


class LRScheduler:
    def __init__(self, lr):
        self.lr = lr
    
    def __call__(self, k):
        raise NotImplementedError

class BaseLR(LRScheduler):
    def __call__(self, k):
        return self.lr

class LambdaLR(LRScheduler):
    def __init__(self, lr, func):
        self.lr = lr
        self.func = func

    def __call__(self, k):
        return self.func(k)


class DecreasingLR(LRScheduler):
    def __init__(self, lr, threshold):
        self.lr = lr
        self.threshold = threshold
       
    def __call__(self, k):
        if k <= math.ceil(self.threshold):
            return self.lr
        else:
            return self.lr*self.threshold*(2*k+1)/(2*(k+1)**2)

import numpy as np
import matplotlib.pyplot as plt
import abc

class RandomWalk(metaclass = abc.ABCMeta):

    def __init__(self, particle_number, step_number):
        self.particle_number = particle_number
        self.step_number = step_number
        self.clear()

    def clear(self):
        self.particle = np.zeros(self.particle_number)
        self.p_range = range(len(self.particle))
        self.step = range(self.step_number)

    def action(self):
        for i in self.step:
            for j in self.p_range:
                r = np.random.rand()
                if r > 0.5:
                    self.particle[j] += 1
                else:
                    self.particle[j] -= 1
            self.afterOneStep(i, j)
        self.afterAllStep()

    def setParticleNumber(self, particle_number):
        self.particle_number = particle_number
        self.clear()

    #si = step_index, pi = particle index
    @abc.abstractmethod
    def afterOneStep(self, si, pi):
        pass

    @abc.abstractmethod
    def afterAllStep(self):
        pass

class RandomWalkDrawer(RandomWalk):
    def __init__(self, particle_number, step_number):
        self.particle_number = particle_number
        self.step_number = step_number
        self.clear()

    #si = step_index, pi = particle index
    def afterOneStep(self, si, pi):
        if si%5 == 0:
            plt.cla()
            plt.plot(self.particle, self.p_range, ".")
            plt.xlim(-150, 150)
            plt.pause(0.01)
            #plt.show()

    def afterAllStep(self):
        plt.show()

class RandomWalkAnalyzer(RandomWalk):
    def __init__(self, particle_number, step_number):
        self.particle_number = particle_number
        self.step_number = step_number
        self.mean = np.zeros(step_number)
        self.std = np.zeros(step_number)
        self.clear()

    def afterOneStep(self, si, pi):
        self.mean[si] = np.mean(self.particle)
        self.std[si] = np.std(self.particle)

    def afterAllStep(self):
        self.drawMeanVarGraph()

    def drawMeanVarGraph(self):
        plt.plot(self.step, self.std)
        plt.plot(self.step, self.mean, "r")
        plt.xlabel("iteration")
        plt.show()

    # def cal_reg_output(X, Y):
    #     m, b = np.polyfit(X, Y, 1)
    #     return m*X + b
    #
    # def draw_ori_reg_grapghs(X, Y, R):
    #     plt.plot(X, Y, 'r')
    #     plt.plot(X, R, 'k')
    #
    # def cal_correlation(X, Y):
    #     return (len(X)*sum(X*Y) - sum(X)*sum(Y))/sqrt(len(X)*sum(X*X) - sum(X)*sum(X))/sqrt(len(X)*sum(Y*Y)-sum(Y)*sum(Y))

import numpy as np
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import os
import abc

class RandomWalk(metaclass = abc.ABCMeta):

    def __init__(self, particle_number = 1000, step_number = 1000):
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
    def __init__(self, particle_number = 1000, step_number = 1000, ani = False):
        self.particle_number = particle_number
        self.step_number = step_number
        self.ani = ani
        self.clear()
        #for report store the 3 particle state
        self.store_index = {9, int(particle_number/2), particle_number - 1}
        self.p_array = []

    #si = step_index, pi = particle index
    def afterOneStep(self, si, pi):
        if si%5 == 0:
            if self.ani:
                plt.cla()

            plt.xlim(-150, 150)
            plt.plot(self.particle, self.p_range, ".")

            if self.ani:
                plt.pause(0.001)
            #plt.show()
        if si in self.store_index:
            (self.p_array).append(np.copy(self.particle))

    def afterAllStep(self):
        plt.show()

    def drawStoredParticles(self):
        x_labels = np.linspace(-100, 100, 5, dtype=int)
        y_labels = np.linspace(0, 1000, 11, dtype=int)
        f, (ax1, ax2, ax3) = plt.subplots(1,3, sharey=True)
        # f.set_figheight(1920)
        # f.set_figwidth(1020)
        #f.text(0.04, 0.5, 'Particle Index', ha='center', weight='bold', rotation='vertical', fontsize=21)
        f.text(0.48, 0.02, 'Location', va='center', fontsize=40)
        ax1.set_xlim(-100, 100)
        ax1.set_ylabel('Particle Index', fontsize = 40)
        ax1.set_xlabel('(a)Step 10', fontsize = 35)
        ax1.set_xticks(x_labels)
        ax1.set_xticklabels(x_labels, fontsize = 25)
        ax1.set_yticklabels(y_labels, fontsize = 25)
        ax1.plot(self.p_array[0], range(self.particle_number), "o")
        ax2.set_xlim(-100, 100)
        ax2.set_xlabel('(b)Step 500', fontsize = 35)
        ax2.set_xticks(x_labels)
        ax2.set_xticklabels(x_labels, fontsize = 25)
        ax2.plot(self.p_array[1], range(self.particle_number), "o")
        ax3.set_xlim(-100, 100)
        ax3.set_xlabel('(c)Step 1000', fontsize = 35)
        ax3.set_xticks(x_labels)
        ax3.set_xticklabels(x_labels, fontsize = 25)
        ax3.plot(self.p_array[2], range(self.particle_number), "o")
        # plt.tight_layout()
        f.subplots_adjust(left=0.1, right=0.95, top=1.0, bottom=0.14, hspace = 0, wspace = 0.15)
        plt.show()


    # def getStoredParticles(self):
    #     return self.p_array

class RandomWalkAnalyzer(RandomWalk):
    def __init__(self, particle_number = 1000, step_number = 1000):
        self.particle_number = particle_number
        self.step_number = step_number
        self.mean = np.zeros(step_number)
        self.std = np.zeros(step_number)
        self.clear()

    def afterOneStep(self, si, pi):
        self.mean[si] = np.mean(self.particle)
        self.std[si] = np.std(self.particle)

    def afterAllStep(self):
        pass

    def cal_reg_cor(self):
        self.std_log = np.log(self.std)
        self.std_square = np.square(self.std)
        self.std_sqrt = np.sqrt(self.std)

        self.s_m, self.s_b, self.s_r = self.regression(self.step, self.std)
        self.l_m, self.l_b, self.l_r = self.regression(self.step, self.std_log)
        self.squ_m, self.squ_b, self.squ_r = self.regression(self.step, self.std_square)
        self.sqr_m, self.sqr_b, self.sqr_r = self.regression(self.step, self.std_sqrt)

        self.s_c = self.cal_correlation(self.std, self.s_r)
        self.l_c = self.cal_correlation(self.std_log, self.l_r)
        self.squ_c = self.cal_correlation(self.std_square, self.squ_r)
        self.sqr_c = self.cal_correlation(self.std_sqrt, self.sqr_r)

        print(self.s_c)
        print(self.l_c)
        print(self.squ_c)
        print(self.sqr_c)
        print('squ: m, b')
        print(self.squ_m)
        print(self.squ_b)


    def regression(self, X, Y):
        m, b = np.polyfit(X, Y, 1)
        return (m, b, m*X + b)

    def cal_correlation(self, X, Y):
        return (len(X)*sum(X*Y) - sum(X)*sum(Y))/np.sqrt(len(X)*sum(X*X) - sum(X)*sum(X))/np.sqrt(len(X)*sum(Y*Y)-sum(Y)*sum(Y))

    def drawMeanVarGraph(self):
        mean_line = mlines.Line2D([], [], color='r', label="Mean")
        std_line = mlines.Line2D([], [], color='k', label="Standard deviation")
        plt.legend(handles=[mean_line, std_line], fontsize=30)
        plt.plot(self.step, self.std, "k")
        plt.plot(self.step, self.mean, "r")
        plt.xlabel("iteration", fontsize=40)
        plt.tick_params(axis='both', labelsize=35)
        plt.subplots_adjust(left=0.05, right=0.95, top=1.0, bottom=0.12, hspace = 0, wspace = 0.15)
        plt.show()

    def drawRegressionGraph(self):
        f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col')
        #f.text(0.04, 0.5, 'Particle Index', ha='center', weight='bold', rotation='vertical', fontsize=21)
        f.text(0.48, 0.02, 'iteration', va='center', fontsize=30)
        self._drawRegSubPlot(ax1, self.step, self.std, self.s_r, 'Standard Deviation')
        self._drawRegSubPlot(ax2, self.step, self.std_log, self.l_r, 'Log')
        self._drawRegSubPlot(ax3, self.step, self.std_square, self.squ_r, 'Square(Variance)')
        self._drawRegSubPlot(ax4, self.step, self.std_sqrt, self.sqr_r, 'Sqrt')
        f.subplots_adjust(left=0.06, right=0.98, top=1.0, bottom=0.11, hspace = 0.13, wspace = 0.09)
        plt.show()

    def predict(X):
        return self.squ_m*X + self.squ_b

    def _drawRegSubPlot(self, ax, X, Y, R, xlabel):
        ax.plot(X, Y, 'k')
        ax.plot(X, R, 'r')
        ax.tick_params(axis='both', labelsize=25)
        ax.set_xlabel(xlabel, fontsize=25)

class RandomWalkDiffusionTester(RandomWalk):
    def __init__(self, particle_number = 1000, step_number = 1000):
        self.particle_number = particle_number
        self.step_number = step_number
        self.block_number = 40
        self.reachable_space = np.linspace(-500, 500, 40 + 1)
        self.dx = 2*500/(40)
        self.D = 315
        self.clear()

    def clear(self):
        self.particle = np.zeros(self.particle_number)
        self.p_range = range(len(self.particle))
        self.step = range(self.step_number)
        self.hist = []

    def afterOneStep(self, si, pi):
        (self.hist).append(np.histogram(self.particle, bins = self.reachable_space)[0])
        if si !=0 and si%10 == 0:
            dif_t = self.hist[si] - self.hist[si-1]
            dif_x = ((self.hist[si-1][2:self.block_number] - 2*self.hist[si-1][1:self.block_number-1] + self.hist[si-1][0:self.block_number-2])/self.dx/self.dx)*self.D
            plt.cla()
            plt.ylim(-100, 100)
            plt.plot(dif_t[1:len(dif_t) - 1], "r")
            plt.plot(dif_x, "b")
            plt.pause(0.001)

    def afterAllStep(self):
        plt.show()

    def getDifs(self):
        return (self.dif_t_list, self.dif_x_list)

# import libraries for plotting
import matplotlib.pyplot as plt

# contains implementation for both algorithms
class Solution:
    sums = [0]
    F = [] # for storing the optimal solution
    R = [] # for storing the number of candidates at each time step

    # function for storing cumulative sums
    def initialize_sums(self, data):
        self.F = [0 for i in range(len(data) + 1)]
        self.R = [[] for i in range(len(data) + 1)]
        for i in range(1, len(data) + 1):
            self.sums.append(self.sums[i-1] + data[i - 1])

    # function for getting segment mean
    def get_mean(self, start, end):
        length = end - start + 1
        if start == 0:
            return self.sums[end] / length

        return (self.sums[end] - self.sums[start - 1]) / length

    # function for getting segment cost
    def cost_func(self, start, end):
        if start > end:
            return 0
        mu = self.get_mean(start, end)
        length = end - start + 1
        total = mu * length

        return (-2 * mu * total) + (length * mu * mu)

    # implementation for pelt
    def pelt(self, data, penalty, K):
        self.initialize_sums(data)
        self.F[0] = -1 * penalty
        n = len(data)
        self.R[1] = [0]

        for i in range(1, n + 1):
            best = 1000000023402423424
            candidates = self.R[i]
            for c in candidates:
                current = self.F[c] + penalty + self.cost_func(c + 1, i)
                if current < best:
                    best = current
            self.F[i] = best
            temp = self.R[i]
            temp.append(i)
            if i != n:
                for t in temp:
                    if (self.F[t] + K + self.cost_func(t+1, i)) <= self.F[i]:
                        self.R[i + 1].append(t)
        return [len(r) for r in self.R]


if __name__ == "__main__":
    s = Solution()
    c1 = range(11, 31) # create 20 points with a specific mean
    c2 = range(41, 61) # create 20 points with mean significantly greater than mean of c1
    data = [] # for storing simulated data
    
    # create data so that change points are at 20, 40, 60, 80, 100
    data.extend(c1)
    data.extend(c2)
    data.extend(c1)
    data.extend(c2)
    data.extend(c1)
    
    candidates = s.pelt(data, 2000, 0)
    
    # plot the candidates stored at each time step for pelt
    plt.plot(range(1, 101), candidates[1:])
    plt.savefig('fig1.png')


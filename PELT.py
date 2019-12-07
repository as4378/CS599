def initialize_sums(data, F, R, sums):
    for i in range(1, len(data) + 1):
        sums.append(sums[i-1] + data[i - 1])

def get_mean(start, end, sums):
    length = end - start + 1
    if start == 0:
        return sums[end] / length

    return (sums[end] - sums[start - 1]) / length

def cost_func(start, end, sums):
    if start > end:
        return 0
    mu = get_mean(start, end, sums)
    length = end - start + 1
    total = mu * length

    return (-2 * mu * total) + (length * mu * mu)

def pelt(data, penalty, K):
    sums = [0]
    F = [0 for i in range(len(data) + 1)]
    R = [[] for i in range(len(data) + 1)]
    
    initialize_sums(data, F, R, sums)
    
    F[0] = -1 * penalty
    n = len(data)
    R[1] = [0]

    for i in range(1, n + 1):
        best = 1000000000000
        candidates = R[i]
        for c in candidates:
            current = F[c] + penalty + cost_func(c + 1, i, sums)
            if current < best:
                best = current
        F[i] = best
        temp = R[i]
        temp.append(i)
        if i != n:
            for t in temp:
                if (F[t] + K + cost_func(t+1, i, sums)) <= F[i]:
                    R[i + 1].append(t)
    return [len(r) for r in R]

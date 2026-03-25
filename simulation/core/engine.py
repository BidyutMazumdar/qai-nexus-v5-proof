class Node:
    def __init__(self, energy, compute, latency):
        self.E = energy
        self.C = compute
        self.L = latency

def sync(nodes):
    return sum(n.E * n.C * n.L for n in nodes)

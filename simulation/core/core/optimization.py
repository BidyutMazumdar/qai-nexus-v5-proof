def optimize(nodes):
    for n in nodes:
        n.C *= (n.E / max(n.L, 0.01))
    return nodes

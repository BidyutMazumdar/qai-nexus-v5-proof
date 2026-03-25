from core.engine import Node, sync
from core.optimization import optimize

nodes = [
    Node(0.82, 0.75, 0.21),
    Node(0.78, 0.80, 0.19),
    Node(0.85, 0.72, 0.23),
    Node(0.88, 0.77, 0.18),
    Node(0.81, 0.74, 0.22),
    Node(0.79, 0.79, 0.20),
    Node(0.84, 0.76, 0.19),
    Node(0.86, 0.78, 0.17),
]

before = sync(nodes)
optimized = optimize(nodes)
after = sync(optimized)

gain = (after - before) / before * 100

print("Before:", round(before, 2))
print("After:", round(after, 2))
print("Gain %:", round(gain, 2))

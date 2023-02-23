import random

def randomizer(n,dim):
    points = []
    for i in range(n):
        point = [random.uniform(-1000,1000) for _ in range(dim)]
        points.append(point)
    return points
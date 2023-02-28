import distance as d

def nearest_points(points):
    n = len(points)
    nearest2 = [points[0],points[1]]
    min2 = d.distance(points[0],points[1])
    for i in range(n):
        for j in range(i+1,n):
            if d.distance(points[i],points[j]) < min2:
                min2 = d.distance(points[i],points[j])
                nearest2 = [points[i],points[j]]
    return nearest2
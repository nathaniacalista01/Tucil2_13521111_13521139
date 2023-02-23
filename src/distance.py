import math

def distance(p1,p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))

def nearest_points(points):
    n = len(points)
    if (n <= 1):
        return None
    elif (n == 2):
        return points
    else:
        sorted_points = sorted(points, key=lambda p: p[0])
        left = sorted_points[:(n//2)]
        right = sorted_points[(n//2):]

        nearest_left = nearest_points(left)
        nearest_right = nearest_points(right)

        if (nearest_left is None):
            nearest = nearest_right
        elif (nearest_right is None):
            nearest = nearest_left
        else:
            left_d = distance(nearest_left[0],nearest_left[1])
            right_d = distance(nearest_right[0],nearest_right[1])
            min = left_d
            if (right_d < min):
                min = right_d
        return nearest

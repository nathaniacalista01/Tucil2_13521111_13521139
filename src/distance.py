import math
import sort as s

# Rumus untuk menghitung jarak
def distance(p1,p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))

#Rumus mencari nearest points 
def nearest_points(points):
    count = 0
    n = len(points)
    if (n <= 1):
        return None, count
    elif (n == 2):
        return points, count
    else:
        left = points[:(n//2)]
        right = points[(n//2):]

        nearest_left, countleft = nearest_points(left)
        nearest_right, countright = nearest_points(right)

        count = count + countleft + countright

        if (nearest_left is None):
            nearest = nearest_right
        elif (nearest_right is None):
            nearest = nearest_left
        else:
            left_d = distance(nearest_left[0],nearest_left[1])
            right_d = distance(nearest_right[0],nearest_right[1])
            count += 2

            if (right_d < left_d):
                min = right_d
                nearest = nearest_right
            else:
                min = left_d
                nearest = nearest_left

            center = (left[-1][0] + right[0][0]) / 2
            mid = [point for point in points if(abs(point[0] - center) < min)]
            n_mid = len(mid)

            for i in range (n_mid):
                for j in range (i+1, n_mid):
                    d = distance(mid[i], mid[j])
                    count += 1
                    if (d < min):
                        nearest = [mid[i],mid[j]]
                        min = d
        return nearest, count
import randomizer as r
import distance as d
import plot as p
import sort as s
import time

n = int(input("Please input the number of points: "))
while n < 2:
    print("A minimum number of 2 points is needed!")
    n = int(input("Please input the number of points: "))

dim = int(input("Please input the dimension: "))
while n < 1:
    print("The smallest dimension possible is 1.")
    dim = int(input("Please input the dimension: "))

points = r.randomizer(n,dim)
print("Your random points are: ")
for i in range(n):
    print(points[i])

sorted = s.merge_sort(points)
start = time.time()
nearest = d.nearest_points(sorted)
end = time.time()
print("Your nearest pair of points are: ", end="")
print(nearest)

print("Runtime: ", end="")
print(end-start)

p.plot(dim,points,nearest)
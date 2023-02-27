import randomizer as r
import distance as d
import plot as p
import sort as s

n = int(input("Please input the number of points: "))
dim = int(input("Please input the dimension: "))

points = r.randomizer(n,dim)
print("Your random points are: ")
for i in range(n):
    print(points[i])

nearest = d.nearest_points(s.merge_sort(points))
# print("Your nearest pair of points are: ")
# print(nearest)

# p.plot(dim,points,nearest)
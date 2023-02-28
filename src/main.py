import randomizer as r
import distance as d
import plot as p
import sort as s
import input as i
import coretan as t
import time as tm

i.welcomeMsg()
n,dim = i.inputUser()

points = r.randomizer(n,dim)
print("Your random points are: ")
for i in range(n):
    print(points[i])

st = tm.perf_counter_ns()
nearest = d.nearest_points(s.merge_sort(points))
et = tm.perf_counter_ns()
# nearest2 = d.nearest_points(t.merge_sort2(points,0))

# for i in range(dim):
#     temp = d.nearest_points(t.merge_sort2(points,i))
#     if(d.distance(nearest2[0],nearest[1]) > d.distance(temp[0],temp[1])):
#         nearest2 = temp

print("Your nearest points are : ",nearest)
print("Distance : ", d.distance(nearest[0],nearest[1]))
print("Execution time : {0:.2f} ".format((et-st)/1000),"miliseconds")

# print(nearest2)
# print("Distance 2 : ",d.distance(nearest2[0],nearest2[1]))

# print("Your nearest pair of points are: ")
# print(nearest)

# p.plot(dim,points,nearest)
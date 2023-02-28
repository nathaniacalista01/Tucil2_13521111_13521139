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

# Divide and Conquer
sorted = s.merge_sort(points)
st = tm.perf_counter_ns()
nearest = d.nearest_points(sorted)
et = tm.perf_counter_ns()

print("===== Divide and Conquer Solution =====")
print("Your nearest points are : ",nearest)
print("Distance : ", d.distance(nearest[0],nearest[1]))
print("Execution time : {0:.2f} ".format((et-st)/1000),"miliseconds")

p.plot(dim,points,nearest)

# Brute Force
st2 = tm.perf_counter_ns()
nearest2 = [points[0],points[1]]
min2 = d.distance(points[0],points[1])

for i in range(n):
    for j in range(i+1,n):
        if d.distance(points[i],points[j]) < min2:
            min2 = d.distance(points[i],points[j])
            nearest2 = [points[i],points[j]]
et2 = tm.perf_counter_ns()

print("===== Brute Force Solution =====")
print("Your nearest points are : ",nearest2)
print("Distance : ", d.distance(nearest2[0],nearest2[1]))
print("Execution time : {0:.2f} ".format((et2-st2)/1000),"miliseconds")

p.plot(dim,points,nearest2)
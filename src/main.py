import randomizer as r
import distance as d
import plot as p
import sort as s
import input as i
import bruteforce as b
import time as tm

i.welcomeMsg()
n,dim = i.inputUser()

points = r.randomizer(n,dim)
print("==================== DONE RANDOMIZING ====================")
print("Do you want to see all the points that were generated?(y/n)")
print("==========================================================")
options=input()
while(True):
    if(options == "y" or options == "Y" or options == "N" or options == "n"):
        break
    else:
        print("Input not valid!")

if(options == "y" or options == "Y"):
    for i in range(n):
        print(points[i])

# Divide and Conquer
sorted = s.merge_sort(points)
st = tm.perf_counter_ns()
nearest, count = d.nearest_points(sorted)
et = tm.perf_counter_ns()

print("\033[91m================= Divide and Conquer Solution ================ \033[0m ")
print("Your nearest points are : ")
print(nearest[0])
print(nearest[1])
print("Distance : ", d.distance(nearest[0],nearest[1]))
print("Euclidean distance computation count : ", count)
print("\033[92mExecution time : {0:.2f} ".format((et-st)/1000000),"miliseconds\033[0m")
print("\033[91m============================================================= \033[0m")
print()

p.plot(dim,points,nearest)

# Brute Force
st2 = tm.perf_counter_ns()
nearest2, count2 = b.nearest_points(points)
et2 = tm.perf_counter_ns()

print("\033[93m==================== Brute Force Solution ===================  \033[0m")
print("Your nearest points are : ")
print(nearest2[0])
print(nearest2[1])
print("Distance : ", d.distance(nearest2[0],nearest2[1]))
print("Euclidean distance computation count : ", count2)
print("\033[92mExecution time : {0:.2f} ".format((et2-st2)/1000000),"miliseconds\033[0m ")
print("\033[93m==============================================================  \033[0m")

# p.plot(dim,points,nearest2)
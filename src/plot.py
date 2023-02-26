import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(dim, points, nearest):
    others = []
    for p in points:
        if p not in nearest:
            others.append(p)

    if dim == 1:
        fig, ax = plt.subplots()

        x = [p[0] for p in others]
        ax.plot(x, [0]*len(others), 'bo')

        if nearest is not None:
            n = [p[0] for p in nearest]
            ax.plot(n, [0,0], 'ro')

        ax.set_yticks([])

        ax.axhline(y=0, color='k')


    elif dim == 2:
        x = [p[0] for p in others]
        y = [p[1] for p in others]

        plt.plot(x, y, 'bo')

        if nearest is not None:
            p1,p2 = nearest
            plt.plot([p1[0],p2[0]],[p1[1],p2[1]],'ro')

    elif dim == 3:
        plot = plt.figure()
        axis = plot.add_subplot(111, projection='3d')

        x = [p[0] for p in others]
        y = [p[1] for p in others]
        z = [p[2] for p in others]
        axis.scatter(x, y, z, c='b')

        # Plot the nearest pair of points in red.
        if nearest is not None:
            p1, p2 = nearest
            axis.scatter([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], c='r')

        axis.set_xlabel('X')
        axis.set_ylabel('Y')
        axis.set_zlabel('Z')
    
    else:
        print("Dimension is not visualizable")
    
    plt.show()
    
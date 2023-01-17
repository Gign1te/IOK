import matplotlib.pyplot as plt
def plot_trajectory(mb, tr):
    #i = 0
   # j = 0
    for i in range(len(mb.material_points)):
        for j in range(len(mb.material_points)):
            plt.plot(mb.material_points[i].coord_x, mb.material_points[j].coord_y, 'r.')
            print(i)
    for i in range(len(mb.material_points)):
        for j in range(len(mb.material_points)):
            plt.plot(tr.point_trajectories[i].x, tr.point_trajectories[j].y, 'b', linewidth=0.2)
            time = len(tr.point_trajectories[i].x) - 1
            plt.plot(tr.point_trajectories[i].x[time], tr.point_trajectories[j].y[time], 'g.')
    plt.axis('equal')
    plt.grid()
    plt.show()
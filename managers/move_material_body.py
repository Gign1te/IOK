import models.material_point
import managers.v1_x
import managers.v2_y
import models.point_trajectory
import models.body_trajectory
import models.butcher_table


def move_material_body(time, h, moved_body):
    point_trajectories = []
    butcher_table = models.butcher_table.butcher_table
    for i in range(len(moved_body.material_points)):
        t = 1
        x_0 = moved_body.material_points[i].x_0
        y_0 = moved_body.material_points[i].y_0
        x_t = [x_0]
        y_t = [y_0]
        for n in range(int(time / h) + 1):
            x_k = x_t[n]
            y_k = y_t[n]
            f_1x = managers.v1_x.v1_x(t, x_k)
            f_2x = managers.v1_x.v1_x(t + butcher_table.c[1] * h, x_k + h * butcher_table.a[1][0] * f_1x)
            f_3x = managers.v1_x.v1_x(t + butcher_table.c[2] * h, x_k + h * butcher_table.a[2][0] * f_1x + h * butcher_table.a[2][1] * f_2x)
            f_4x = managers.v1_x.v1_x(t + butcher_table.c[3] * h, x_k + h * butcher_table.a[3][0] * f_1x + h * butcher_table.a[3][1] * f_2x + h * butcher_table.a[3][2] * f_3x)
            f_1y = managers.v2_y.v2_y(t, y_k)
            f_2y = managers.v2_y.v2_y(t + butcher_table.c[1] * h, y_k + h * butcher_table.a[1][0] * f_1y)
            f_3y = managers.v2_y.v2_y(t + butcher_table.c[2] * h, y_k + h * butcher_table.a[2][0] * f_1y + h * butcher_table.a[2][1] * f_2y)
            f_4y = managers.v2_y.v2_y(t + butcher_table.c[3] * h, y_k + h * butcher_table.a[3][0] * f_1y + h * butcher_table.a[3][1] * f_2y + h * butcher_table.a[3][2] * f_3y)
            x_t.append(x_k + h * (butcher_table.b[0] * f_1x + butcher_table.b[1] * f_2x + butcher_table.b[2] * f_3x + butcher_table.b[3] * f_4x))
            y_t.append(y_k + h * (butcher_table.b[0] * f_1y + butcher_table.b[1] * f_2y + butcher_table.b[2] * f_3y + butcher_table.b[3] * f_4y))
            t += h
        point_trajectories.append(models.point_trajectory.PointTrajectory(moved_body.material_points[i], x_t, y_t))
    body_trajectory = models.body_trajectory.BodyTrajectory(point_trajectories, moved_body)
    return body_trajectory

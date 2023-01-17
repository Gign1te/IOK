import managers.create_material_body
import managers.fields
import managers.move_material_body
import managers.move_though_space
import managers.plot_trajectory

x_corner = 3
y_corner = -3
h = 0.3
time = 1
grid_axis = 2

body = managers.create_material_body.create_material_body(x_corner, y_corner, h)
trajectory = managers.move_material_body.move_material_body(time, h, body)
managers.plot_trajectory.plot_trajectory(body, trajectory)

velocity_fields = managers.move_though_space.move_through_space(time, h, grid_axis)
managers.fields.plot_velocity_fields(velocity_fields, grid_axis, h)

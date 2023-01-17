import models.material_point
import managers.v1_x
import managers.v2_y
import models.material_body
def create_material_body(x_c,y_c,h):
    t = 1
    m = 0
    material_points = []
    for i in range(int(2/h)+1):
        for j in range(int(2/h)+1):
            x = x_c + j*h
            y = y_c + i*h
            material_points.append(models.material_point.MaterialPoint(m, x, y, managers.v1_x.v1_x(t, x), managers.v2_y.v2_y(t, y), x, y, t))
            m += 1
    material_body = models.material_body.MaterialBody(material_points)
    return material_body

from material_point import MaterialPoint
from typing import List

class MaterialBody:
    def __int__(self, material_points: List[MaterialPoint], time):
        self.material_points = material_points
        self.time = time

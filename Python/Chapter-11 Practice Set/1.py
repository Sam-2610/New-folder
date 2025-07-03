"""  Create a class (2-D vector) and use it to create another class representing a 3-D 
vector.  """

class Vector_2D:
    def __init__(self,x_axis,y_axis):
        self.x_axis = x_axis
        self.y_axis = y_axis


class Vector_3D(Vector_2D):
    def __init__(self,x_axis,y_axis,z_axis):
        super().__init__(x_axis,y_axis)
        self.z_axis = z_axis



val = Vector_3D(11,33,22)
print(val.z_axis,val.x_axis,val.y_axis)
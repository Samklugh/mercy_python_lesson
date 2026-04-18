# **************************************
            # MODULES
# **************************************

# Modules are used to make our accessible to all folders in the same directory. To use a module, we need to import it. We can import a module using the import statement followed by the name of the module. For example, if we have a module named "math", we can import it as follows:

# importing from my system files:
# import z1

# print(f"Area of the circle is: {z1.circle_area}")
# print(f"Area of the rectangle is: {z1.rectangle_area}") 
# print(f"Area of the square is: {z1.square_area}")
# print(f"Area of the triangle is: {z1.triangle_area}")
# print(f"Diameter of the circle is: {z1.Circle_diameter}")
# print(f"Volume of the cube is: {z1.cube_volume}")
# print(f"Volume of the cylinder is: {z1.cylinder_volume}")
# print(f"Volume of the prism is: {z1.prism_volume}")
# print(f"Volume of the sphere is: {z1.sphere_volume}")
# print(f"Volume of the cone is: {z1.cone_volume}")
# 

# *****************
  # using aliases
# *****************

# Aliases are used to give a module a different name. This is useful when the module name is too long or when we want to avoid naming conflicts with other modules. We can use the "as" keyword to give a module an alias. For example, if we want to import the "math" module and give it an alias of "m", we can do it as follows:  

# import math as m

# in our case, we can import z1 as follows:
# import z1 as formulas
# 
# # print(f"\n\nArea of the circle is: {formulas.circle_area}")
# # print(f"Area of the rectangle is: {formulas.rectangle_area}")
# # print(f"Area of the square is: {formulas.square_area}")
# # print(f"Area of the triangle is: {formulas.triangle_area}")
# # print(f"Diameter of the circle is: {formulas.Circle_diameter}")
# # print(f"Volume of the cube is: {formulas.cube_volume}")
# # print(f"Volume of the cylinder is: {formulas.cylinder_volume}")
# # print(f"Volume of the prism is: {formulas.prism_volume}")
# # print(f"Volume of the sphere is: {formulas.sphere_volume}")
# # print(f"Volume of the cone is: {formulas.cone_volume}")






# *****************
# using "from" keyword
# *****************

# We can also import specific functions or variables from a module using the "from" keyword. For example, if we want to import only the "circle_area" variable from the "z1" module, we can do it as follows:

from z1 import circle_area

print(f"Area of the circle is: {circle_area}")

# thiat way, we can import only the variables or functions that we need from a module, which can help to reduce memory usage and improve performance.
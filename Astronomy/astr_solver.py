#from sympy import *
import sympy as sp
import numpy as np 


'''
class UnitConversion:
    def __init__(self, unit, si_unit, unit_type):
        self.units = units

    def convert(self, value, )
'''
SPEED_OF_LIGHT = 2.9979E8
GRAV_CONST = 6.670e-11
PLANK_CONST = 6.62607015e-34
BOLTS_CONST = 1.380649e-23
MASS_ELECTRON = 9.109e-31
MASS_PROTON = 1.673e-27
ATOM_MASS_UNIT = 1.661e-27
AVAGRANDRO = 6.022E23
STEF_BOLTZ = 5.67e-8

class EquationToList:

    def __init__(self, solve_for: int, names_list: list):
        self.solve_for = solve_for
        #self.var_nums = var.nums #might not need it
        self.names_list = names_list
    
    def convert_to_list(self) -> list:
        #this is a METHOD

        variable_list = []
        i = 0
        while (i < len(names_list)):
            if i != (solve_for - 1):
                the_var = input(f"Enter {names_list[i]}: ")
                variable_list.append(the_var)
            else:
                the_var = sp.symbols('x')
                variable_list.append(the_var)

            i += 1

#current_eq = EquationToList()

def gravitational_force(solve_for: int):
    ''' 
    Enters an integer representing which equation to solve for
    [1) small mass, 2) large mass), 3) radius, 4) force ]
     '''
    #x = symbol('x')
    names_list = ["small mass", "large mass", "radius", "force"]
    variable_list = []
    i = 0
    while (i < 4):
        if i != (solve_for - 1):
            the_var = input(f"Enter {names_list[i]}: ")
            variable_list.append(the_var)
        else:
            the_var = sp.symbols('x')
            variable_list.append(the_var)

        i += 1
    #solve_for = variable_list.index('x')
    small_m = variable_list[0]
    big_m = variable_list[1]
    radius = variable_list[2]
    force = variable_list[3]
    equation = sp.Eq(force, (GRAV_CONST * small_m * big_m) / (radius ** 2))
    if small_m == 'x':
        solution = sp.solve(equation, small_m)
    elif (big_m == 'x'):
        solution = sp.solve(equation, big_m)
    elif (radius == 'x'):
        solution = sp.solve(equation, radius)
    else: 
        solution = sp.solve(equation, force)

    
gravitational_force(2)
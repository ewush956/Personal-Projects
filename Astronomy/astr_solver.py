import sympy as sp
import numpy as np

SPEED_OF_LIGHT = 2.9979E8
GRAV_CONST = 6.670e-11
PLANK_CONST = 6.62607015e-34
BOLTS_CONST = 1.380649e-23
MASS_ELECTRON = 9.109e-31
MASS_PROTON = 1.673e-27
ATOM_MASS_UNIT = 1.661e-27
AVAGRANDRO = 6.022E23
STEF_BOLTZ = 5.67e-8

all_equations_vars = {
    ## From chapter 1
    'Gravitational force': 
    ["smaller mass", "larger mass", "radius", "Gravitational Force"],
    'Planetary Diameter': 
    ["Linear distance", "angular size in radians", "distance to planet"],
    'Inverse Square Law': 
    ["The Relative Flux at distance", "Luminosity emitted by source", "Distance from source"],
    'Power absorbed by planet': 
    ["Solar Luminosity", "Distance from Planet to Star", "Planetary Radius", "Planetary Albedo"],
    'Power emitted by a Planet': 
    ["Power emitted by Planet","Planetary Radius","Surface temperature on planet"],
    'Equilibrium Temperature': 
    ["Equilibrium Temperature", "Solar Luminosity", "Planetary Albedo","Distance from planet to sun"],
    'Hydrostatic Equilibrium': 
    ["Pressure at distance r from center","Distance from the center(r)", "Planetary Radius", "Average Planetary Density"],
    'Maximum Mountain height': 
    ["Planetary Mass", "Planetary Radius", "Density of the Mountain", "Critical Pressure", "Height of Mountain"],
    ## Atmosphere
    'Atmospheric Pressure' :
    ["Surface Pressure", "Final pressure", "Pressure Gradient", "Surface Temperature", "Altitude",
     "Mean atomic mass", "Surface Gravity"]
}
class EquationToList:

    def __init__(self, solve_for: int, names_list: list):
        self.solve_for = solve_for
        #self.var_nums = var.nums #might not need it
        self.names_list = names_list
    
    def convert_to_list(self) -> list:
        #this is a METHOD

        variable_list = []
        i = 0
        while (i < len(self.names_list)):
            if i != (self.solve_for - 1):
                the_var = input(f"Enter {self.names_list[i]}: ")
                the_var = float(the_var)
                variable_list.append(the_var)
            else:
                #the_var = sp.symbols('x')
                the_var = 'x'
                variable_list.append(the_var)

            i += 1
        return variable_list

def gravitational_force(solve_for) -> float:

    vars_list = all_equations_vars['Gravitational force']
    eq = EquationToList(solve_for, vars_list)
    numerical_list = eq.convert_to_list()

    small_m = numerical_list[0]
    large_m = numerical_list[1]
    radius = numerical_list[2]
    force_g = numerical_list[3]
    x = sp.Symbol('x')

    if (small_m == 'x'):
        small_m = x
    elif (large_m == 'x'):
        large_m = x
    elif (radius == 'x'):
        radius = x
    else:
        force_g = x

    equation = sp.Eq(force_g, (GRAV_CONST * small_m * large_m) / (radius ** 2)) 
    solution = sp.solve(equation, x)
    return solution


equation_function_dictionary = {
    1: gravitational_force
}

def display_equations_list():
    print("Which equation would you like to use?")
    #print(all_equations_vars.keys())
    equations_list = list(all_equations_vars.keys())
    for i in range(len(equations_list)):
        print(f'-{equations_list[i]:<25} [{i+1:}] ')

def choose_variable(eq_selection: int):
    print("Which variable would you like to solve for?")
    equations_list = list(all_equations_vars.keys())
    equation = all_equations_vars.get(equations_list[eq_selection])
    for i in range(len(equation)):
        print(f'-{equation[i]:<25} [{i+1:}] ')
    
    return equations_list
#gravitational_force(1)
def main():

    go_again = True
    while go_again: 
    
        display_equations_list()
        eq_select = int(input("Enter selection: "))
        print("\n")
        equations_list = choose_variable(eq_select - 1)
        solve_for = int(input("Enter selection: ")) 
        
        print("\n")
        solution = equation_function_dictionary[eq_select](solve_for)
        print(f'\n{solution}')
        go_again_prompt = input('Enter another value? (y/n): ')
        go_again_prompt = go_again_prompt.upper()

        if (go_again_prompt == 'Y'):
            go_again = True
        else:
            go_again = False



main()

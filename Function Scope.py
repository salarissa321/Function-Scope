



#---------------------------------------------
#-------------- Function Scope------
#--------------------------------------------



x = 1 # Global Scope

def one() :
    global x
    x = 2
    print(f"Print Variable from Function Scope {x}")


def two() :
    x = 4
    print(f"Print Variable from Function Scope {x}")



print(f"Print Variable from Global Scope {x}") # Print Variable from Global Scope 1

one() # Print Variable from Function Scope 2
two() # Print Variable from Function Scope 4
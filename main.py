
import numpy as np


# ------------------ CONSTANTS --------------------

F_M = 50.1 * 10**6 

V_TUBE = 2.248 * 10**8
V_SOLID = 1.87 * 10**8
V_AIR = 2.99 * 10**8

L_SOLID = 0.3
L_TUBE = 1 # +-0.001

V_C = 2.998 * 10**8

E_0 = 8.854 * 10** -12
MU_0 = 1.1257 * 10** -6

# ------------------------------------------------

def rel_err(v_theo:float, v_exp:float) -> float:
    """Computes the relative error between v_theo and v_exp.

    Args:
        v_theo (float): Theoretical value.
        v_exp (float): Experimental value.

    Returns:
        float: Relative error between the values
    """    
    return abs(v_theo - v_exp) / v_theo * 100


air_xi = np.array([0,0,0,0,0])
air_xf = np.array([1.42, 1.42, 1.41, 1.41, 1.405]) # +- 0.0025
air_mean = np.mean(air_xf - air_xi) # +- 0.0025 ? 

v_air = 4 * F_M * air_mean
rel_err_air = rel_err(V_AIR, v_air)

solid_xi = np.array([1.1475, 1.13, 1.135, 1.15, 1.13])
solid_xf = np.array([1.375, 1.375, 1.3775, 1.38, 1.38]) # +- 0.0025
solid_mean = np.mean(solid_xf - solid_xi) # +- 0.0025 ? 

v_solid = (L_SOLID*v_air) / (L_SOLID + 2*solid_mean)
rel_err_solid = rel_err(V_SOLID, v_solid)

tube_xi = np.array([1.145, 1.145, 1.14, 1.14, 1.12])
tube_xf = np.array([1.375, 1.38, 1.37, 1.3725, 1.3775]) # +- 0.0025
tube_mean = np.mean(solid_xf - solid_xi) # +- 0.0025 ? 

v_tube = (L_TUBE*v_air) / (L_TUBE + 2*solid_mean)
rel_err_tube = rel_err(V_TUBE, v_tube)

if __name__ == '__main__':

    from leastsq import leastsq
    from to_latex import to_latex

    x = ['X_i', 'X_f']

    to_latex(x, [air_xi, air_xf], buf='air.tex', index=False, escape=False, column_format='c|c')
    to_latex(x, [solid_xi, solid_xf], buf='solid.tex', index=False, escape=False, column_format='c|c')
    to_latex(x, [tube_xi, tube_xf], buf='tube.tex', index=False, escape=False, column_format='c|c')

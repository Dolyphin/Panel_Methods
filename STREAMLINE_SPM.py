# FUNCTION - COMPUTE X AND Y GEOMETRIC INTEGRALS FOR SOURCE PANEL METHOD
# Written by: JoshTheEngineer
# YouTube   : www.youtube.com/joshtheengineer
# Website   : www.joshtheengineer.com
# Started   : 01/23/19
# Updated   : 01/23/19 - Started code in MATLAB
#                      - Works as expected
#           : 02/03/19 - Transferred to Python
#                      - Works as expected
#
# PURPOSE
# - Compute the geometric integral at point P due to source panels
# - Source panel strengths are constant, but can change from panel to panel
# - Geometric integral for X-direction: Mx(ij)
# - Geometric integral for Y-direction: My(ij)
#
# REFERENCE
# - [1]: Streamline Geometric Integral SPM, Mx(ij) and My(ij)
#           Link: https://www.youtube.com/watch?v=BnPZjGCatcg
#
# INPUTS
# - XP  : X-coordinate of computation point, P
# - YP  : Y-coordinate of computation point, P
# - XB  : X-coordinate of boundary points
# - YB  : Y-coordinate of boundary points
# - phi : Angle between positive X-axis and interior of panel
# - S   : Length of panel
# 
# OUTPUTS
# - Mx  : Value of X-direction geometric integral (Ref [1])
# - My  : Value of Y-direction geometric integral (Ref [1])

import numpy as np
import math as math

def STREAMLINE_SPM(XP,YP,XB,YB,phi,S):
    
    # Number of panels
    numPan = len(XB)-1                                                          # Number of panels
    
    # Initialize arrays
    Mx = np.zeros(numPan)                                                       # Initialize Ix integral array
    My = np.zeros(numPan)                                                       # Initialize Iy integral array
    
    # Compute integral
    for j in range(numPan):                                                     # Loop over all panels
        # Compute intermediate values
        A = -(XP-XB[j])*np.cos(phi[j]) - (YP-YB[j])*np.sin(phi[j])              # A term
        B  = (XP-XB[j])**2 + (YP-YB[j])**2;                                     # B term
        Cx = -np.cos(phi[j]);                                                   # C term (X-direction)
        Dx = XP - XB[j];                                                        # D term (X-direction)
        Cy = -np.sin(phi[j]);                                                   # C term (Y-direction)
        Dy = YP - YB[j];                                                        # D term (Y-direction)
        E  = math.sqrt(B-A**2);                                                 # E term
        
        # Compute Mx, Ref [1]
        term1 = 0.5*Cx*np.log((S[j]**2 + 2*A*S[j]+B)/B);                        # First term in Mx equation
        term2 = ((Dx-A*Cx)/E)*(math.atan2((S[j]+A),E) - math.atan2(A,E));       # Second term in Mx equation
        Mx[j] = term1 + term2;                                                  # X-direction geometric integral
        
        # Compute My, Ref [1]
        term1 = 0.5*Cy*np.log((S[j]**2 + 2*A*S[j]+B)/B);                        # First term in My equation
        term2 = ((Dy-A*Cy)/E)*(math.atan2((S[j]+A),E) - math.atan2(A,E));       # Second term in My equation
        My[j] = term1 + term2;                                                  # Y-direction geometric integral
    
    return Mx, My                                                               # Return both Mx and My matrices
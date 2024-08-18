# ----------------------------------  
# Exercise 01 of Course "Introduction to Wind Turbine Aerodynamics".
# ----------------------------------
# Import Libraries
import numpy as np
import math
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# a) find R, lambda_D and z
# Define the Variables and Values
R         = 63            # [m]  
Lamda_D   = 7             # [-]
Z         = 3             # [-]

# b) find optimal AoA and cL
# Read and extract data from Excel File (NACA64_A17)
AirfoilFile = pd.read_excel('C:/Users/s/Desktop/VS_Codes/Aerodynamic/Lift_to_Drag_Ratio.xlsx')
print (AirfoilFile)

# Plotting Comparison of AOA vs Cl/Cd
plt.figure()
graph_Cl_Cd = sns.lineplot(x= 'Degree',y= 'Cl', data = AirfoilFile, color = 'Orange', marker = 'o', label = 'Cl')
graph_Cl_Cd = sns.lineplot(x= 'Degree',y= 'Cd', data = AirfoilFile, color = 'Yellow', marker = 'o', label = 'Cd')
plt.title('AOA Vs Cl and Cd')
plt.xlabel('AOA')
plt.ylabel('Cl and Cd')
plt.legend()

# Plotting Comparison of Angle of attact and Lift to Drag ratio
plt.figure()
graph_AOA_LTDR = sns.lineplot(x= 'Degree',y= 'Lift to drag ratio', data = AirfoilFile, color = 'Orange', marker = 'o')
plt.title('AOA Vs Epsilon')
plt.xlabel('AOA')
plt.ylabel('Epsilon')
plt.legend()

# find maximum value of Lift to Drag_ratio
Maximum_Value_of_Lift_to_Drag_Ratio = AirfoilFile['Lift to drag ratio'].max()
print (Maximum_Value_of_Lift_to_Drag_Ratio)

# Entire row details of maximum Lift to drag ratio
Row_Values = AirfoilFile[AirfoilFile['Lift to drag ratio'] == Maximum_Value_of_Lift_to_Drag_Ratio]
print(Row_Values)

# Take Alfa_A and CL directly from Row_Values
Alfa_A = Row_Values['Degree'].iloc[0]               # Angle of Attack
CL = Row_Values['Cl'].iloc[0]                       # Lift Coefficient
print(Alfa_A) 
print(CL)

# c) find twist and chord
# Read NRELoffshBsline5MW_AeroDyn_Equil_noTwr excel file
NRELoffshrbsline5MW = pd.read_excel('C:/Users/s/Desktop/VS_Codes/Aerodynamic/NRELOffshrBsline5MW_AeroDyn_Equil_noTwr.xlsx')
print (NRELoffshrbsline5MW)
# Extract RNodes values from Excel files
r_values = NRELoffshrbsline5MW['RNodes']
print (r_values)

# Define functions of Distrubution twist angle
def Distrubution_Twist_Angle(R,r, Lamda_D, Alfa_A):
    return math.degrees(math.atan((2/3) * (R / (r * Lamda_D)))) - Alfa_A
# Define Loops for repait r values
result_Distrubution_Twist_angle = []
for r in r_values:
    result_D_T_A = Distrubution_Twist_Angle(R, r, Lamda_D, Alfa_A)
    print(f"For r = {r}: Result = {result_Distrubution_Twist_angle}")
    result_Distrubution_Twist_angle.append(result_D_T_A)
print(result_Distrubution_Twist_angle)

# Define function Chord Length
def Chord_Length(R,r, Lamda_D, Z, CL):
    return (1/Z) * (8/9) * ((2 * math.pi * R)/CL) * (1/ (Lamda_D * ((Lamda_D * (r/R))**2 + (4/9) )** (1/2)))
result_Chord_Length = []
for r in r_values:
    r_C_Length = Chord_Length(R, r, Lamda_D, Z, CL)
    print(f"For r = {r}: Result = {result_Chord_Length}")
    result_Chord_Length.append(r_C_Length)
print(result_Chord_Length)

# Read Exercise_01 excel file 
Exercise_01 = pd.read_excel('C:/Users/s/Desktop/VS_Codes/Aerodynamic/Exercise01.xlsx')
print (Exercise_01)
# Chord length values are being exported for Exercise01 excel file
for j in range(len(result_Chord_Length)):
    Exercise_01.iloc[0 + j, 1] = result_Chord_Length[j]
# Distrubution Twist angle values are being exported for Exercise01 excel file
for k in range(len(result_Distrubution_Twist_angle)):
    Exercise_01.iloc[0 + k, 3] = result_Distrubution_Twist_angle[k]    
print (Exercise_01)

Exercise_01.to_excel('C:/Users/s/Desktop/VS_Codes/Aerodynamic/Exercise01_copy.xlsx')

# Plotting Comparison of chord Length
plt.figure()
graph = sns.lineplot(x= 'r',y= 'Chord Betz', data = Exercise_01, color = 'Orange', marker = 'o', label = 'Chord Betz')
graph = sns.lineplot(x= 'r',y= 'Chord NREL', data = Exercise_01, color = 'Yellow', marker = 'o', label = 'Chord NREL')
plt.xticks([2.87,5.60,8.33,11.75,15.85,19.95,24.05,28.15,32.25,36.35,40.45,44.55,48.65,52.75,56.17,58.90,61.63])
plt.title('Comparison Chord Length')
plt.xlabel('r')
plt.ylabel('Chord Length')
plt.legend()

# Plotting Comparison of Twist angle
plt.figure()
graph_2 = sns.lineplot(x= 'r',y= 'Twist Betz', data = Exercise_01, color = 'Orange', marker = 'o', label = 'Twist Betz')
graph_2 = sns.lineplot(x= 'r',y= 'Twist NREL', data = Exercise_01, color = 'Yellow', marker = 'o', label = 'Twist NREL')
plt.xticks([2.87,5.60,8.33,11.75,15.85,19.95,24.05,28.15,32.25,36.35,40.45,44.55,48.65,52.75,56.17,58.90,61.63])
plt.title('Comparison Twist Angle')
plt.xlabel('r')
plt.ylabel('Twist Angle')
plt.legend()
# Show the plot
plt.show()








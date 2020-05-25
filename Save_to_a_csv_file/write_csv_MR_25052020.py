# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:39:58 2020
@author: Mohammad-reza Moeini

            You should first open the visualization.

"""
import numpy as np

' Abaqus modules '
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
from part import *
from material import *
from section import *
from optimization import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from odbAccess import *



# =============================================================================
# Matrix form 
# =============================================================================

def Give_FieldVariable_matrixform(COORD1, COORD2, COORD3, U1, U2, U3):
    """Give the field varialbe in the form of [[c1, c2, c3, u1,u2,u3],...] 
    
    input:
        COORD1, COORD2, COORD3: nodal coordinates
        U1, U2, U3: the interested field variable at nodes
        
    Output:
        U: a matrix includes coordinate and field variable
        
    Note:
        this function helps to save this nodal information into a csv file."""
    U=[]    
    for i in range(0,len(COORD1)):
        
        # coordinate
        c1 = COORD1[i][1][1]
        c2 = COORD2[i][1][1]
        c3 = COORD3[i][1][1]
        
        # Field variable
        u1 = U1[i][1][1]
        u2 = U2[i][1][1]
        u3 = U3[i][1][1]
                
        U.append([c1, c2, c3, u1, u2, u3])
        
    return U


# =============================================================================
# Save to a csv file 
# =============================================================================
    
def Extract_FieldVariable_odb(OdbFile, SetName, csvFile):
    """
    This function saves the nodal displacement field of a given set.
    
    Input:
        OdbFile: The odb file (string) eg.: 'Job-1.odb'
        SetName: the name of your set (string)
        csvFile: csv file name (string).
    
    Output:
        A csv file including nodal coordinate and dispalcement in a form of:
            x, y, z, U1, U2, U3
        will be saved in your Work directory
            
    Note:       
        *** You should first open the visualization ***
            

    """
    
    
    myOdb = openOdb(path = OdbFile)
    nodes=myOdb.rootAssembly.nodeSets[SetName]
    framelen=len(myOdb.steps['Step-1'].frames)


    U1_Fr=session.xyDataListFromField(odb=myOdb, outputPosition=NODAL, variable=(('U',NODAL, ((COMPONENT, 'U1'),  )), ), nodeSets=(SetName, ))
    U2_Fr=session.xyDataListFromField(odb=myOdb, outputPosition=NODAL, variable=(('U',NODAL, ((COMPONENT, 'U2'),  )), ), nodeSets=(SetName, ))
    U3_Fr=session.xyDataListFromField(odb=myOdb, outputPosition=NODAL, variable=(('U',NODAL, ((COMPONENT, 'U3'),  )), ), nodeSets=(SetName, ))
    
    COORD1_Fr=session.xyDataListFromField(odb=myOdb, outputPosition=NODAL, variable=(('COORD',NODAL, ((COMPONENT, 'COOR1'),  )), ), nodeSets=(SetName, ))
    COORD2_Fr=session.xyDataListFromField(odb=myOdb, outputPosition=NODAL, variable=(('COORD',NODAL, ((COMPONENT, 'COOR2'),  )), ), nodeSets=(SetName, ))
    COORD3_Fr=session.xyDataListFromField(odb=myOdb, outputPosition=NODAL, variable=(('COORD',NODAL, ((COMPONENT, 'COOR3'),  )), ), nodeSets=(SetName, ))


    Total = Give_FieldVariable_matrixform(COORD1_Fr, COORD2_Fr, COORD3_Fr,
                                      U1_Fr, U2_Fr, U3_Fr)
    
    
    np.savetxt(csvFile, Total, delimiter=",")


    

Extract_FieldVariable_odb('Dogbone_25052020_03.odb',
                          'FRONT_Y', 'Test_function_002.csv')


# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:39:58 2020
@author: Mohammad-reza Moeini



This python script defines a set of nodes in a FE model of Abaqus. 
Run it in the Graphical User Interface (GUI)--> File/Run Script


There are three main functions namely:
    Node_Set_X, Node_Set_Y, Node_Set_Z
which creates set-node with constant X, Y or Z. (You can also write your own set
definder function by combination of these three). 

To use these functions, you need also input  the instance name. 
    Note:
        If you don't know the instance_name, check Assembly/Instances/
        in the tree graphs.

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



def Functions_Set_Face_AC(Face, Name_Face):
    """AC: ABAQUS_Complementary Fucntion: Set
         To reduce the lines and volume of each set function"""
         
    modelName1='Model-1'
    mdb.models[modelName1].rootAssembly.Set(faces=Face, name=Name_Face)
    mdb.models[modelName1].rootAssembly.Set(name=Name_Face, nodes=mdb.models[modelName1].rootAssembly.sets[Name_Face].nodes)

    


def Node_Set_X(X, modelName, instanceName):
     """ABAQUS_Fucntion: Set
     defines a set of nodes at the front surface of the specimen
     
     input:
         X: Level of the surface
         (Depending of your coordinate system, it may change. But it should be 
         in direction of the thichness).
         modelName: name of the model
         instanceName: name of the instance
                   """     

         
     X=round(X,6); 
      
     FRONT=[]; 
     for i in mdb.models[modelName].rootAssembly.instances[instanceName].faces:
         a=i.pointOn[0]    
    
         if a[0]== X:
             FRONT=FRONT+[mdb.models[modelName].rootAssembly.instances[instanceName].faces.findAt(((a[0],a[1],a[2]),))]
 
    #Assign set
     Functions_Set_Face_AC(FRONT, 'FRONT_X')



def Node_Set_Y(Y, modelName, instanceName):
     """ABAQUS_Fucntion: Set
     defines a set of nodes at the front surface of the specimen
     
     input:
         Y: Level of the surface
        """     
     Y=round(Y,6); 
      
     FRONT=[]; 
     for i in mdb.models[modelName].rootAssembly.instances[instanceName].faces:
         a=i.pointOn[0]    
    
         if a[1]== Y:
             FRONT=FRONT+[mdb.models[modelName].rootAssembly.instances[instanceName].faces.findAt(((a[0],a[1],a[2]),))]
 
    #Assign set
     Functions_Set_Face_AC(FRONT, 'FRONT_Y')



def Node_Set_Z(Z, modelName, instanceName):
     """ABAQUS_Fucntion: Set
     defines a set of nodes at the front surface of the specimen
     
     input:
         Z: Level of the surface
        """     
     Z=round(Z,6); 
      
     FRONT=[]; 
     for i in mdb.models[modelName].rootAssembly.instances[instanceName].faces:
         a=i.pointOn[0]    
    
         if a[2]== Z:
             FRONT=FRONT+[mdb.models[modelName].rootAssembly.instances[instanceName].faces.findAt(((a[0],a[1],a[2]),))]
 
    #Assign set
     Functions_Set_Face_AC(FRONT, 'FRONT_Z')






# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:37:12 2020

@author: momoe
"""
# =============================================================================
# Import
# =============================================================================
#Python:
import numpy as np
# Abaqus modules 
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


# =============================================================================
# Run it in File/Run script
# =============================================================================
def Stress_Strain(Job):
        '''Save stress and strain in a txt file
        
    Job: the Job's name (string)
    '''
        Job=Job+'.odb'
        myOdb = openOdb(path=Job);
        frameRepository = myOdb.steps['Step-1'].frames;
        frameS=[]; frameE=[]; 
        
        #Stress
        frameS.insert(0,frameRepository[-1].fieldOutputs['S'].getSubset(position=INTEGRATION_POINT));
        
        #Strain
        frameE.insert(0,frameRepository[-1].fieldOutputs['E'].getSubset(position=INTEGRATION_POINT));
        
        # empty list for stress and strain
        Stress_total = []
        Strain_total = []
        
        for II in range(0,len(frameS[-1].values)):        
            # Append stress and strain in a list 
            Stress_total.append(frameS[0].values[II].data)
            Strain_total.append(frameE[0].values[II].data)
            
        #save
        np.savetxt('Stress_total',Stress_total,fmt='%.4f') # save strain in a txt file
        np.savetxt('Strain_total',Strain_total,fmt='%.4f') # save strain in a txt file
        
        # It will be saved in your home directory (prbably is C:\Temp)
        # to import it in Python again use: 
        # S = np.loadtxt('Stress_total.txt', dtype = float) 
        
        
        
        
        
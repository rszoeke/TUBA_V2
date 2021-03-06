#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 01:20:46 2016

"""
import external.euclid as eu
import logging
import math

import tuba_vars_and_funcs as tub

from external.UnitCalculator import *
auto_converter(mmNS)

#==============================================================================
#==============================================================================
## Point Properties
#==============================================================================
#==============================================================================
        
#Command to define degree of freedom of a point- 'x' represents freedom, 0 no freedom and a value an imposed deformation
def Block (x='x',y='x',z='x',rx='x',ry='x',rz='x',reference="global"):
    '''The Block function blocks the degree of freedoms of the last created point. Per default all components are set to 'x' 
        which equals to no restriction on the DOF for the respective component. Setting a real value applies a restriction, 
        whereas a value != to 0 implies a deflection/torsion of the point.
        There are several ways how to use it:\n
        Block single compontents by naming --> B(x=0,rz=0)
        reference="global" to block in direction of the global base
        reference="local" to block in directions of the local base of the element      
        '''
    ddl=[x,y,z,rx,ry,rz]
    tub.current_tubapoint.ddl=ddl
    tub.current_tubapoint.ddl_reference=reference
    print (ddl)
 

def Spring (x=0, y=0, z=0, rx=0, ry=0, rz=0,reference="global"):
    """appends a stiffness matrix to the current tubapoint.
    
        Multiple stiffness matrixes can be summed up.    
    """
    stiffness=[x,y,z,rx,ry,rz]
    tub.current_tubapoint.stiffness=stiffness
    tub.current_tubapoint.stiffness_reference=reference
 
def Mass (mass):  
    tub.current_tubapoint.mass=mass
    
def Force(x=0,y=0,z=0,reference="global"):
    """appends a force-vector to the current tubapoint
            
       Multiple force vectors can be summed up. 
    """
  
    force=eu.Vector3(x,y,z)
    tub.current_tubapoint.force.append(force)    

def Moment(rx=0,ry=0,rz=0,reference="local"):
    """appends a moment to the current tubapoint
            
       Multiple moments can be summed up. 
    """
    moment = eu.Vector3(rx,ry,rz)
    tub.current_TubaPoint.moment.append(moment)


def Friction(mu=0):

    tub.current_tubapoint.friction_coefficient=mu

#==============================================================================
#==============================================================================
## Line Properties
#==============================================================================
#==============================================================================
def Model (model):
    """Append a FEM-Model to the defined Vector-Object. The following models are 
    available at the moment:
    
#.  "TUBE": \n      
    The tube model uses a circular cross-section along the 1-dimensonal mesh. The neutral fibre can
    be deformed but not the "wall"(cross-section) itself. This theory gives a 
    good approximation for straight pipes but especially for bents this theory is limited.
    As in a bent, flexibility and stress intensity are strongly influenced by the deformation (ovalisation) of the cross-section
    itself, correction factors namely the Stress Intensity Factor (SIF) and Flexibilty Factor have to be introduced to
    correct the model.\n
    Furthermore, as the crosssection is stiff, the influence of internal pressure can't be calculated. Normally pressure is taken into account
    by superposition after solving the calculation.\n
    Most commercial piping codes and ASME 31.3 work with this model.
    
#.  "TUYAU": \n  
    A more advanced model is the TUYAU model. Along the 1-dimensional mesh,       
    
#.  "RECTANGULAR"  \n

#.  "BEAM" \n
    
#.  "BAR"  \n
    A bar is the most simple finite element. These elements transfer loads in their longitudinal direction but will not bend or transfer any torque or bending moment.
     
     
     
    The following models will be added in the future:


#.    "CABLE" \n

#.    "3D?"\n

    """    
    
    tub.current_model=model
        
def Temperature(T=20,T_ref=20):    
    '''Applies the Temperature T to the following constructed Sections. T_ref is used to simulate cold springs.
      
       At T=T_ref the thermal dilation is set to 0. So if you want to pretension a piping part so that at f.ex. T=300°C 
       the thermal dilation is zero, T_ref has to be set to 300°C'''
    tub.current_temperature=T
    tub.current_ref_temperature=T_ref    
    
def SectionTube(outer_radius,wall_thickness):
    """Defines the cross-section of the piping,beam. In this case, outer Radius and thickness of the piping can be defined.\n
       Additional cross-sections will be added later on"""
    if (outer_radius)==str:
          a="NPS" 
          b="DN"
    tub.current_section=[outer_radius, wall_thickness]

def SectionRectangular(height_y,height_z=0,thickness_y=0,thickness_z=0):
    """Global Function: Defines the cross-section of the beam with rectangular crosssection.
       height_y and height_z are the dimensions in the local coordinate system."""   
    tub.current_section=[height_y,height_z,thickness_y,thickness_z]

def SectionOrientation(degree):
    """Global Function: Lets you define an rotationangle (in degree) for your section
    """
    tub.current_section_orientation=degree

def Pressure(pressure):
    """Defines the internal Pressure of the piping system. For 3D and TUYAU models, this pressure is part of the simulation. \n
       For TUBE -Elements this pressure is only taken into account for the postprocessing by superposing it with the simulation\n
       results.             
    """
    tub.current_pressure=pressure


def Material(material):
    """Global Function: Appends the choosen material to the following vector elements. The material 
    properties can be defined in library_material.py \n
    The material properties can be defines constant or as a function of temperature.    
    
    At the moment, the following materials are accessible: \n
    "SS304"   - f(Temperature)\n
    "SS316"   - f(Temperature)\n
    "CSA53"   - f(Temperature)\n
    \n
    "Ax1"  - constant \n
    "A42"  - constant\n
    "IMS"  - constant\n
    "RIGIDE"  - constant\n
    "ACIER"  - constant    \n
    """
    tub.current_material=material
    
def LinearForce(x=0,y=0,z=0,reference="global"):
    """appends a linear force-vector to the last created vector.
       [N/mm]
            
       Multiple force vectors can be summed up. 
    """    
    force=eu.Vector3(x,y,z)
    tub.dict_tubavectors[-1].linear_force.append(force)    

def RhoFluid(density_fluid):
    """allows to take into account the weight of the fluid in the pipe. """
    
    tub.current_rho_fluid=density_fluid
    print("density_fluid",density_fluid)


def Insulation(insulation_thickness, insulation_density):
    """by providing insulation thickness and density, this function
    allows to take into account the weight of the pipe insulation. """
    
    tub.current_insulation=[insulation_thickness, insulation_density]
    print("Insulation",insulation_thickness, insulation_density)
    
def Windload(x,y,z):     
    pass


def SIF_and_FLEX(SIF='',FLEX=''): 
    if FLEX:
        tub.dict_tubavectors[-1].cflex=FLEX
    if SIF:    
        tub.dict_tubavectors[-1].sif=SIF
    pass
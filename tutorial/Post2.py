# -*- coding: utf-8 -*-

###
### This file is generated automatically by SALOME v7.8.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
theStudy = salome.myStudy

import salome_notebook
notebook = salome_notebook.NoteBook(theStudy)
sys.path.insert( 0, r'/home/jangeorg/TUBA/tutorial/001')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New(theStudy)

O = geompy.MakeVertex(0, 0, 0)
Vx = geompy.MakeVectorDXDYDZ(1, 0, 0)
Vy = geompy.MakeVectorDXDYDZ(0, 1, 0)
Vz = geompy.MakeVectorDXDYDZ(0, 0, 1)
P0_ = geompy.MakeVertex(0, 0, 0)
geomObj_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_2 = geompy.MakeTranslationVectorDistance(P0_, geomObj_1, 100)
Vd2x_P0_ = geompy.MakeVector(P0_, geomObj_2)
P1_ = geompy.MakeVertex(1000, 0, 0)
geomObj_3 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_4 = geompy.MakeTranslationVectorDistance(P1_, geomObj_3, 100)
Vd2x_P1_ = geompy.MakeVector(P1_, geomObj_4)
P2_ = geompy.MakeVertex(2000, 0, 0)
geomObj_5 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_6 = geompy.MakeTranslationVectorDistance(P2_, geomObj_5, 100)
Vd2x_P2_ = geompy.MakeVector(P2_, geomObj_6)
P3_ = geompy.MakeVertex(2850, 0, 0)
geomObj_7 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_8 = geompy.MakeTranslationVectorDistance(P3_, geomObj_7, 100)
Vd2x_P3_ = geompy.MakeVector(P3_, geomObj_8)
P3_4_center_ = geompy.MakeVertex(2850, 150, 0)
geomObj_9 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_10 = geompy.MakeTranslationVectorDistance(P3_4_center_, geomObj_9, 100)
Vd2x_P3_4_center_ = geompy.MakeVector(P3_4_center_, geomObj_10)
P4_ = geompy.MakeVertex(3000, 150, 0)
geomObj_11 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1, 0)
geomObj_12 = geompy.MakeTranslationVectorDistance(P4_, geomObj_11, 100)
Vd2x_P4_ = geompy.MakeVector(P4_, geomObj_12)
P5_ = geompy.MakeVertex(3000, 1150, 0)
geomObj_13 = geompy.MakeVectorDXDYDZ(6.123233995736766e-17, 1, 0)
geomObj_14 = geompy.MakeTranslationVectorDistance(P5_, geomObj_13, 100)
Vd2x_P5_ = geompy.MakeVector(P5_, geomObj_14)
V0 = geompy.MakeVector(P0_, P1_)
CercleExt = geompy.MakeCircle(P0_, V0, 35)
CercleInt = geompy.MakeCircle(P0_, V0, 31)
geomObj_15 = geompy.MakeFaceWires([CercleExt, CercleInt], 1)
geomObj_16 = geompy.MakeWire([V0], 1e-07)
Pipe = geompy.MakePipe(geomObj_15, geomObj_16)
V1 = geompy.MakeVector(P1_, P2_)
CercleExt_1 = geompy.MakeCircle(P1_, V1, 35)
CercleInt_1 = geompy.MakeCircle(P1_, V1, 31)
geomObj_17 = geompy.MakeFaceWires([CercleExt_1, CercleInt_1], 1)
geomObj_18 = geompy.MakeWire([V1], 1e-07)
Pipe_1 = geompy.MakePipe(geomObj_17, geomObj_18)
V2 = geompy.MakeVector(P2_, P3_)
CercleExt_2 = geompy.MakeCircle(P2_, V2, 35)
CercleInt_2 = geompy.MakeCircle(P2_, V2, 31)
geomObj_19 = geompy.MakeFaceWires([CercleExt_2, CercleInt_2], 1)
geomObj_20 = geompy.MakeWire([V2], 1e-07)
Pipe_2 = geompy.MakePipe(geomObj_19, geomObj_20)
V_Bent3 = geompy.MakeArcCenter(P3_4_center_, P3_, P4_,False)
CercleExt_3 = geompy.MakeCircle(P3_, Vd2x_P3_, 35)
CercleInt_3 = geompy.MakeCircle(P3_, Vd2x_P3_, 31)
geomObj_21 = geompy.MakeFaceWires([CercleExt_3, CercleInt_3], 1)
geomObj_22 = geompy.MakeWire([V_Bent3], 1e-07)
Pipe_3 = geompy.MakePipe(geomObj_21, geomObj_22)
V4 = geompy.MakeVector(P4_, P5_)
CercleExt_4 = geompy.MakeCircle(P4_, V4, 35)
CercleInt_4 = geompy.MakeCircle(P4_, V4, 31)
geomObj_23 = geompy.MakeFaceWires([CercleExt_4, CercleInt_4], 1)
geomObj_24 = geompy.MakeWire([V4], 1e-07)
Pipe_4 = geompy.MakePipe(geomObj_23, geomObj_24)
Pipe.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
Pipe_1.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
Pipe_2.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
Pipe_3.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
Pipe_4.SetColor(SALOMEDS.Color(0.8,0.8,0.8))
geompy.addToStudy( O, 'O' )
geompy.addToStudy( Vx, 'Vx' )
geompy.addToStudy( Vy, 'Vy' )
geompy.addToStudy( Vz, 'Vz' )
geompy.addToStudy( P0_, 'P0 ' )
geompy.addToStudy( Vd2x_P0_, 'Vd2x_P0 ' )
geompy.addToStudy( P1_, 'P1 ' )
geompy.addToStudy( Vd2x_P1_, 'Vd2x_P1 ' )
geompy.addToStudy( P2_, 'P2 ' )
geompy.addToStudy( Vd2x_P2_, 'Vd2x_P2 ' )
geompy.addToStudy( P3_, 'P3 ' )
geompy.addToStudy( Vd2x_P3_, 'Vd2x_P3 ' )
geompy.addToStudy( P3_4_center_, 'P3_4_center ' )
geompy.addToStudy( Vd2x_P3_4_center_, 'Vd2x_P3_4_center ' )
geompy.addToStudy( P4_, 'P4 ' )
geompy.addToStudy( Vd2x_P4_, 'Vd2x_P4 ' )
geompy.addToStudy( P5_, 'P5 ' )
geompy.addToStudy( Vd2x_P5_, 'Vd2x_P5 ' )
geompy.addToStudy( V0, 'V0' )
geompy.addToStudyInFather( Pipe, CercleExt, 'CercleExt' )
geompy.addToStudyInFather( Pipe, CercleInt, 'CercleInt' )
geompy.addToStudy( Pipe, 'Pipe' )
geompy.addToStudy( V1, 'V1' )
geompy.addToStudyInFather( Pipe_1, CercleExt_1, 'CercleExt' )
geompy.addToStudyInFather( Pipe_1, CercleInt_1, 'CercleInt' )
geompy.addToStudy( Pipe_1, 'Pipe' )
geompy.addToStudy( V2, 'V2' )
geompy.addToStudyInFather( Pipe_2, CercleExt_2, 'CercleExt' )
geompy.addToStudyInFather( Pipe_2, CercleInt_2, 'CercleInt' )
geompy.addToStudy( Pipe_2, 'Pipe' )
geompy.addToStudy( V_Bent3, 'V_Bent3' )
geompy.addToStudyInFather( Pipe_3, CercleExt_3, 'CercleExt' )
geompy.addToStudyInFather( Pipe_3, CercleInt_3, 'CercleInt' )
geompy.addToStudy( Pipe_3, 'Pipe' )
geompy.addToStudy( V4, 'V4' )
geompy.addToStudyInFather( Pipe_4, CercleExt_4, 'CercleExt' )
geompy.addToStudyInFather( Pipe_4, CercleInt_4, 'CercleInt' )
geompy.addToStudy( Pipe_4, 'Pipe' )
V0 = V0
V1 = V1
V2 = V2
V_Bent3 = V_Bent3
V4 = V4

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New(theStudy)
V0_1 = smesh.Mesh(V0)
Regular_1D_1 = V0_1.Segment()
NumberOfSegments_8_0 = Regular_1D_1.NumberOfSegments(8,None,[])
QuadraticMesh = Regular_1D_1.QuadraticMesh()
isDone = V0_1.Compute()
P0 = V0_1.GroupOnGeom(P0_,'P0 ',SMESH.NODE)
P1 = V0_1.GroupOnGeom(P1_,'P1 ',SMESH.NODE)
V0_2 = V0_1.GroupOnGeom(V0,'V0',SMESH.EDGE)
V1_1 = smesh.Mesh(V1)
Regular_1D_1_1 = V1_1.Segment()
NumberOfSegments_8_0_1 = Regular_1D_1_1.NumberOfSegments(8,None,[])
status = V1_1.AddHypothesis(QuadraticMesh)
isDone = V1_1.Compute()
P1_1 = V1_1.GroupOnGeom(P1_,'P1 ',SMESH.NODE)
P2 = V1_1.GroupOnGeom(P2_,'P2 ',SMESH.NODE)
V1_2 = V1_1.GroupOnGeom(V1,'V1',SMESH.EDGE)
V2_1 = smesh.Mesh(V2)
Regular_1D_1_2 = V2_1.Segment()
NumberOfSegments_8_0_2 = Regular_1D_1_2.NumberOfSegments(8,None,[])
status = V2_1.AddHypothesis(QuadraticMesh)
isDone = V2_1.Compute()
P2_1 = V2_1.GroupOnGeom(P2_,'P2 ',SMESH.NODE)
P3 = V2_1.GroupOnGeom(P3_,'P3 ',SMESH.NODE)
V2_2 = V2_1.GroupOnGeom(V2,'V2',SMESH.EDGE)
V_Bent3_1 = smesh.Mesh(V_Bent3)
Regular_1D_1_3 = V_Bent3_1.Segment()
NumberOfSegments_8_0_3 = Regular_1D_1_3.NumberOfSegments(8,None,[])
status = V_Bent3_1.AddHypothesis(QuadraticMesh)
isDone = V_Bent3_1.Compute()
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.NODE,SMESH.FT_LyingOnGeom,'=',P3_)
aCriteria.append(aCriterion)
aFilter_1 = smesh.GetFilterFromCriteria(aCriteria)
P3_1 = V_Bent3_1.GroupOnFilter( SMESH.NODE, 'P3', aFilter_1 )
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.NODE,SMESH.FT_LyingOnGeom,'=',P4_)
aCriteria.append(aCriterion)
aFilter_2 = smesh.GetFilterFromCriteria(aCriteria)
P4 = V_Bent3_1.GroupOnFilter( SMESH.NODE, 'P4', aFilter_2 )
V_Bent3_2 = V_Bent3_1.GroupOnGeom(V_Bent3,'V_Bent3',SMESH.EDGE)
V4_1 = smesh.Mesh(V4)
Regular_1D_1_4 = V4_1.Segment()
NumberOfSegments_8_0_4 = Regular_1D_1_4.NumberOfSegments(8,None,[])
status = V4_1.AddHypothesis(QuadraticMesh)
isDone = V4_1.Compute()
P4_1 = V4_1.GroupOnGeom(P4_,'P4 ',SMESH.NODE)
P5 = V4_1.GroupOnGeom(P5_,'P5 ',SMESH.NODE)
V4_2 = V4_1.GroupOnGeom(V4,'V4',SMESH.EDGE)
Completed_Mesh = smesh.Concatenate([V0_1.GetMesh(), V1_1.GetMesh(), V2_1.GetMesh(), V_Bent3_1.GetMesh(), V4_1.GetMesh()], 1, 0, 1e-05)
[ P0_1, P1_2, V0_3, P2_2, V1_3, P3_2, V2_3, P3_3, P4_2, V_Bent3_3, P4_3, P5_1, V4_3 ] = Completed_Mesh.GetGroups()
coincident_nodes = Completed_Mesh.FindCoincidentNodes( 1e-05, 0 )
Completed_Mesh.MergeNodes([[ 16, 18 ], [ 33, 35 ], [ 50, 52 ], [ 67, 69 ]], [])
equal_elements = Completed_Mesh.FindEqualElements( Completed_Mesh )
Completed_Mesh.MergeElements( [] )
smesh.SetName(Completed_Mesh, 'Completed_Mesh')
P0_1.SetName( 'P0' )
P1_2.SetName( 'P1' )
P2_2.SetName( 'P2' )
P3_2.SetName( 'P3' )
P4_3.SetName( 'P4' )
P5_1.SetName( 'P5' )
try:
  Completed_Mesh.ExportMED( r'/home/jangeorg/TUBA/tutorial/001/new_case.mmed', 0, SMESH.MED_V2_2, 1, None ,1)
except:
  print 'ExportToMEDX() failed. Invalid file name?'


## Set names of Mesh objects
smesh.SetName(V1_2, 'V1')
smesh.SetName(P2_1, 'P2')
smesh.SetName(P3, 'P3')
smesh.SetName(Regular_1D_1.GetAlgorithm(), 'Regular_1D_1')
smesh.SetName(P1_1, 'P1')
smesh.SetName(QuadraticMesh, 'QuadraticMesh')
smesh.SetName(NumberOfSegments_8_0_1, 'NumberOfSegments=8,[],0:1:1:21')
smesh.SetName(P2, 'P2')
smesh.SetName(NumberOfSegments_8_0, 'NumberOfSegments=8,[],0:1:1:19')
smesh.SetName(NumberOfSegments_8_0_4, 'NumberOfSegments=8,[],0:1:1:27')
smesh.SetName(NumberOfSegments_8_0_2, 'NumberOfSegments=8,[],0:1:1:23')
smesh.SetName(NumberOfSegments_8_0_3, 'NumberOfSegments=8,[],0:1:1:25')
smesh.SetName(Completed_Mesh.GetMesh(), 'Completed_Mesh')
smesh.SetName(V0_1.GetMesh(), 'V0')
smesh.SetName(V2_1.GetMesh(), 'V2')
smesh.SetName(V1_1.GetMesh(), 'V1')
smesh.SetName(V4_1.GetMesh(), 'V4')
smesh.SetName(V_Bent3_1.GetMesh(), 'V_Bent3')
smesh.SetName(V4_2, 'V4')
smesh.SetName(P5, 'P5')
smesh.SetName(P4_1, 'P4')
smesh.SetName(V2_2, 'V2')
smesh.SetName(P4, 'P4')
smesh.SetName(P3_1, 'P3')
smesh.SetName(V1_3, 'V1')
smesh.SetName(V2_3, 'V2')
smesh.SetName(V0_3, 'V0')
smesh.SetName(V_Bent3_3, 'V_Bent3')
smesh.SetName(V4_3, 'V4')
smesh.SetName(V0_2, 'V0')
smesh.SetName(P1, 'P1')
smesh.SetName(P0_1, 'P0')
smesh.SetName(P2_2, 'P2')
smesh.SetName(P0, 'P0')
smesh.SetName(P1_2, 'P1')
smesh.SetName(P3_3, 'P3')
smesh.SetName(V_Bent3_2, 'V_Bent3')
smesh.SetName(P3_2, 'P3')
smesh.SetName(P4_3, 'P4')
smesh.SetName(P4_2, 'P4')
smesh.SetName(P5_1, 'P5')

###
### ASTER component
###

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
new_casermed = MEDReader(FileName='/home/jangeorg/TUBA/tutorial/001/new_case.rmed')

# set active source
SetActiveSource(None)

# find source
mEDReader1 = FindSource('MEDReader1')

# set active source
SetActiveSource(mEDReader1)

# set active source
SetActiveSource(new_casermed)

# set active source
SetActiveSource(mEDReader1)

# set active source
SetActiveSource(new_casermed)

#### saving camera placements for all active views




if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser(1)

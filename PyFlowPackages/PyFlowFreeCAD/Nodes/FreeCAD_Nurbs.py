import numpy as np
import random
import functools
import time
import inspect

from FreeCAD import Vector
import FreeCAD
import FreeCADGui
import Part


from PyFlow import CreateRawPin
from PyFlow.Core import NodeBase
from PyFlow.Core.NodeBase import NodePinsSuggestionsHelper
from PyFlow.Core.Common import *
from PyFlow.Packages.PyFlowBase.Nodes import FLOW_CONTROL_COLOR

import nodeeditor.store as store
from nodeeditor.say import *

from PyFlow.Packages.PyFlowFreeCAD.Nodes.FreeCAD_Object import timer, FreeCadNodeBase




class FreeCAD_Tripod(FreeCadNodeBase):
	'''
	position on a surface or curve
	'''

	def __init__(self, name="LOD",**kvargs):

		super(FreeCAD_Tripod, self).__init__(name)
		self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
		self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

		self.createInputPin('name', 'StringPin','view3d')
		a=self.createInputPin('u', 'FloatPin',0)
		a.recomputeNode=True
		a=self.createInputPin('v', 'FloatPin',0)
		a.recomputeNode=True
		self.createInputPin('Shape', 'ShapePin')
		self.createOutputPin('position', 'VectorPin')
		self.createOutputPin('placement', 'PlacementPin' )
		self.createInputPin("display", 'BoolPin', True)
		self.createInputPin("directionNormale", 'BoolPin', False)
		self.createInputPin("curvatureMode", 'BoolPin', True)
		


	@staticmethod
	def description():
		return FreeCAD_Tripod.__doc__

	@staticmethod
	def category():
		return 'Document'

	@staticmethod
	def keywords():
		return ['Surface','position','Point','uv']





class FreeCAD_YYY(FreeCadNodeBase):
	'''
	position on a surface or curve
	'''

	def __init__(self, name="LOD",**kvargs):

		super(FreeCAD_YYY, self).__init__(name)
		self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
		self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')

		self.createInputPin('name', 'StringPin','view3d')
		a=self.createInputPin('u', 'FloatPin',0)
		a.recomputeNode=True
		a=self.createInputPin('v', 'FloatPin',0)
		a.recomputeNode=True
		self.createInputPin('Shape', 'ShapePin')
		self.createOutputPin('position', 'VectorPin')
		self.createOutputPin('placement', 'PlacementPin' )
		self.createInputPin("display", 'BoolPin', True)
		self.createInputPin("directionNormale", 'BoolPin', False)
		self.createInputPin("curvatureMode", 'BoolPin', True)
		


	@staticmethod
	def description():
		return FreeCAD_YYY.__doc__

	@staticmethod
	def category():
		return 'Document'

	@staticmethod
	def keywords():
		return ['Surface','position','Point','uv']


class FreeCAD_Bar(FreeCadNodeBase):
	'''
	dummy for tests
	'''

#	def __init__(self, name="Fusion"):
#		super(FreeCAD_Bar, self).__init__(name)


	def compute(self, *args, **kwargs):

		sayl()
		import nodeeditor.dev
		reload (nodeeditor.dev)
		nodeeditor.dev.run_bar_compute(self,*args, **kwargs)
		self.outExec.call()

	@staticmethod
	def description():
		return FreeCAD_Bar.__doc__

	@staticmethod
	def category():
		return 'Development'

	@staticmethod
	def keywords():
		return []


class FreeCAD_uIso(FreeCadNodeBase):
	'''
	uIso curve on a surface
	'''

	def __init__(self, name="Fusion"):
		super(self.__class__, self).__init__(name)
		self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
		self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
		self.createInputPin('Face', 'ShapePin')
		a=self.createInputPin('u', 'FloatPin',5)
		a.recomputeNode=True
		self.createInputPin("display", 'BoolPin', True)
		self.createOutputPin('Edge', 'ShapePin')


	@staticmethod
	def description():
		return FreeCAD_uIso.__doc__

	@staticmethod
	def category():
		return 'Development'

	@staticmethod
	def keywords():
		return []


import traceback
import inspect

class FreeCAD_vIso(FreeCadNodeBase):
	'''
	vIso curve on a surface
	'''

	def __init__(self, name="Fusion"):
		super(self.__class__, self).__init__(name)
		self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
		self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
		self.createInputPin('Face', 'ShapePin')
		a=self.createInputPin('v', 'FloatPin',5)
		a.recomputeNode=True
		self.createInputPin("display", 'BoolPin', True)
		self.createOutputPin('Edge', 'ShapePin')


	@staticmethod
	def description():
		return FreeCAD_vIso.__doc__

	@staticmethod
	def category():
		return 'Development'

	@staticmethod
	def keywords():
		return []


class FreeCAD_uvGrid(FreeCadNodeBase):
	'''
	uIso and vIso curves grid
	'''

	def __init__(self, name="Fusion"):
		super(self.__class__, self).__init__(name)
		self.inExec = self.createInputPin(DEFAULT_IN_EXEC_NAME, 'ExecPin', None, self.compute)
		self.outExec = self.createOutputPin(DEFAULT_OUT_EXEC_NAME, 'ExecPin')
		self.createInputPin('Face', 'ShapePin')
		a=self.createInputPin('uCount', 'IntPin',5)
		a.recomputeNode=True
		a=self.createInputPin('vCount', 'IntPin',5)
		a.recomputeNode=True
		self.createInputPin("display", 'BoolPin', True)
		self.createOutputPin('uEdges', 'ShapeListPin')
		self.createOutputPin('vEdges', 'ShapeListPin')


	@staticmethod
	def description():
		return FreeCAD_uvGrid.__doc__

	@staticmethod
	def category():
		return 'Development'

	@staticmethod
	def keywords():
		return []











def nodelist():
	return [
				FreeCAD_Bar,
				FreeCAD_Tripod,
				FreeCAD_YYY,
				FreeCAD_uIso, FreeCAD_vIso,
				FreeCAD_uvGrid
		]

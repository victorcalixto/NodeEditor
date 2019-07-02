# tools zum zugriff auf pyFlow

import os
os.environ["QT_PREFERRED_BINDING"] = os.pathsep.join([ "PyQt4"])
import Qt
print (Qt)
print (Qt.IsPyQt4)

from PyFlow.Core.Common import *
from nodeeditor.say import *


import FreeCAD


from PyFlow import(
	INITIALIZE,
	GET_PACKAGES
)

from PyFlow.Core import(
	GraphBase,
	PinBase,
	NodeBase,
	GraphManager
)


def deleteInstance():
	say ("delet instance")
	FreeCAD.PF.hide()
	#FreeCAD.PF.deleteLater() # geth nicht wegen logger
	del(FreeCAD.PF)



def getInstance():

	try:
		say("try FreeCAD.PF ...")
		return FreeCAD.PF
	except:
		say("fails, recreate FreeCAD.PF! ")
	try: INITIALIZE()
	except: pass

	from PyFlow.App import PyFlow
	instance = PyFlow.instance()

	t=instance.windowTitle()
	if not t.startswith("FreeCAD NodeEditor"):
		instance.setWindowTitle("FreeCAD NodeEditor v0.01 @ "+instance.windowTitle())

	FreeCAD.PF=instance


	from PyFlow import(
		INITIALIZE,
		GET_PACKAGES
	)

	from PyFlow.Core import(
		GraphBase,
		PinBase,
		NodeBase,
		GraphManager
	)

	return instance

from PyFlow import(
		INITIALIZE,
		GET_PACKAGES
	)




def getGraphManager():
	return getInstance().graphManager.get()


def createFunction(packageName,libName,functionName):
	packages = GET_PACKAGES()
	lib = packages[packageName].GetFunctionLibraries()[libName]
	defFoos = lib.getFunctions()
	fun = NodeBase.initializeFromFunction(defFoos[functionName])
	return fun


def createNode(packageName,nodeClass,nodeName):
	packages = GET_PACKAGES()
	classNodes = packages[packageName].GetNodeClasses()
	node = classNodes[nodeClass](nodeName)
	return node



def connect(nodeA,pinNameA,nodeB,pinNameB):
	return connectPins(nodeA[str(pinNameA)], nodeB[str(pinNameB)])

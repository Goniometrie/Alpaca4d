import System
import os
import Grasshopper


ghFilePath = ghenv.LocalScope.ghdoc.Path
ghFileName = ghenv.LocalScope.ghdoc.Name
folderNameLength = len(ghFilePath)-len(ghFileName)-2 #have to remove '.gh'
ghFolderPath = ghFilePath[0:folderNameLength]

outputPath = ghFolderPath + 'assembleData'
wrapperFile = ghFolderPath + 'assembleData\\openSeesModel.txt'

#userObjectFolder = Grasshopper.Folders.DefaultUserObjectFolder
fileName = r'C:\GitHub\Alpaca4d\PythonScript\Analyses\EarthQuakeAnalysis\openSees_EarthQuakeAnalysis.py'


EarthQuakeAnalysis = System.Diagnostics.ProcessStartInfo(fileName)
EarthQuakeAnalysis.Arguments = wrapperFile + " " + str(GMdirection) + " " + str(GMfile) + " " + str(GMtimeStep) + " " + str(GMfact) + " " + str(Damping) + " " + str(NewmarkGamma) + " " + str(NewmarkBeta)
process = System.Diagnostics.Process.Start(EarthQuakeAnalysis)
System.Diagnostics.Process.WaitForExit(process)



print("I have fineshed")
## READ THE OUTPUT FROM THE OPEENSEES_SOLVER
## THE ORDER MUST BE THE SAME OF THE OUTPUT LIST IN OpenSeesStaticSolver.py


"""
outputFile = outputPath + '\\openSeesEarthQuakeAnalysisOutputWrapper.txt'

with open(outputFile, 'r') as f:
    lines = f.readlines()
    nodeModalDispWrapper = eval( lines[0].strip() )
    elementModalWrapper = eval( lines[1].strip() )
    period = eval( lines[2].strip() )
    frequency = eval( lines[3].strip() )



openSeesOutputWrapper = [nodeModalDispWrapper]
"""
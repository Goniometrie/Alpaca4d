import System
import os
import Grasshopper as gh

def InitializeGroundMotionAnalysis(AlpacaModel, TmaxAnalyses, GroundMotionDirection, GroundMotionValues, GroundMotionTimeStep, GroundMotionFactor, TimeStepIncrement, Damping, NewmarkGamma, NewmarkBeta):
    ghFilePath = ghenv.LocalScope.ghdoc.Path

    # delete file if already there
    workingDirectory = os.path.dirname(ghFilePath) 
    outputFileName = 'openSeesEarthQuakeAnalysisOutputWrapper.txt'

    for dirpath, dirnames, filenames in os.walk(workingDirectory):
        for filename in filenames:
            print(filename)
            if filename == outputFileName:
                file = os.path.join(dirpath,outputFileName)
                os.remove(file)


    ghFolderPath = os.path.dirname(ghFilePath)
    outputFolder = os.path.join(ghFolderPath,'assembleData')
    wrapperFile = os.path.join( outputFolder,'openSeesModel.txt' )

    #userObjectFolder = Grasshopper.Folders.DefaultUserObjectFolder
    fileName = r'C:\GitHub\Alpaca4d\PythonScript\Analyses\EarthQuakeAnalysis\openSees_EarthQuakeAnalysis.py'


    earthQuakeSettings = []

    for item in GroundMotionValues:
        earthQuakeSettings.append( "GROUNDMOTIONVALUES {}".format(item) )

    for item in GroundMotionTimeStep:
        earthQuakeSettings.append( "GROUNDMOTIONTIMESTEP {}".format(item) )

    earthQuakeSettings.append( "GROUNDMOTIONDIRECTION {}".format(GroundMotionDirection) )
    earthQuakeSettings.append( "GROUNDMOTIONFACTOR {}".format(GroundMotionFactor) )
    earthQuakeSettings.append( "DAMPING {}".format(Damping) )
    earthQuakeSettings.append( "NEWMARKGAMMA {}".format(NewmarkGamma) )
    earthQuakeSettings.append( "NEWMARKBETA {}".format(NewmarkBeta) )
    earthQuakeSettings.append( "TMAXANALYSES {}".format(TmaxAnalyses) )
    earthQuakeSettings.append( "TIMESTEP {}".format(TimeStepIncrement) )



    earthQuakeSettingsFile = os.path.join( outputFolder,'earthQuakeSettingsFile.txt')

    with open(earthQuakeSettingsFile, 'w') as f:
        for item in earthQuakeSettings:
            f.write("%s\n" % item)



    EarthQuakeAnalysis = System.Diagnostics.ProcessStartInfo(fileName)
    EarthQuakeAnalysis.Arguments = wrapperFile + " " + earthQuakeSettingsFile
    process = System.Diagnostics.Process.Start(EarthQuakeAnalysis)
    System.Diagnostics.Process.WaitForExit(process)


    print("I have finished")

    ## READ THE OUTPUT FROM THE OPEENSEES_SOLVER
    ## THE ORDER MUST BE THE SAME OF THE OUTPUT LIST IN OpenSeesStaticSolver.py


    outputFile = os.path.join(outputFolder, outputFileName)

    with open(outputFile, 'r') as f:
        lines = f.readlines()
        nodeDispFilePath = lines[0]
        elementModalWrapper = eval( lines[1].strip() )
        nodeWrapper = eval( lines[2].strip() )
        maxDisplacement = lines[3]
        minDisplacement = lines[4]


    AlpacaGroundmotionOutput = [nodeDispFilePath, elementModalWrapper, nodeWrapper]

    return [AlpacaGroundmotionOutput, maxDisplacement, minDisplacement]

checkData = True

if not AlpacaModel:
    checkData = False
    msg = "input 'AlpacaModel' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)

if TmaxAnalyses is None:
    checkData = False
    msg = "input 'TmaxAnalyses' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)

if GroundMotionDirection is None:
    checkData = False
    msg = "input 'GroundMotionDirection' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)


if not GroundMotionValues:
    checkData = False
    msg = "input 'GroundMotionValues' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)


if not GroundMotionTimeStep:
    checkData = False
    msg = "input 'GroundMotionTimeStep' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)


if GroundMotionFactor is None:
    checkData = False
    msg = "input 'GroundMotionFactor' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)


if TimeStepIncrement is None:
    checkData = False
    msg = "input 'TimeStepIncrement' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)


if Damping is None:
    checkData = False
    msg = "input 'Damping' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)

if NewmarkGamma is None:
    checkData = False
    msg = "input 'NewmarkGamma' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)

if NewmarkBeta is None:
    checkData = False
    msg = "input 'NewmarkBeta' failed to collect data"
    ghenv.Component.AddRuntimeMessage(gh.Kernel.GH_RuntimeMessageLevel.Warning, msg)


if checkData != False:
    AlpacaGroundmotionOutput, maxDisplacement, minDisplacement = InitializeGroundMotionAnalysis(AlpacaModel, TmaxAnalyses, GroundMotionDirection, GroundMotionValues, GroundMotionTimeStep, GroundMotionFactor, TimeStepIncrement, Damping, NewmarkGamma, NewmarkBeta)
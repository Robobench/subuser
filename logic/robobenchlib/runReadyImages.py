__author__ = 'jweisz'


import subuserlib.install
import subuserlib.runReadyImages
import os
import subuserlib.subuser
import subuserlib.paths
import robobenchlib.paths

def runReadyImageHostData(subuserToRun):
    """

    :param subuser: The subuserlib.subser to adapt to the current host
    :return: a new subuserlib.installedImage that has been modified for this host
    """
    #Add host_descriptor.json and the datacache to the image
    dockerfileContents = subuserlib.runReadyImages.generateImagePreparationDockerfile(subuserToRun)
    dockerfileContents += 'USER %s \n'%(str(os.getuid()))
    dockerfileContents += "ADD hostdata /subuser/hostdata \n"
    dockerfileContents += "RUN bash /subuser/hostdata/ \n"
    return dockerfileContents

def runReadyImageScripts(imageId):
    """

    :param imageId: The ID of which to add the client side scripts to.
    :return:
    """
    dockerfileContents =  "From " + imageId + " \n"
    dockerfileContents += "ADD robobench /subuser/dockerside-scripts"
    dockerfileContents += "USER root"
    dockerfileContents += "RUN bash /subuser/dockerside-scripts/install_client_gpu.bash"
    dockerfileContents += "USER %s \n"%(str(os.getuid()))

def buildRunReadyImageForSubuser(subuserToRun):
    imageId = subuserToRun.getUser().getDockerDaemon().build(robobenchlib.paths.getRobobenchHostDataCacheDir(),quietClient=True,useCache=True,forceRm=True,rm=True,dockerfile=runReadyImageHostData(subuserToRun))
    imageId = subuserToRun.getUser().getDockerDaemon().build(subuserlib.paths.getDockersideScriptsPath(),quietClient=True,useCache=True,forceRm=True,rm=True,dockerfile=runReadyImageScripts(subuserToRun))
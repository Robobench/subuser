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
    return dockerfileContents

def runReadyImageScripts(imageId):
    """

    :param imageId: The ID of which to add the client side scripts to.
    :return:
    """
    dockerfileContents =  "From " + imageId + " \n"
    dockerfileContents += "ADD ./robobench /subuser/ \n"
    dockerfileContents += "USER root \n"
    dockerfileContents += "RUN bash /subuser/install_client_gpu.bash \n"
    dockerfileContents += "USER %s \n"%(str(os.getuid()))
    return dockerfileContents

def markImageInstalled(imageId, subuserToRun):
    user = subuserToRun.getUser()
    imageSource = subuserToRun.getImageSource()
    lastUpdateTime = imageSource.getPermissions()["last-update-time"]
    if lastUpdateTime == None:
        lastUpdateTime = subuserlib.installTime.currentTimeString()

    user.getInstalledImages()[imageId] = subuserlib.classes.installedImage.InstalledImage(user,imageId,imageSource.getName(),imageSource.getRepository().getName(),lastUpdateTime)
    user.getInstalledImages().save()

def buildRunReadyImageForSubuser(subuserToRun):
    """

    :param subuserToRun: The subuser image to run
    :type: subuserToRun: subuserlib.subuser.Subuser
    :return:
    """
    repoName = "subuser-%s"%(subuserToRun.getName())
    imageId = subuserToRun.getUser().getDockerDaemon().build(os.path.dirname(robobenchlib.paths.getRobobenchHostDataCacheDir()),quietClient=True,useCache=True,forceRm=True,rm=True,dockerfile=runReadyImageHostData(subuserToRun))
    markImageInstalled(imageId, subuserToRun)
    imageId = subuserToRun.getUser().getDockerDaemon().build(subuserlib.paths.getDockersideScriptsPath(),quietClient=False,useCache=True,forceRm=True,rm=True,dockerfile=runReadyImageScripts(imageId),tag='%s:%s'%(repoName,'run-ready'))
    markImageInstalled(imageId, subuserToRun)
    return imageId

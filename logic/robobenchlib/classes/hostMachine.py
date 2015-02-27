
#external imports
import os, collections, json, sys
import robobenchlib.paths
import subuserlib.subprocessExtras
import subuserlib.classes.user
import subuserlib.classes.fileBackedObject, subuserlib.classes.userOwnedObject
import json, json_minify


class HostMachine(collections.OrderedDict, subuserlib.classes.fileBackedObject.FileBackedObject, subuserlib.classes.userOwnedObject.UserOwnedObject):
    def __init__(self, user, readpath, writepath):
        subuserlib.classes.userOwnedObject.UserOwnedObject.__init__(self,user)
        collections.OrderedDict.__init__(self)

        self.readPath = readpath
        self.writePath = writepath


    def describe(self):
        if self.has_key("description"):
            print( "Description: " +self["description"])
        if self.has_key("xorg"):
            print("Knows the host's XServer version")
            print( "xorg: " +self["xorg"])

        if self.has_key("nvidia"):
            print("Knows that host has an nvidia card and what it's driver version is")
            print( "nvidia: " +self["nvidia"])


    def save(self):
        """
        Save the hostMachine to the given file.
        """
        try:
            dir,_ = os.path.split(self.writePath)
            os.makedirs(dir)
            with open(self.writePath,'w') as fp:
               json.dump(self, fp, indent=1, separators=(',', ': '))
        except OSError:
            print("Failed to save hostMachine Descriptor")
            pass

    def load(self):
        """ Load the host machine from a given file

        """
        try:
            with open(self.readPath,'r') as fp:
                self.update(json.load(fp))
        except OSError:
            print"Failed to read hostMachine descriptor"



    def generateAndLoadFromScript(self):
        """
        Generates json file that describes the host system parameters that may be needed to configure the
        docker image. Then loads the script

        :returns True if file is created and loaded
        :returns False if creation fails.

        """

        scriptName = "get_host_descriptor.bash"
        outputDir = robobenchlib.paths.getRobobenchHostDataCacheDir()
        args = ["bash", scriptName, outputDir]

        # The output of this script is cached in the outputDir.
        scriptDir = robobenchlib.paths.getRobobenchInstallScriptDir()
        subuserlib.subprocessExtras.subprocessCallPlus(args, scriptDir)
        self.readPath = os.path.join(outputDir,'host_descriptor.json')
        self.load()



if __name__ == '__main__':
    # run tests
    import unittest
    class HostMachineTestCase(unittest.TestCase):
        def test_1(self):
            print("Test Load")
            h = HostMachine(subuserlib.classes.user.User(),"","")
            h.generateAndLoadFromScript()
            h.describe()

    unittest.main()
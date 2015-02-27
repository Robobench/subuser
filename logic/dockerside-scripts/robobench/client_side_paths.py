import os
"""
Module used for determining non-user-configurable paths on the created image    
"""


def getSubuserDir():    
    return os.path.join("/subuser") 

def getPermissionsDir():
    return getSubuserDir()
    
def getPermissionsDotJsonPath():
    return os.path.join(getPermissionsDir(), "permissions.json")

def getHostDescriptorDir():
    return getSubuserDir()

def getHostDescriptorDotJsonPath():
    return os.path.join(HostDescriptorDotDir(), "host_descriptor.json")

def getClientSideScriptsPath():
    return os.path.join(getSubuserDir(), "scripts")

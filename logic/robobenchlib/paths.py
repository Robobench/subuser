#!/usr/bin/env python

"""
Module for determining non-user-configurable paths
"""

import os
import subuserlib.paths
import subuserlib.classes.user

def getRobobenchLibDir():
    """ Get the top level directory of the robobenchlib module """
    return os.path.join(subuserlib.paths.getSubuserDir(), "logic","robobenchlib")

def getRobobenchInstallScriptDir():
    """ Get the directory of install scripts for the robobench module """
    return os.path.join(getRobobenchLibDir(), "installScripts")

def getRobobenchHostDataCacheDir():
    """ Get the directory that will store metadata and temporary files such as the nvidia driver used by the disk image """
    user = subuserlib.classes.user.User()
    return os.path.join(user.homeDir,".subuser","robobench","hostdata")

#!/usr/bin/env python
# This file is a driver that reads a configuration file for available demos and 
# optimizations. 

import sys,os,subprocess
import json

def printHelp():
    print("You can use one of the following commands:")
    print("  list - see the available demos and benchmarks in this app image")
    print("  enter -  drop into a shell after starting up the image" )
    print("  [benchark_name or demo_name] - run the named demo. Run the list command for more information. ")

def listApps(configDict):
    """

    :param configDict:
    :return:
    """
    print("---Avaialable Commands---")
    for command in configDict["command_options"]:
        print("-")



def getConfig():
    configFilename = "/subuser/command_options.json"
    if not os.path.exists(configFilename):
        return {}

    try:
        with open(configFilename, 'w') as fp:
            return json.load(fp)
    except:
        print("Failed to load config file. Does your rappman package specify one?")
        return {}


def main():
    # find the configuration
    configDict = getConfig()

    if not len(configDict) or len(sys.argv) < 2 or sys.argv[1] == "help" or sys.argv[1] == "--help" or sys.argv[1] == "-h":
        printHelp()
        exit()

if __name__=="__main__":
    main()
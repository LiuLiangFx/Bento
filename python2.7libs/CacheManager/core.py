# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
## Description
"""
Core program to exchange datas.
"""
#-------------------------------------------------------------------------------

import os, sys
sys.dont_write_bytecode = True
import hou

from . import define as Define
reload(Define)

#-------------------------------------------------------------------------------
# Core API to access to Houdini Datas
#-------------------------------------------------------------------------------
class houManager(object):
    """Core API to access to Houdini Datas
    """
    def __init__(self):
        super(houManager, self).__init__()

    @classmethod
    def getCacheList(self):
        ## Init variable
        current_cache_nodes = []
        all_nodes = hou.pwd().allSubChildren()

        for node in all_nodes:

            for item in Define.CACHE_NODES:

                node_type = item.get("name")

                if node.type().name().lower() == node_type:

                    eachNode_dict     = {}
                    node_path         = node.path()
                    node_type         = node.type().name().lower()
                    cache_path        = self.unexpStrPath(node_path, node_type)
                    evalCachePath     = self.evalStrPath(node_path, node_type)

                    eachNode_dict["name"]           = node.name()
                    eachNode_dict["node_path"]      = node_path
                    eachNode_dict["cache_path"]     = cache_path
                    eachNode_dict["env"]            = self.analizeEnv(cache_path)
                    eachNode_dict["expanded_path"]  = evalCachePath
                    eachNode_dict["color"]          = node.color().rgb()
                    # eachNode_dict["editable"]       = self.isEditable(node_path)

                    current_cache_nodes.append(eachNode_dict)

        print current_cache_nodes
        for node in current_cache_nodes:
            print node.get("editable")

        return current_cache_nodes

    @classmethod
    def unexpStrPath(self, path, opType):
        for item in Define.CACHE_NODES:
            if item.get("name") == opType:
                parmName = item.get("parmName")

        parmPath = path + '/' + parmName
        unExpPath = hou.parm(parmPath).unexpandedString()

        return unExpPath

    @classmethod
    def evalStrPath(self, path, opType):
        for item in Define.CACHE_NODES:
            if item.get("name") == opType:
                parmName = item.get("parmName")

        parmPath = path + '/' + parmName
        evalPath = hou.evalParm(parmPath)

        return evalPath


    @classmethod
    def analizeEnv(self, path):
        try:
            pathTokens = path[0].split('/')
            if pathTokens[0] == None:
                return "-"
            else:
                return pathTokens[0]
        except:
            return None

    @classmethod
    def isEditable(self, path):
        pathTokens = path.split("/")

        # for path in range(len(pathTokens)):
        #

        return True



#-------------------------------------------------------------------------------
# OS file management class
#-------------------------------------------------------------------------------
class fileManager(object):
    """OS file management class
    """
    def __init__(self):
        super(fileManager, self).__init__()


    def copy(self, filepath, remove = False):
        pass


    def copyFile(self, filepath, remove = False):
        pass


    def copyDir(self, dir, remove = False):
        pass


    def fileCheck(self, filepath):
        pass



#-------------------------------------------------------------------------------
# Other useful methods
#-------------------------------------------------------------------------------

def makeListByDictKey(key, listOfDict, default = None):

    res = []
    for d in listOfDict:
        if d.has_key(key):
            res.append(d[key])
        else:
            res.append(default)
    return res


#-------------------------------------------------------------------------------
# EOF
#-------------------------------------------------------------------------------

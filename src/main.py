#    ___ _                                    _
#   / _ (_)_ __   _____      _____   ___   __| |
#  / /_)/ | '_ \ / _ \ \ /\ / / _ \ / _ \ / _` |
# / ___/| | | | |  __/\ V  V / (_) | (_) | (_| |
# \/    |_|_| |_|\___| \_/\_/ \___/ \___/ \__,_|
# Steven Rakhmanchik (C) 2022 Pinewood Programming Language
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

import sys
import os.path
import errorhandler as eh
import declare
import output
import g

def mainLoop(woodFile):
    for line in g.lines:
        line_lex = line.split(' ')
        if '->' in line:
            declare.declareNum(line)
        if line_lex[0] == 'out':
            line = line[3:len(line)]
            output.out(line)
        if '=>' in line:
            declar.declareNonNum(line)


#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
if (len(sys.argv)) != 2:
    eh.noFileArg()
else:
    woodFile = sys.argv[1]
    if woodFile[len(woodFile)-5:len(woodFile)] != ".wood":
        eh.noWoodFileArg()
    else:
        if os.path.exists(woodFile) == False:
            eh.noWoodFileExist()
        else:
            file = open(woodFile, "r")
            g.lines = [(line.rstrip('\n')) for line in file]
            file.close()

            g.vars = []
            g.varNames = []

            mainLoop(woodFile)

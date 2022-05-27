#    ___ _                               _
#   / _ \ |_   ___      _____   ___   __| |
#  / /_)/ | | | \ \ /\ / / _ \ / _ \ / _` |
# / ___/| | |_| |\ V  V / (_) | (_) | (_| |
# \/    |_|\__, | \_/\_/ \___/ \___/ \__,_|
#          |___/
# Steven Rakhmanchik (C) 2022 Plywood Programming Language
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
import g

def getLine(line):
    return(g.lines.index(line))
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WoodFile Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def noFileArg():
    print("Pinewood Error: noFileArg\nNo file was passed as an argument")
    quit(0)
def noWoodFileArg():
    print("Pinewood Error: noWoodFileArg\nNo \'.wood\' file was passed as an argument")
    quit(0)
def noWoodFileExist():
    print("Pinewood Error: noWoodFileExist\nGiven \'.wood\' file doesn't exist")
    quit(0)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Declaration Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def multiDeclare(loc):
    print("Pinewood Error: multiDeclare in line " + str(loc) + "\nMore than one declaration was made in a line")
    quit(0)
def invalidVarName(loc):
    print("Pinewood Error: invalidVarName in line " + str(loc) + "\nVariable name must be alphabetical")
    quit(0)
def varExistNotNumerical(loc):
    print("Pinewood Error: varExistNotNumerical in line " + str(loc) + "\nAttempted to set numerical to non-numerical")
    quit(0)
def varInWrongContext(loc):
    print("Pinewood Error: varInWrongContext in line " + str(loc) + "\nAttempted numerical operation with non-numerical variable")
    quit(0)
def varDoesntExist(loc):
    print("Pinewood Error: varDoesntExist in line " + str(loc) + "\nAttempted to use non-existant variable")
    quit(0)
def declarationNonNumerical(loc):   #this shouldn't really ever happen
    print("Pinewood Error: declarationNonNumerical in line " + str(loc) + "\nGot non-numerical result from numerical declaration")
    quit(0)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Label and Goto Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def invalidLblName(loc):
    print("Pinewood Error: invalidLblName in line " + str(loc) + "\nLbl name must be alphabetical")
    quit(0)
def invalidGotoDest(loc):
    print("Pinewood Error: invalidGotoDest in line " + str(loc) + "\nGoto destination must be alphabetical")
    quit(0)
def gotoWithNoDest(loc):
    print("Pinewood Error: gotoWithNoDest in line " + str(loc) + "\nGoto has no cooresponding label")
    quit(0)
def lblTooManyArgs(loc):
    print("Pinewood Error: lblTooManyArgs in line " + str(loc) + "\nLabel only takes one argument")
    quit(0)
def gotoTooManyArgs(loc):
    print("Pinewood Error: gotoTooManyArgs in line " + str(loc) + "\nGoto only takes one argument")
    quit(0)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Label and Goto Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

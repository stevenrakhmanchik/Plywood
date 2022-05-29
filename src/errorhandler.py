#    ___ _                               _
#   / _ \ |_   ___      _____   ___   __| |
#  / /_)/ | | | \ \ /\ / / _ \ / _ \ / _` |
# / ___/| | |_| |\ V  V / (_) | (_) | (_| |
# \/    |_|\__, | \_/\_/ \___/ \___/ \__,_|
#          |___/
# Steven Rakhmanchik (C) 2022 Plywood Programming Language
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
import g

def getLine(line):                  # DEPRECATED was used for getting line number by matching code
    return(g.lines.index(line))     # Doesn't work if two lines have the same code (will use the first)
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# WoodFile Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def noFileArg():
    print(g.RED+"Pinewood Error: "+g.CYAN+"noFileArg"+g.WHITE+"\nNo file was passed as an argument"+g.RESET)
    quit(0)
def noWoodFileArg():
    print(g.RED+"Pinewood Error: "+g.CYAN+"noWoodFileArg"+g.WHITE+"\nNo \'.wood\' file was passed as an argument")
    quit(0)
def noWoodFileExist():
    print(g.RED+"Pinewood Error: "+g.CYAN+"noWoodFileExist"+g.WHITE+"\nGiven \'.wood\' file doesn't exist")
    quit(0)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Declaration Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def multiDeclare(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"multiDeclare"+g.WHITE+" in line " + str(loc) + "\nMore than one declaration was made in a line")
    quit(0)
def invalidVarName(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"invalidVarName "+g.WHITE+"in line " + str(loc) + "\nVariable name must be alphabetical")
    quit(0)
def varExistNotNumerical(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"varExistNotNumerical "+g.WHITE+"in line " + str(loc) + "\nAttempted to set numerical to non-numerical")
    quit(0)
def varInWrongContext(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"varInWrongContext "+g.WHITE+"in line " + str(loc) + "\nAttempted numerical operation with non-numerical variable")
    quit(0)
def varDoesntExist(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"varDoesntExist "+g.WHITE+"in line " + str(loc) + "\nAttempted to use non-existant variable")
    quit(0)
def declarationNonNumerical(loc):   #this shouldn't really ever happen
    print(g.RED+"Pinewood Error: "+g.CYAN+"declarationNonNumerical "+g.WHITE+"in line " + str(loc) + "\nGot non-numerical result from numerical declaration")
    quit(0)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Label and Goto Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def invalidLblName(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"invalidLblName "+g.WHITE+"in line " + str(loc) + "\nLbl name must be alphabetical")
    quit(0)
def invalidGotoDest(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"invalidGotoDest "+g.WHITE+"in line " + str(loc) + "\nGoto destination must be alphabetical")
    quit(0)
def gotoWithNoDest(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"gotoWithNoDest "+g.WHITE+"in line " + str(loc) + "\nGoto has no cooresponding label")
    quit(0)
def lblTooManyArgs(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"lblTooManyArgs "+g.WHITE+"in line " + str(loc) + "\nLabel only takes one argument")
    quit(0)
def gotoTooManyArgs(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"gotoTooManyArgs "+g.WHITE+"in line " + str(loc) + "\nGoto only takes one argument")
    quit(0)
def lblMustBeAlone(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"lblMustBeAlone "+g.WHITE+"in line " + str(loc) + "\nLbl must be on its own line")
    quit(0)
def gotoMustBeAlone(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"gotoMustBeAlone "+g.WHITE+"in line " + str(loc) + "\nGoto must be on its own line")
    quit(0)

#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# If, Then, EndIf Errors:
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
def ifDoesntTakeArgs(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"ifDoesntTakeArgs "+g.WHITE+"in line " + str(loc) + "\nIf doesn't take any arguments")
    quit(0)
def ifStmtInBadPlace(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"ifStmtInBadPlace "+g.WHITE+"in line " + str(loc) + "\nIf statment cannot be between another if/then declaration")
    quit(0)
def thenDoesntTakeArgs(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"thenDoesntTakeArgs "+g.WHITE+"in line " + str(loc) + "\nThen doesn't take any arguments")
    quit(0)
def endifDoesntTakeArgs(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"endifDoesntTakeArgs "+g.WHITE+"in line " + str(loc) + "\nEndif doesn't take any arguments")
    quit(0)
def elseDoesntTakeArgs(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"elseDoesntTakeArgs "+g.WHITE+"in line " + str(loc) + "\nElse doesn't take any arguments")
    quit(0)
def endifWithNoIf(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"endifWithNoIf "+g.WHITE+"in line " + str(loc) + "\nEndif is only used at the end of an if clause")
    quit(0)
def ifCondInvalid(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"ifCondInvalid "+g.WHITE+"in line " + str(loc) + "\nInvalid condition in between if and then")
    quit(0)
def lineBreakInCond(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"lineBreakInCond "+g.WHITE+"in line " + str(loc) + "\nCannot have line breaks between conditions of an if")
    quit(0)
def ifMustBeAlone(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"ifMustBeAlone "+g.WHITE+"in line " + str(loc) + "\nIf must be on its own line")
    quit(0)
def thenMustBeAlone(loc):
    print(g.RED+"Pinewood Error: "+g.CYAN+"thenMustBeAlone "+g.WHITE+"in line " + str(loc) + "\nThen must be on its own line")
    quit(0)

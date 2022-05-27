import g
import errorhandler as eh

def lbl(line):
    #loc = eh.getLine("LBL" + line)
    loc = g.lineNumber + 1
    line = line.strip()
    g.lbls[line] = loc




def goto(line):
    #loc = eh.getLine("GOTO" + line)
    loc = g.lineNumber + 1
    line = line.strip()
    if not(line.isalpha()):
        eh.invalidGotoDest(loc)
    if not(line in list(g.lbls.keys())):
        eh.gotoWithNoDest(loc)
    g.lineNumber = int(g.lbls[line])
    return g.lineNumber

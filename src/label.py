import g
import errorhandler as eh

def lbl(line):
    loc = g.lineNumber + 1
    line = line.strip()
    g.lbls[line] = loc

def goto(line):
    loc = g.lineNumber + 1
    line = line.strip()
    if not(line.isalpha()):
        eh.invalidGotoDest(loc)
    if not(line in list(g.lbls.keys())):
        eh.gotoWithNoDest(loc)
    g.lineNumber = int(g.lbls[line])
    g.nestedIf = 0
    return g.lineNumber - 1

global lbls
global varValues
global varTypes
global varNames
global lines
global parser
global lineNumber
global nestedIf
global ifStmtsFlag
global do
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Global Variable Declarations
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
do = True
lines = []
varNames = []
varTypes = []
varValues = []
lbls = {}
lineNumber = 0
nestedIf = 0
ifStmtsFlag = False
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
# Constants (Mostly Colors and Stuff For Error Codes)
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
RED = "\u001b[31m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
RESET = "\u001b[0m"

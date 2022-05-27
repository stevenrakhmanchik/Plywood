from py_expression_eval import Parser
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
global lbls
global varValues
global varTypes
global varNames
global lines
global parser
global lineNumber
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
lines = []
varNames = []
varTypes = []
varValues = []
lbls = {}
parser = Parser()
lineNumber = 0

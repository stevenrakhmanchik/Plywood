#    ___ _                                    _
#   / _ (_)_ __   _____      _____   ___   __| |
#  / /_)/ | '_ \ / _ \ \ /\ / / _ \ / _ \ / _` |
# / ___/| | | | |  __/\ V  V / (_) | (_) | (_| |
# \/    |_|_| |_|\___| \_/\_/ \___/ \___/ \__,_|
# Steven Rakhmanchik (C) 2022 Pinewood Programming Language
#––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

def noFileArg():
    print("Pinewood Error: noFileArg\nNo file was passed as an argument")
    quit(0)
    return(0)
def noWoodFileArg():
    print("Pinewood Error: noWoodFileArg\nNo \'.wood\' file was passed as an argument")
    quit(0)
    return(0)
def noWoodFileExist():
    print("Pinewood Error: noWoodFileExist\nGiven \'.wood\' file doesn't exist")
    quit(0)
    return(0)

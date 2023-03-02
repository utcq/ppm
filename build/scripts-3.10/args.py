from sys import argv as args; del args[0]
from pmlib.utils.log import Log
from pmlib.utils.colors import Colors as fg
import pmlib.utils.settings as settings

def _NoArgs():
    Log.warnerror(settings.no_arg)
    Log.info(settings.help_sugg)

def Args() -> dict:
    #Args initialization and parsing
    if (len(args)==0): _NoArgs()
    cmds=list(filter(lambda arg: "--" not in arg, args))
    opts=list(filter(lambda arg: "--" in arg, args))
    return {
        "cmd": cmds,
        "opt": opts
    }

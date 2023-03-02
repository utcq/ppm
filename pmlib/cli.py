from pmlib.utils.args import Args
from pmlib.utils.log import Log
from pmlib.utils.colors import Colors as fg
import pmlib.utils.settings as settings
import pmlib.utils.configurator as conf
import inquirer
import os,sys

class Runner:
    def Help():
        print(settings.help_str)
    def Init():
        if os.path.isfile("project.json"): Log.warnerror("Project file already exists") ;return False
        cdir=os.getcwd().split("/")[-1]; name=Log.question(f"Project Name ({cdir})")
        if (name==""): name=cdir
        version=Log.question("Version (0.1.0)")
        if (version==""): version="0.1.0"
        questions = [inquirer.Checkbox('frameworks',message=f"{fg.BLUE}Frameworks{fg.RESET}",choices=settings.frameworks,carousel=True,),inquirer.List('entry',message=f"{fg.YELLOW}Add deafult run command to main.py?{fg.RESET}",choices=['Yes', 'No'],),]
        answers = inquirer.prompt(questions); frameworks=answers['frameworks']; entry=answers['entry']
        conf.Initialize(name,version,frameworks,entry)
    def List():
        root,deps=conf.treeRetriever()
        Log.pkgtree(root,deps)
class ArgManager:
    def loader(argument:str)->None:
        match (argument):
            case "help": Runner.Help()
            case "init": Runner.Init()
            case "ls"  : Runner.List()
            case _     : Log.warnerror(f"Unknown Command/Argument: '{argument}'")
def init():
    arg=Args()
    if(len(arg['cmd'])==0): return False
    match (arg['cmd'][0]):
        case "start": conf.command('start')
        case "test" : conf.command('test')
        case "run"  : conf.command(arg['cmd'][1])
        case "install":
            if (len(arg['cmd'])>1):
                pkgs=arg['cmd']
                del pkgs[0]
                conf.installpkg(pkgs)
            else:
                conf.installconf()
        case _:
            for cct in arg['cmd']:
                ArgManager.loader(cct)


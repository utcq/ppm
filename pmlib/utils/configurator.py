import json, os
import pmlib.utils.settings as settings
from pmlib.utils.log import Log
from pip._internal import main as pipmain
from pip._vendor import pkg_resources

def Initialize(name:str,version:str,frameworks:list,entry:str):
    myconf={
        "name":name,
        "version":version,
        "dependencies": [],
        "scripts": {}
    }
    for framework in frameworks:
        for dependency in settings.framework_deps[framework]:
            myconf["dependencies"].append(dependency)
    if (entry=="Yes"): myconf["scripts"]["start"]="python main.py"
    json.dump(myconf, open("project.json", "w"), indent=4)


def _install(package):
    pipmain(['install', package])

def command(cmd:str)->None:
    myconf=json.load(open("project.json", "r"))
    if cmd not in myconf["scripts"]: Log.warnerror(f"Missing '{cmd}' script from project.json"); return False
    os.system(myconf["scripts"][cmd])

def installpkg(pkgs:list[str])->None:
    myconf=json.load(open("project.json", "r"))
    for pkg in pkgs:
        if pkg not in myconf['dependencies']: myconf['dependencies'].append(pkg); json.dump(myconf, open("project.json", "w"), indent=4); _install(pkg)
        else: _install(pkg)

def installconf()->None:
    myconf=json.load(open("project.json", "r"))
    for pkg in myconf["dependencies"]:
        _install(pkg)

def treeRetriever()->list:
    myconf=json.load(open("project.json", "r"))
    root=myconf['name']+"@"+myconf["version"]+(" "*3)+os.getcwd()
    deps=myconf["dependencies"]
    dps={}
    for dep in deps:
        _package = pkg_resources.working_set.by_key[dep]
        reqs=_package.requires()
        dps[dep]=[]
        for req in reqs: dps[dep].append(str(req))
    return [root, dps]

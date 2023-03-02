from setuptools import setup
import glob
import os

scpt=[]
scpt+=glob.glob("tpmlib/*/*.py")
scpt+=glob.glob("tpmlib/*.py")
#scpt+=glob.glob("scripts/*/*.py")
#scpt+=glob.glob("scripts/*.py")
try: os.mkdir("pmlib")
except: pass
try: os.mkdir("pmlib/utils")
except: pass
for file in scpt:
    new=file.split("/")
    del new[0]
    efile='/'.join(new)
    code=open(file, 'r').read().replace("from ppm import", "from pmlib.ppm import").replace("import cli as ui", "import pmlib.cli as ui").replace("import utils.", "import pmlib.utils.").replace("from utils.", "from pmlib.utils.")
    open("pmlib/"+efile, "w").write(code)
sept=[]
sept+=glob.glob("pmlib/*/*.py")
sept+=glob.glob("pmlib/*.py")
setup(
      name='PPM',
      include_package_data=True,
      version='1.0',
      description='Python Project Manager',
      author='unitythecoder',
      author_email='',
      url='github.com/unitythecoder/ppm',
      packages=['pmlib', 'pmlib.utils'],
      include=['pmlib', 'pmlib.*', 'pmlib.utils.*', 'pmlib/utils'],
      data_files = sept,
      install_requires=['inquirer'],
      #scripts=sept,
      entry_points = {'console_scripts': [
        'ppm = pmlib:main',
    ],},
)


from fbs.cmdline import command
from os.path import dirname
from fbs.builtin_commands import freeze,clean
import fbs.cmdline
from shutil import copyfile

import os,sys
import MJOLNIR

@command
def customFreeze(debug=False):
    print('Cleaning up the previous mess...')
    clean()
    print('Freezing application with debug = {}'.format(debug))
    freeze(debug=debug)
    print('Generating needed folder for MJOLNIR normalizations')

    newFolder = os.path.join('target','MJOLNIRGui','MJOLNIR')
    if not os.path.isdir(newFolder):
        os.mkdir(newFolder)
    for f in [MJOLNIR.__flatConeNormalization__,MJOLNIR.__multiFLEXXNormalization__]:
        copyfile(f, os.path.join(newFolder,os.path.split(f)[1]))
    
    operatingSystem = sys.platform
    if operatingSystem == sys.platform == 'win32':
        location = os.path.join('target','MJOLNIRGui','MJOLNIRGui.exe')
    else:
        location = os.path.join('target','MJOLNIRGui','MJOLNIRGui')
    print("Done. You can now run `{}`. If that\ndoesn't work, see https://build-system.fman.io/troubleshooting.".format(location))



if __name__ == '__main__':
    project_dir = dirname(__file__)
    print(project_dir)
    fbs.cmdline.main(project_dir)
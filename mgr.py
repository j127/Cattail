import os
import sys
import argparse
import shutil
from subprocess import call, STDOUT

# Command line arguments
parser = argparse.ArgumentParser(
    prog='mgr',
    description='Makes a git repo with the default .gitignore.'
)
args = parser.parse_args()

# Locations
current_directory = os.getcwd()
script_location = os.path.abspath('{f}/../'.format(f=__file__))
data_dir = script_location + '/data/'

# Data
gitignore_default = '{data_dir}gitignore_default.txt'.format(data_dir=data_dir)
gitignore_target = '.gitignore'
initial_commit_message = 'Initial commit by Cattail.'
# TODO: pass the initial_commit_message into the `git init` command

def make_git_repo():
    """Makes a Git repo with the default .gitignore."""
    call(['git', 'init'])

    if os.path.isfile(gitignore_target):
        print('.gitignore file already exists here. The script did not overwrite it.')
    else:
        try:
            shutil.copyfile(gitignore_default, '{cur_dir}/{fname}'.format(cur_dir=current_directory, fname=gitignore_target))
            print('Copied .gitignore to current directory.')
        except:
            print('Something went wrong while copying the .gitignore file:', sys.exc_info()[0])
            print('Tried to copy from {src} to {dst}'.format(src=gitignore_default, dst=current_directory))
            raise
    return 'Done'

def main():
    """Checks if the script is being run from within an existing Git repo."""
    if call(['git', 'branch'], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        make_git_repo()
    else:
        print('This is already a Git repository. Exiting.')
        sys.exit()

if __name__ == '__main__':
    main()

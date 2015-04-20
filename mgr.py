import os
import sys
import argparse
from subprocess import call, STDOUT

parser = argparse.ArgumentParser(
    prog='mgr',
    description='Makes a git repo with the default .gitignore.'
)
args = parser.parse_args()

def make_git_repo():
    """Makes a Git repo with the default .gitignore."""
    return 'hi there'

def main():
    """Checks if the script is being run from within an existing Git repo."""
    if call(["git", "branch"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
        make_git_repo()
    else:
        print('This is already a Git repository. Exiting.')
        sys.exit()

if __name__ == '__main__':
    main()

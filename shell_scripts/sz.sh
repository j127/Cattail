#!/bin/sh

# JUST FOR REFERENCE WHILE CONVERTING TO PYTHON.

# Please note, this is a work in progress just in the early stages
# Don't use this script unless you understand exactly what it does!
# It doesn't check for existing files and could delete something important.

helpme () {
echo "Shelzilla: a toolbox for automating repetitive stuff in the terminal.";
echo "sz init - starts a git repo in the current directory with a .gitignore. Does the initial commit."
}

if [ $1 ]
then
    case "$1" in
        init)
            echo "Creating git repo"
            git init
            echo "Adding .gitignore"
            echo "*~\n*.sw[po]\n*.py[co]\n__pycache__\n" >> .gitignore
            echo "Adding .gitignore to repo. It contains:"
            cat .gitignore
            echo "==================="
            git add .gitignore
            echo "Committing to repo"
            git commit -m "Initial commit by Shellzilla"
            echo "Done"
            ;;
        commit)
            echo "This doesn't do anything yet."
            ;;
        *)
            helpme;
            ;;
    esac
else
    helpme
fi


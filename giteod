#!/bin/bash

#git status but summarized and more script friendly
if [[ $(git status --porcelain) ]]; then

#Message to user
        echo "Changes detected. Updating remote repo."
#Set git location
        read -r -p "Path to git repo? [Default= ~/mycode ]: " GIT_DIR ##Gets user input
        GIT_DIR=${GIT_DIR:-~/mycode} ##Set GET_DIR to ~/mycode IF null or not set already
        echo "$GIT_DIR selected"
#Add changed files
        git add "$GIT_DIR" > /dev/null
#Get commit message
        read -r -p "Input commit message: " MESSAGE
#Commit with message
        git commit -m "$MESSAGE" > /dev/null
#Update remote repo
        git push origin HEAD > /dev/null
#Show successful update
        git status
else
#Message to user
        echo "No changes detected. GET CODING!"
fi

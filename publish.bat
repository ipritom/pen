ECHO "HELLO WOLD"
ECHO OFF
SET /p commit_message=ENTER YOUR MESSAGE:

@REM Uploading the new article to git
git add .
git commit -m "%commit_message%
git push origin main

PAUSE 

@REM Updating the contents.json file
git add . 
git commit -m "update: contents info"
git push origin main

ECHO "Updated!"
PAUSE
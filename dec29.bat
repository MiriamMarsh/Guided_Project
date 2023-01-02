echo off
echo starting
@REM calling my python file below
python dec29.py %name% %teacher%
set name=%1
set teacher=%2
@REM adding text to a new file called file.txt
echo "Welcome to class! This is for taking notes" > file.txt
@REM opening the new file.txt that I just created
start file.txt
@REM adding text to a new file called file.docx
echo "Welcome to class! This is for taking notes" > file.docx
@REM opening the new file.docx that I just created
start file.docx
@REM opening slack on my computer
start C:\Users\Owner\AppData\Local\slack\slack.exe
echo is completed

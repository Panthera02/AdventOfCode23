git add .
set /p input= Type the message for the commit: 
git commit -m %input%
git push

pause
exit
@echo off
echo Fixing hosts file...
echo.

REM Create a temporary file without the tunesph.com entry
type C:\Windows\System32\drivers\etc\hosts | findstr /V "tunesph.com" > C:\Windows\System32\drivers\etc\hosts.tmp

REM Replace the original file with the temporary file
copy C:\Windows\System32\drivers\etc\hosts.tmp C:\Windows\System32\drivers\etc\hosts > nul

REM Clean up
del C:\Windows\System32\drivers\etc\hosts.tmp

echo Hosts file has been fixed.
echo.
echo New hosts file contents:
echo.
type C:\Windows\System32\drivers\etc\hosts
echo.
echo Please run this batch file as Administrator for it to work properly.
pause
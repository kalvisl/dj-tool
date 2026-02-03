@echo off
echo Pushing DJ BPM Analyzer to GitHub...
echo.

echo 1. Committing files...
git commit -m "Initial commit: DJ BPM Analyzer"

echo 2. Renaming branch...
git branch -M main

echo.
echo 3. NEXT STEPS:
echo    - Create repository at https://github.com/new
echo    - Name: dj-tool
echo    - Make it PUBLIC
echo    - Don't add README
echo.
echo 4. After creating repository, run:
echo    git remote add origin https://github.com/kalvisl/dj-tool.git
echo    git push -u origin main
echo.
pause
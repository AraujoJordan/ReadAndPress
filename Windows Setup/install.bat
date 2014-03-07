@echo off
echo.
echo  		Installation will begin
echo.
echo 	We will install 2 programs and copy
echo 		one folder in your system
echo.
echo.
pause
start Exes\python-2.7.6.amd64.msi
start Exes\pywin32-218.win-amd64-py2.7.exe
xcopy Lib\selenium C:\Python27\Lib /e
echo.
echo.
echo		 Installation complete!
echo.
pause

@echo off
setlocal EnableDelayedExpansion

:: Prompt for original name
set /p original_name=What is the initial name?

:: Prompt for new name
set /p new_name=What is the new name?

:: Check if new_name contains "-"
echo %new_name% | findstr "-" >nul
if %errorlevel% equ 0 (
    echo New project name should not contain any '-'. Replace '-' by '_'
    exit /b 1
)

:: Check if new_name is too short (< 4 characters)
if not defined new_name (
    echo New project name is empty
    exit /b 1
)
set name_len=0
for /l %%A in (12,-1,0) do (
    set /a "bit=(1<<%%A)"
    set /a "tmplen=!name_len!+bit"
    for %%B in (!tmplen!) do if "!new_name:~%%B,1!" NEQ "" set /a name_len+=bit
)
if !name_len! LSS 4 (
    echo New project name '%new_name%' is too short
    exit /b 1
)

echo Renaming everything
echo Changing from '%original_name%' to '%new_name%'

GOTO :MAIN

:: Function to replace text in file using PowerShell
:: %1 = file, %2 = old string, %3 = new string
:rename_in_file
powershell -Command "(Get-Content '%~1') -replace '%~2', '%~3' | Set-Content '%~1'"
exit /b

:: Function to iterate over files in a folder
:: %1 = folder, %2 = old string, %3 = new string
:rename_in_folder
for /R "%~1" %%F in (*.*) do (
    call :rename_in_file "%%F" %2 %3
)
exit /b

:MAIN
call :rename_in_folder "%original_name%" %original_name% %new_name%
call :rename_in_folder "tests" %original_name% %new_name%
if exist "%original_name%" (
 rename "%original_name%" "%new_name%"
)
call :rename_in_folder "conf" %original_name% %new_name%
call :rename_in_file "docs/conf.py" %original_name% %new_name%
call :rename_in_file "docs/index.rst" %original_name% %new_name%
call :rename_in_file "tox.ini" %original_name% %new_name%

endlocal
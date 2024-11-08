@echo off
setlocal

if "%~2"=="" (
    echo Error: Not enough arguments.
    echo Usage: %0 filepath username
    exit /b 1
)

ssh-keygen -t rsa -f %~1 -C %~2
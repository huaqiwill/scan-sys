@echo off
setlocal

REM 确认用户操作
echo This will delete all __pycache__ folders in the current directory and all subdirectories.
echo Are you sure? (Y/N)
set /p confirm=

if /i not "%confirm%"=="Y" (
    echo Operation canceled.
    exit /b
)

REM 删除存在的 __pycache__ 文件夹
for /d /r %%i in (*) do (
    if exist "%%i\__pycache__" (
        echo Deleting %%i\__pycache__
        rd /s /q "%%i\__pycache__"
    )
)

echo All __pycache__ folders have been deleted.
endlocal
pause

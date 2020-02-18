rem Requires pyinstaller
pyinstaller hlsparser.py --onefile
rmdir /Q /s __pycache__
rmdir /Q /s build
del /Q hlsparser.spec
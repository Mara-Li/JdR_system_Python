@echo off
pyinstaller -y -w -F -i "data/logo.ico" --add-data "data/reset.png";"data" --add-data "data/log_file.png";"data" "JDR_System.py"
pyinstaller -y -w -i "data/logo.ico" --add-data "data/reset.png";"data" --add-data "data/log_file.png";"data" "JDR_System.py"
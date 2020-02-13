from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])
include_files = ['logo.ico']

base = None

if sys.platform == "win32":
    base = "Win32GUI"

target = Executable(
    script='CDI_dice.py',
    base=base,
    icon='logo.ico',)

setup(name='Aide',
      version = '1.4',
      description = 'Une aide pour les joueurs et MJ',
      options={'build_exe' : {'include_files' : include_files}},
      executables = [target]
      )
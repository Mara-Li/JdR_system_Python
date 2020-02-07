from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('CDI_dice.py', base=base, targetName = 'Aide')
]

setup(name='Helper',
      version = '1.3',
      description = 'Une aide pour les joueurs et MJ',
      options = dict(build_exe = buildOptions),
      executables = executables)

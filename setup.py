from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [],)

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

target = Executable(
    script="CDI_dice.py",
    base=base,
    targetName='Helper'
    )

setup(name='Helper',
      version = '1.4',
      description = 'Une aide pour les joueurs et MJ',
      options = dict(build_exe = buildOptions),
      executables = [target]
      )
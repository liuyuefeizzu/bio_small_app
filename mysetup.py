# -*- coding: cp936 -*-
from distutils.core import setup
import py2exe
import sys
sys.argv.append("py2exe")

py2exe_options={
    "dll_excludes":["MSVCP90.dll"],
    "compressed":1,
    "optimize":2,
    "ascii":0,
    "bundle_files":1,

    }
setup(
    name="wxpython app",
    version="1.0",
    description="[程序描述]",
    windows=[{"script":"app.py",
              "icon_resources":[(1,"q7.ico")]
              }],
    zipfile=None,
    options={"py2exe":py2exe_options}

    )

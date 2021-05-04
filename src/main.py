# Copyright (c) Rusted Studio
# Licensed under APGL-3.0 license. Read LiCENSE.txt for more info
# Developers:
# CertifiedRice - Lead Developer
# Rusted Studio - Development Studio
# Rusted Script Github Repository Contributors - Developers

import sys
import os
import rustedscript
from interpreter import run

command = sys.argv[1]
action=""
cnt=0
for argv in sys.argv:
    if cnt>=2:
        action=action+argv+" "
    cnt=cnt+1

if command is not None and action is not None:
    if command == "run":
        run(sys.argv[2])
    elif command == "install":
        print("We currently do not support this feature\n")
        print("The Rusted Script Package Manager is not yet ready to be depoloyed!")
        sys.exit(0)
    else:
        print("Usage: \n")
        print("    run <filename> <options> | options is not yet supported")
        print("    install <module> <options> | not supported yet")

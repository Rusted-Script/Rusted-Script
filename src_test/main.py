# Copyright (c) Rusted Studio
# Licensed under APGL-3.0 license. Read LiCENSE.txt for more info
# Developers:
# CertifiedRice - Lead Developer
# Rusted Studio - Development Studio
# Rusted Script Github Repository Contributors - Developers

import sys
import rustedscript

command = sys.argv[1]
action=""
cnt=0
for argv in sys.argv:
    if cnt>=2:
        action=action+argv+" "
    cnt=cnt+1

if command is not None and action is not None:
    if command == "run_line":
        result, error = rustedscript.run("<stdin>", action)
        if error:
            print(error.as_string())
            print("-----\n")
            print("     {} exited with a non-zero status code.".format('<file rusted>'))
            sys.exit(1)
        elif result: print(result)
    elif command == "install":
        print("We currently do not support this feature\n")
        print("The Rusted Script Package Manager is not yet ready to be depoloyed!")
        sys.exit(0)
    else:
        print("Usage: \n")
        print("    run_line <line> <options> | options is not yet supported")
        print("    install <module> <options> | not supported yet")

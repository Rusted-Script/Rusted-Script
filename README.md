[![Rusted Script](https://github.com/Rusted-Script/Rusted-Script/blob/master/icon.png)

# Rusted-Script
Rusted Script is an advanced programming language made by Rusted Studio. 


- [Discord](https://discord.gg/xKv9VKHSr5)
- [Website](https://rusted-script.github.io/)
- [Docs](https://github.com/Rusted-Script/Rusted-Script/tree/master/docs#docs)

## Versions:
| Release | Status | URL |
| -------- | ------ | ----  
| Version 0.0.1 | Outdated - Pre-Alpha - Stable| [here](https://github.com/Rusted-Script/Rusted-Script/releases/tag/0.0.1(Pre-Alpha)) |
| Version 0.0.2 | Pre-Alpha - Stable | [here](https://github.com/Rusted-Script/Rusted-Script/releases/tag/0.0.2) |
| Version 0.0.3 | Pre-Alpha - Unstable | [here](https://github.com/Rusted-Script/Rusted-Script/releases/tag/0.0.3) |
| Version 0.0.4 Pre-Release | Alpha - Unstable | ...|

## Setup

Setup development with **Rusted Script** on your computer.

### Shell Enviroment

If you want to play around and see what Rusted Script can do, run the shell like below;

Run [shell.py](https://github.com/Rusted-Script/Rusted-Script/blob/master/src/shell.py) with python3!

```sh
$ git clone https://github.com/Rusted-Script/Rusted-Script.git
$ cd Rusted-Script
$ cd src
$ python3 shell.py
```

### Rusted Script Interpreter

The current version of the interpreter may have bugs, as it is still in [Pre-Alpha (Version 0.0.3)](https://github.com/Rusted-Script/Rusted-Script/releases/tag/0.0.3)! If you come accross any bugs, dont hesitate to open a issue.

## Compiling via source
To compile and test the source code of Rusted Script, you need to download the repository and the languages.
Programming languages used to make Rusted Script:
- Python
- C



## Linux

We have native binaries for linux, so just run the `/Linux_Installer.sh` file, and it will install the binaries for you. After that, go to the `/binary/linux` folder, and run, `./rusted run home/file.rusted`. The `home/file.rusted` is a demo file, and you should replace it with the ***FULL PATH*** to your .rusted file.

## Windows

In windows, we currently dont have native binaries, so you would need to run the interpreter manually.

```sh
$ cd src # go to the src/ dir in Rusted-Script
$ python3 main.py run C:\Users\test\test.rusted # make sure to replace it with your rusted file path
```
## Example of Rusted Script code 
```js
# Rusted Script syntax
var x = 1 + 1 * 3 / 2 ^ 3 - 2
if x == 3 then 123 elif x == 0 then 321 else 12345
```

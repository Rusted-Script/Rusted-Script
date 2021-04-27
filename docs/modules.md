# Modules In Rusted Script

Modules are packages that are developed to help with certain tasks, and make advanced tasks easier to write with new functions in that module. This guide will show you how to use them.


# How to use a Module


## Install The Module

To install Rusted Script modules, you would need to put the module folder in the `rusted_modules` folder, and then with the name of the folder you can include it in your project. In the future Rusted Script will have a built in command, `rusted install`, and you can install modules simply like that. Since we are in early development stages, the only way to use a module is to put the folder in the `rusted_modules` folder.

## Include The Module

To Include the module in your rusted file, you can use the simple syntax like below,

```rusted
use_module("test_module")
```

This will include everythig from the `rusted_script/test_module/index.rusted` file.


# How to develop a Module


## Setup the basic structure

Your module needs a main folder, with the module name, so if the folder name is `test_1`, then you can inculde it using `use_module("test_1")`. Then make a simple `index.rusted` file in your folder. This is needed, it will be where the `use_module()` function looks, you can include other files in the main `index.rusted` file to fit your needs.

## Put the folder in rusted_modules

This step is simple, just put your folder in the rusted_modules folder, and now you can use it in any of your files!



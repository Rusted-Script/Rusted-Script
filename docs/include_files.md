# Include Files

You can include other *.rusted* files in your Rusted Script. If you want to include a *module*, or one of your other *.rusted* files, you can use the `use()` function, it is a built in function in `Rusted Script`. It got introduced in [Version 0.0.2](https://github.com/Rusted-Script/Rusted-Script/releases/tag/0.0.2), and is only available in the interpreter, you cant use it in the shell *yet*.

## How to use it

The below is an example usage of the `use()` function. It includes the variable `i` from `secondary.rusted`, and outputs it.

`main.rusted`

```rusted
use("secondary.rusted")
i # since there is no print function yet, this will output the value of "i"
```

#

`secondary.rusted`

```rusted
var i = 15

```

## Explanation

We included `secondary.rusted` in our `main.rusted` file, and that gives us access to **all** of the variables, functions, and classes of the `secondary.rusted`. In our case, this included the variable `i` from the `secondary.rusted` file. We outputed it to the screen, and its done!

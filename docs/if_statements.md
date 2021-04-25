# If Statements

If statements allow you to check if a certain condition is met, for example, `if 1 == 1 then .......`. This statement would be true, since the number 1 is equal to number 1.

## Examples Of If Statements;

```rusted
var x = 30
if x == 1 * 30 /* if 30 equals 30 ... */ 
then /* do something (if 30 equals 30)*/ elif 0 * 30 then /* do somethin (if 0 is true)
```

Another Example Can Be;

```rusted
if 15 == 7 /* if 15 equals 7 */ 
then /* do something (if 15 equals 7)  else /* else do something (if 15 DOES NOT equal 7)
```

To check for equality, you must use == (two equal signs), not = (one equal sign). Thats because the "=" operator *assigns* a value to the variable.

## Scenarios where to use it

You need to *check* if a user agrees with the privacy policy;

```rusted
var agrees_with_privacy_policy = false
if agrees_with_privacy_policy == true
then /* User Agrees */ else /* User Does Not Agree */
```

You need to see if a user payed enough for a product;

```rusted
var amount_payed = 15
if amount_payed >= 15
then /* User Payed */ else /* User didnt pay */
```

Use scenarios of *if statements* are *endless*, these are just some examples.

## Links

- [Rusted Script Docs](https://github.com/Rusted-Script/Rusted-Script/tree/master/docs)

- [Rusted Script Examples](https://github.com/Rusted-Script/Rusted-Script/tree/master/examples)

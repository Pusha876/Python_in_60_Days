# error-handling, try-except

## Try-except 
can be used when you want to anticipate a specific kind of error. You can use it to display a friendly error message to the user instead of letting the program end abruptly showing the user an error message that they can hardly understand.

### The interpreter
will first try to execute the code indented under "try".

### If the code under "try"
has the error anticipated in the except-line the code indented under "except" will be executed.

### If you don't specify the error which you anticipate
then, if the code under "try" has ANY type of error the code indented under "except" will be executed.
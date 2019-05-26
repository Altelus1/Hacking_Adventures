# stack-zero

let's start looking at the source code:

![](Insert image 1)

We can see a struct is defined inside the main function.
The BANNER is printed.
locals.changeme has been set to 0 then a gets() is called saving the
user input to locals.buffer.

# GOAL:
In order to win, we have to change the value of locals.changeme

### Digging Deeper:

Let's look at the assembly of the main function in GDB

![](Insert image 2)





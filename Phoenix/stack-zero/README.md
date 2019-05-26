# stack-zero

let's start looking at the source code:

![](https://raw.githubusercontent.com/Altelus1/Hacking_Adventures/master/Phoenix/stack-zero/images/1.png)

We can see a struct is defined inside the main function.
The BANNER is printed.
locals.changeme has been set to 0 then a gets() is called saving the
user input to locals.buffer.

# GOAL:
In order to win, we have to change the value of locals.changeme

### Digging Deeper:

Let's look at the assembly of the main function in GDB

![](https://raw.githubusercontent.com/Altelus1/Hacking_Adventures/master/Phoenix/stack-zero/images/2.png)





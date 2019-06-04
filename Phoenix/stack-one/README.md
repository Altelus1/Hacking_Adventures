# stack-one

Hello Again!

This challenge is about AMD64 stack-one

Let's start looking at the source code:

![](https://raw.githubusercontent.com/Altelus1/Hacking_Adventures/master/Phoenix/stack-one/images/1.png)

It's basically the same as stack-zero. The only differences are:
- It's getting user input the command line. Specifically the 1st argument.
- The user input is now stored in the locals.buffer using strcpy() instead of gets()
- local.changeme has to have a specific value which is 0x496c5962

(stack-zero : https://github.com/Altelus1/Hacking_Adventures/tree/master/Phoenix/stack-zero)

Question:
If it's almost exact the same, does the exploit from stack-zero (with a little tweaking) would still work?

Let's see.

![](https://raw.githubusercontent.com/Altelus1/Hacking_Adventures/master/Phoenix/stack-one/images/2.png)



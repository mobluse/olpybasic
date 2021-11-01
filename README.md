# OLPyBASIC
Python with line numbers (Ordered List Python BASIC) is a new programming language with goto and gosub. Syntax may change.
There are numbers before each line and the code runs in order, but execution can jump using goto and gosub with return. 
For each numbered line it uses Python's exec() function. That means it's compatile with Python3 in each logical line.
OLPyBASIC has the advantage that you can have tutorials where you add lines to the program. It will also be easy to implement 
single stepping and continue after stop. Another advantage is that you can run spaghetti code in Python. This means that you 
can easily convert old BASIC programs to run in a modern programming language that lacks goto. This buys you time while you 
can try to figure out how to remove the gotos. Gosubs are easier to replace with functions.

To start:

    python3 -i olpybasic.py

Paste:

    _a('10 print("test 1")')
    _a('20 print("test 2")')
    _a('30 x=30')
    _a('40 print(x)')
    _a('50 _gosub=90')
    _a('60 x+=1')
    _a('70 if x<=40:_goto=40')
    _a('80 _stop')
    _a('90 print(11*x)')
    _a('99 _return')

Enter:

    _run()
    _l()
    _d(60)
    _l()
    _a('60 x+=2')
    _l()
    _run()
    _trace=1
    _run()
    _trace=0

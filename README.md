# OLPyBASIC
Python with line numbers (Ordered List Python BASIC (Beginners' All-purpose Symbolic Instruction Code)) is a new programming language 
with goto and gosub. Syntax and features will change without prior notice.

There are numbers before each line and the code runs in order, but execution can jump using goto and gosub with return. 
For each numbered line it uses Python's `exec()` function. That means it's compatible with Python3 and MicroPython in each logical line.
OLPyBASIC has the advantage that you can have tutorials where you add lines to the program. It will also be easy to implement 
single stepping and continue after stop. Another advantage is that you can run spaghetti code in Python. This means that you 
can easily convert old BASIC programs to run in a modern programming language that normally lacks goto. This buys you time while you 
try to figure out how to remove the gotos, or leave them in, if your customer accepts that. Gosubs are easier to replace with functions.

To start:

    python3 -i olpybasic.py # Next line is an alternative if you have MicroPython in Linux or Unix.
    ~/micropython/ports/unix/micropython -i olpybasic.py # Next line is for NumWorks calculator.
    from olpybasic import _a,_run,_l,_d,_tron,_troff # Trace doesn't work on NumWorks.

Paste:

    _a('10 print("OLPyBASIC")') # _a is short for add or append.
    _a('20 print("MicroPython")')
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
    _l() # list
    _d(60) # delete
    _l()
    _a('60 x+=2') # add
    _l()
    _tron() # trace on
    _run()
    _troff() # trace off
    _run()

Please create issues if you have bug reports, suggestions for e.g. code improvement (I'm a Python/MicroPython beginner), or feature requests. 
This should be very light weight, but also comfortable to use. 

Planned changes: I will probably change the assignment to `_goto` and `_gosub` to using them as keywords and there will probably be a `_label` 
keyword. C style `_for` loops might be implemented, by converting them to `if` with `goto`s like in Ratfor. I might skip the prefix `_` for OLPyBASIC 
functions and variables -- consider the words without prefix reserved!

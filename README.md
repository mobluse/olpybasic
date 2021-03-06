# OLPyBASIC
Python with line numbers (Ordered List Python BASIC (Beginners' All-purpose Symbolic Instruction Code)) is a new programming language 
with goto. Syntax and features will change without prior notice.

There are numbers before each line and the code runs in order, but execution can jump using goto or gosub with return. 
For each numbered line it uses Python's `exec()` function. That means it's compatible with Python3 or MicroPython in each logical line.
*OLPyBASIC* has the advantage that you can have tutorials where you add lines to the program. It will also be easy to implement 
single stepping and continue after stop. Another advantage is that you can run spaghetti code in Python. This means that you 
can easily convert old BASIC programs to run in a modern programming language that normally lacks goto. This buys you time while you 
try to figure out how to remove the gotos, or leave them in, if your customer accepts that. Labels are supported
using e.g. `lbl("ex")` and `goto("ex")`, see the examples folder.

To start:

    python3 -i olpybasic.py # Next line is an alternative if you have MicroPython in Linux or Unix.
    ~/micropython/ports/unix/micropython -i olpybasic.py # Next line is for NumWorks calculator.
    from olpybasic import *

Example input (no need to input comments after #):

    P('10 print("OLPyBASIC")') # P is short for put.
    run() # Run i.e. start program.
    P('20 print("uPython")') # If difficult to enter single quote, try P(input())
    run()
    P('30 x=30')
    P('40 print(x)')
    run()
    P('50 x+=1')
    P('60 if x<=40:goto(40)')
    run()
    PM() # PM is short for paste mode
    70 stop()
    90 print(11*x)
    99 ret()
    45 gosub(90) # Enter empty line to quit paste mode.

Enter:

    run()
    L() # L is short for list
    D(50) # D is short for delete
    L()
    P('50 x+=2')
    L()
    tron() # trace on
    run()
    troff() # trace off
    run()

Please create issues if you have bug reports, suggestions for e.g. code improvements (I'm a Python/MicroPython beginner), or feature requests. 
This should be very light weight, but also comfortable to use. 

Planned changes: `for` loops might be implemented, by converting them to `if` with `goto`s like in Ratfor.

Run OLPyBASIC online in browser:
https://my.numworks.com/python/mobluse/olpybasic  
https://my.numworks.com/python/mobluse/test_olpybas  
https://my.numworks.com/simulators/zzpnwo (Doesn't work now, but the [issue](https://github.com/numworks/epsilon/issues/1896) is reported.)

[New Reddit](https://www.reddit.com/r/numworks/comments/qlk3z6/olpybasic_python_with_line_numbers_ordered_list/?utm_source=share&utm_medium=web2x&context=3)  
[Old Reddit](https://old.reddit.com/r/numworks/comments/qlk3z6/olpybasic_python_with_line_numbers_ordered_list/?ref=share&ref_source=link)

The editor is inspired by [ZX Forth Editor Manual](https://worldofspectrum.org//pub/sinclair/games-info/s/SpectrumForth(EditorUserManual).pdf).

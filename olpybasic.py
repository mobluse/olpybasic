#!/usr/bin/python3 -i
# ^ Ordinary Python
#!/media/pi/Elements/micropython/ports/unix/micropython -i
# ^ For my locally compiled MicroPython
# from olpybasic import * # < NumWorks graphing calculator

# OLPyBASIC https://github.com/mobluse/olpybasic
from math import *
from random import *
_prog={}
_pad={}

def P(s):
  global _prog
  i=s.index(' ')
  _prog[int(s[:i])]=s[i+1:]

def PM():
  while True:
    s=input()
    if len(s)==0:
      break
    P(s)

def D(n):
  global _prog,_pad
  _pad.clear()
  _pad[n]=_prog[n]
  del _prog[n]

def clear():
  global _running,_stop,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,å,ä,ö,é,ü
  a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=å=ä=ö=é=ü=0
  _running=_stop=False

def new():
  global _prog,_pad
  if _prog!={}:
    _pad.clear()
    for i in _prog:
      _pad[i]=_prog[i]
    _prog.clear()
  _sort_prog()
  clear()

def R(n=-1):
  global _prog,_pad
  m=min(list(_pad))
  for i in _pad:
    if n==-1:
      _prog[i]=_pad[i]
    else:
      _prog[n+i-m]=_pad[i]

_trace=False
_lines=[]
_returns=[]
_goto=-1
_gosub=-1
_i=-1
_running=False
_stop=False

def _prtrace():
  global _trace,_i,_lines,_prog
  if _trace:
    print('#',_lines[_i],_prog[_lines[_i]])

def tron():
  global _trace
  _trace=True

def troff():
  global _trace
  _trace=False

def _sort_prog():
  global _lines,_prog
  del _lines[:]
  _lines.extend(list(_prog))
  _lines.sort()

def L(n=-1):
  global _lines, _prog
  _sort_prog()
  if n==-1:
    for i in range(len(_lines)):
      print(_lines[i],_prog[_lines[i]])
  else:
    i=_lines.index(n)
    print(_lines[i],_prog[_lines[i]])

def run():
  global _lines,_returns
  del _returns[:]
  _sort_prog()
  clear()
  goto(_lines[0])

def goto(n):
  global _i,_lines,_running,_goto
  if _running:
    _goto=n
  else:
    _sort_prog()
    _i=_lines.index(n)
    _i-=1
    cont()

def gosub(n):
  global _gosub
  _gosub=n

def ret():
  global _i
  _i=_returns.pop()

def stop():
  global _stop
  _stop=True

def cont():
  global _i,_lines,_prog,_goto,_gosub,_returns,_running,_stop
  _running=True
  _sort_prog()
  _i+=1
  while _i<len(_lines):
    _prtrace()
    if _stop:
      _stop=False
      break
    exec(_prog[_lines[_i]], globals())
    if _goto>-1 or _gosub>-1:
      if _goto>-1:
        _i=_lines.index(_goto)
        _goto=-1
      elif _gosub>-1:
        _returns.append(_i)
        _i=_lines.index(_gosub)
        _gosub=-1
    else:
      _i+=1
  _running=False

new()

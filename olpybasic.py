#!/usr/bin/python3 -i
# ^ Ordinary Python
#!/media/pi/Elements/micropython/ports/unix/micropython -i
# ^ For my locally compiled MicroPython
# from olpybasic import * # < NumWorks graphing calculator

# OLPyBASIC https://github.com/mobluse/olpybasic
#from math import *
#from random import *
_prog={}
_pad={}

def P(s):
  global _prog
  i=s.index(' ')
  _prog[int(s[:i])]=s[i+1:]

def PM():
  while True:
    s=input()
    if not s:
      break
    P(s)

def D(n):
  global _prog,_pad
  _pad.clear()
  _pad[n]=_prog[n]
  del _prog[n]

def clear():
  global a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
  a=b=c=d=e=f=g=h=i=j=k=l=m=n=o=p=q=r=s=t=u=v=w=x=y=z=0

def new():
  global _prog,_pad,_running
  if _prog:
    _pad.clear()
    for i in _prog:
      _pad[i]=_prog[i]
    _prog.clear()
  _sort_prog()
  clear()
  stop()

def R(n=-1):
  global _prog,_pad
  if n==-1:
    for i in _pad:
      _prog[i]=_pad[i]
  else:
    m=min(list(_pad))
    for i in _pad:
      _prog[n+i-m]=_pad[i]

_trace=False
_lines=[]
_labels={}
_returns=[]
_goto=-1
_gosub=-1
_i=-1
_running=False

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

def _buffer_labels():
  global _lines,_prog,_labels
  _labels.clear()
  for i in range(len(_lines)):
    if _prog[_lines[i]][:4]=='lbl(':
      _labels[_prog[_lines[i]][5:-2]]=_lines[i]

def _sort_prog():
  global _lines,_prog
  del _lines[:]
  _lines.extend(list(_prog))
  _lines.sort()
  _buffer_labels()

def L(n=-1):
  global _lines,_prog
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

def lbl(n):
  pass

def goto(n):
  global _i,_lines,_labels,_running,_goto
  if type(n)!=int:
    n=_labels[n]
  if _running:
    _goto=n
  else:
    _sort_prog()
    _i=_lines.index(n)
    cont()

def gosub(n):
  global _gosub
  if type(n)!=int:
    n=_labels[n]
  _gosub=n

def ret():
  global _i
  _i=_returns.pop()

def stop():
  global _running
  _running=False

def cont():
  global _i,_lines,_prog,_goto,_gosub,_returns,_running
  _running=True
  _sort_prog()
  while _i<len(_lines):
    _prtrace()
    if not _running:
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

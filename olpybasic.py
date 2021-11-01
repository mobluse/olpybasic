#!/usr/bin/python3 -i
_prog={}
def _a(s):
    global _prog
    p = s.index(' ')
    _prog[int(s[:p])]=s[p+1:]

def _d(n):
    global _prog
    del _prog[n]

_trace=0
_lines=[]
_returns=[]
_goto=-1
_gosub=-1
_i=-1
def _prtrace():
    global _trace, _i, _lines, _prog
    if _trace:
        print('# ', _lines[_i], _prog[_lines[_i]])

def _l():
    global _lines, _prog
    del _lines[:]
    _lines.extend(list(_prog))
    _lines.sort()
    for i in range( len(_lines)):
        print(_lines[i], _prog[_lines[i]])

def _run():
    global x, _i, _lines, _prog, _goto, _gosub, _returns
    _i = -1
    del _returns[:]
    _cont()

def _g(n):
    global x, _i, _lines, _prog, _goto, _gosub, _returns
    _i=_lines.index(n)
    _i-=1
    _cont()

def _cont():
    global x, _i, _lines, _prog, _goto, _gosub, _returns
    del _lines[:]
    _lines.extend(list(_prog))
    _lines.sort()
    _i+=1
    while _i < len(_lines):
        if _prog[_lines[_i]]=='_return':
            _prtrace()
            _i = _returns.pop()+1
        if _prog[_lines[_i]]=='_stop':
            _prtrace()
            break
        _prtrace()
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

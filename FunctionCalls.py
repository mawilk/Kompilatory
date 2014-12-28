
function_dict = {
    '+': lambda x: reduce(lambda a,b: a+b, x),
    '-': lambda x: reduce(lambda a,b: a-b, x),
    '*': lambda x: reduce(lambda a,b: a*b, x),
    '/': lambda x: reduce(lambda a,b: a/float(b), x),
    '%': lambda x: evaluate(x,"%"),
    '>': lambda x: evaluate(x,'>'),
    '<': lambda x: evaluate(x,'<'),
    '>=': lambda x: evaluate(x,'>='),
    '<=': lambda x: evaluate(x,'<='),
    '==': lambda x: evaluate(x,'=='),
    '!=': lambda x: evaluate(x,'!='),
    '<<': lambda x: evaluate(x,'<<'),
    '>>': lambda x: evaluate(x,'>>'),
    '&&': lambda x: evaluate(x,'and'),
    '/|/|': lambda x: evaluate(x,'or'),
    'print': lambda x: callPrint(x)
}

def callPrint(x):
    print x

def evaluate(x, operator):
    return eval(str(x[0])+operator+str(x[1]))

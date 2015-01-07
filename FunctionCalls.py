
function_dict = {
    '+': lambda x: evaluate(x,"+"),
    '-': lambda x: reduce(lambda a,b: a-b, x),
    '*': lambda x: evaluate(x,"*"),
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
}


def evaluate(x, operator):
    return eval(str(x[0])+operator+str(x[1]))

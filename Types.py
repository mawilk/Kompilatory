bin_op = ['\|\|','&&','<<','>>']
arith_op = ['*', '/', '+', '-']
comp_op = [ '<', '>', '==', '!=', '<=', '>=']

class Ttype(dict):

    def __missing__(self, key):
        self[key] = Ttype()
        return self[key]

ttype = Ttype()

for op in bin_op+arith_op:
    ttype[op]['int']['int'] = 'int'

for op in arith_op:
    ttype[op]['float']['float'] = 'float'

for op in comp_op:
    ttype[op]['int']['int'] = 'int'
    ttype[op]['float']['float'] = 'int'
    ttype[op]['string']['string'] = 'int'

ttype["*"]['int']['float'] = 'float'
ttype["*"]['float']['int'] = 'float'

ttype['=']['int']['int'] = 'int'
ttype['=']['float']['float'] = 'float'
ttype['=']['string']['string'] = 'string'
ttype['=']['int']['float'] = 'int'
ttype['=']['float']['int'] = 'float'

ttype['+']['string']['string'] = 'string'
ttype['*']['string']['int'] = 'string'
import sys
import ply.yacc as yacc
from Cparser import Cparser
from TypeChecker import TypeChecker
from Interpreter import Interpreter


if __name__ == '__main__':

    filename = ""

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "tests\\passed\\primes.in"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    Cparser = Cparser()
    parser = yacc.yacc(module=Cparser)
    text = file.read()
    tree = parser.parse(text, lexer=Cparser.scanner)
    # print(tree)
    typeChecker = TypeChecker()
    interpreter = Interpreter()

    errors, warnings = tree.accept(typeChecker)
    for warn in warnings:
        print warn

    if(errors == []):
        tree.accept2(interpreter)
    else:
        for er in errors:
            print er

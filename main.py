from pprint import pprint
from calculadora.suma import suma as s
from calculadora.resta import resta as r
from calculadora.multiplicacion import multiplicacion as m
from calculadora.division import division as d

def main() :
    pprint(s.suma(4,5))
    pprint(r.resta(8,5))
    pprint(m.multiplicacion(2,5))
    pprint(d.division(4,2))


if __name__=='__main__':
    main()

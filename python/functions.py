

def avg(first, *rest):
    return (first + sum(rest)) / (1+len(rest))


#print(avg(1, 2, 3, 4, 5, 1, 1))

def plus(a, b):
    return a+b


def mult(a, b):
    return a*b


def minus(a, b):
    return a-b


func_dict = {
    'plus': plus,
    'minus': minus,
    'mult': mult,
}

func_array = [plus, mult, minus]

for func in func_array:
    print(func(4, 5))

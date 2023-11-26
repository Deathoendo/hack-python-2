"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    i = 0
    resultado = []
    if len(result)> 1:
        for c in result:
            i += 1
            if i % 2 == 0:
                resultado.append('-')
            else:
                resultado.append(str(i))
    else:
        resultado = ["0"]
    return resultado
print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))
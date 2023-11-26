"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""


def fn_hack_7(result):
    i = 0
    resultado = []
    if len(result)> 1:
        for c in result:
            i += 1
            if i % 2 == 0:
                resultado.append(i)
            else:
                resultado.append(str(i))
    else:
        resultado = [0]
    return resultado
print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([]))
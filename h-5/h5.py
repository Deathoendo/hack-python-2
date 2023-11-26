"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(result):
    i=0
    resultado = ""
    aux =0

    if result[:3] == 'foo':
        for c in result:
            if i == 2:
                aux+=1
                resultado = resultado + "-" 
                i = -1
                if aux == 2:
                    resultado = resultado + c
                    i = 0
            else:
                resultado = resultado + c
            i += 1
    if result[:3] == 'bar' or result[:2] == 'qu' or result[:2] == 'eq':        
        for c in result:
            if i == 2:
                resultado = resultado + "-"
                i = -1
            else:
                resultado = resultado + c
            i += 1
    return resultado

print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))
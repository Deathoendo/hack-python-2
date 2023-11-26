"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    i=0
    resultado = ""
    for c in result:
        if i == 0:
            if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
                c = ""
            i = -1
        resultado = resultado + c
        i += 1

    return resultado

print(fn_hack_2("fooziman"))
print(fn_hack_2("barziman"))
print(fn_hack_2("qux"))
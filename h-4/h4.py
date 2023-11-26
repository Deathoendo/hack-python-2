"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(result):
    i=0
    resultado = ""
    for c in result:
        if i == 0:
            if c == 'f':
                c = ""
            if c == 'n':
                c = ""
            if c == 'b':
                c = ""       
            i = -1
        resultado = resultado + c
        i += 1

    return resultado

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))


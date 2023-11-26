"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(result):
    i = 1
    resultado = ""
    for c in result:
        if i == 2:
            if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
                c = c.upper()
            i = -1
        resultado = resultado + c
        i += 1

    return resultado

print(fn_hack_1("fooziman"))
print(fn_hack_1("qux"))
print(fn_hack_1("eq"))
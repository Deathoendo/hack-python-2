"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    i=0
    resultado = ""
    for c in result:
        if i == 0:
            if c == 'a':
                c = '@'    
            if c == 'i':
                c = '¡'
            if c =='o': 
                c = '0'
            if c == 'u': 
                c = 'v'
            if c == 'q':
                c = c.upper()
            if c == 'x':
                c = c.upper()
            if c == 'f':
                c = c.upper()
            if c == 'n':
                c = c.upper()
            if c == 'b':
                c = c.upper()        
            i = -1
        resultado = resultado + c
        i += 1

    return resultado

print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))
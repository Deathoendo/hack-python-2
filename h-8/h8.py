"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    i = len(result)
    resultado = []
    cadena = ""
    if i % 2 != 0:
        while i > 0:
            i-= 1
            cadena = result[i] + "-" + str(i + 1) 
            resultado.append(cadena)
    else:
      while i > 0:
            i-= 1
            cadena = str(i + 1) 
            resultado.append(cadena)          
    return resultado
print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b"]))
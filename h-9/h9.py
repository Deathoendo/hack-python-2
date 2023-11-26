"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""



def fn_hack_9(result):
    var = ""
    result.pop('bar')
    sd = list(result.keys())
    prueba = str(sd[0])
    jh=""
    jh = prueba
    prueba = str(prueba).capitalize()
    result[prueba] = result.pop(jh)

    for key, value in result.items():
            sd = list(result.keys())
            prueba = str(sd[0])
            if key == prueba:
                 prueba2 = str(value).capitalize() 
                 result[key] = prueba2      
            for v in value:
                if v== 'k':
                    v= ''
                else:
                    var = str(var) + v
    var = var.capitalize()
    result[prueba] = var 
    result = str(result)
    return result
print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
s="""
def C_to_F (Celsius):
    Farenheit=((9/5)*Celsius)+32
    return Farenheit
def F_to_C (Farenheit):
    Celsius= ((5/9)*(Farenheit-32))
    return Celsius
"""
with open("Util.py",'x+') as Module:
    Module.writelines(s)

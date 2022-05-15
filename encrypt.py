import numpy as np
import math

def Encrypt():
    print("Enkriptimi nga Plain ne Cipher Text")
    print("Ne rast se teksti nuk eshte i gjate mjaftueshem sa ta mbuloj celesi ateher mesazhit i shtohet nje Z")

  #Inputi shendrrohet ne upper-case
    mesazhi = input("Plain Text: ").upper()

    #Validimi nuk i merr parasysh hapesirat ose karakteret speciale per shkak se punon vetem ne baze te rendit alfabetik (A-Z)
    temp=""
    for x in mesazhi:
        try:
            if x!=" ":
                int(x)
        except:
            temp+=x
    mesazhi=temp

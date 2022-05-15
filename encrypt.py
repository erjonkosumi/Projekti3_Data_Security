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
 while True:
        #format e mundshme te vargut dmth matrica te rangut 2,3 dhe 4
        while True:
            key = input("4(2x2)/9(3x3)/16(4x4) : ").upper()
            if len(key)==4 or len(key)==9 or len(key)==16:
                break
            else:
                print("Gjatesia e celesit nuk pershtatet")

        
        oMatrix = int(math.sqrt(len(key)))
        if oMatrix==2:
            while len(mesazhi)%2!=0:
                mesazhi+="Z"
        elif oMatrix==3:
            while len(mesazhi)%3!=0:
                mesazhi+="Z"
        elif oMatrix==4:
            while len(mesazhi)%4!=0:
                mesazhi+="Z"
#formimi i vargjeve permes librarise numpy
        matrixmsg = np.zeros((len(mesazhi),1))
        matrixkey = np.zeros((oMatrix,oMatrix))
        matrixrez = list()

      #ndryshimi i celesit(shkronje) ne nje celes te matrices(numer)
        incre1 = 0
        for kolona in range(oMatrix):
            for rreshti in range(oMatrix):
                matrixkey[kolona][rreshti] = ord(key[incre1])-65
                incre1 += 1

        #matrixkey duhet te jete e kthyeshme (reversibile) ashtu qe cipher texti mund te dekriptohet

        #matrixkey eshte e kthyeshme ne rast se te gjitha elementet e saj jane te ndryshme nga 0
        #nese ky kusht nuk mbushet, programi ristartohet
        
        if np.linalg.det(matrixkey) != 0:
            break
        else:
            print("Matrica celes nuk eshte e kthyeshme (nuk ka element invers) keshtu mesazhi nuk mund te dekriptohet")


     #konvertimi i mesazhit(shkronje) te nje mesazh te matrices(numer)
    incre2 = 0
    for kolona in range(len(mesazhi)):
        matrixmsg[kolona][0] = ord(mesazhi[incre2])-65
        incre2 += 1

    #shumezimi i matricave permes numpy
    for x in range(0,len(mesazhi),oMatrix):
        rezultati = matrixkey.dot(matrixmsg[x:x+oMatrix])
        for y in rezultati:
            matrixrez.append(y%26)

    #return rezultatin numer ne rezultat shkronje
    print("Cipher Text : ",end="")
    for i in matrixrez:
        print(chr(int(i)+65),end="")
    print("")
    input("\nEnter...")


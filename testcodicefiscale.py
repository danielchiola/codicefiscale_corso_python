#SCRIVERE UNA FUNZIONE CHE STAMPI LA PRIMA PARTE DEL CODICE FISCALE FINO AL MESE

cognome = str(input('Inserisci cognome: '))
nome = str(input('Inserisci nome: '))
vocali = ('aeiouAEIOU')
mesi = ('abcdehlmprstABDCDEHLMPRST')
anno_nascita = int(input('Inserisci anno: '))
mese_nascita = int(input('Inserisci mese: '))
contatore = 0


#COGNOME / NOME
for consonanti in cognome: 
    if not(consonanti in vocali): 
        print(consonanti[0:3],end=" ")
 #IN CASO DI DUE CONSONANTI PRENDI LA PRIMA VOCALE

    
    

                  
for consonanti in nome : 
    if not(consonanti in vocali):
        print(consonanti[0]+ consonanti[2:4],end=" ")
    


 #IN CASO DI DUE CONSONANTI PRENDI LA PRIMA VOCALE

 
    
        
    
#ANNO DI NASCITA ✅

str(anno_nascita)[-2:]
print(str(anno_nascita)[-2:],end=" ") #end=" " stampa i valori sulla stessa riga

    
#MESE ✅
def calcolaMese(mese_nascita):
   if (mese_nascita == "1"):
    return 'A'
   elif(mese_nascita == '2'):
    return'B'
   if(mese_nascita == '3'):
       return 'C'
   if(mese_nascita == '4'):
        return 'D'
   if(mese_nascita == '5'):
        return 'E'
   if(mese_nascita == '6'):
       return 'H'
   if(mese_nascita == '7'):
       return 'L'
   if(mese_nascita == '8'):
       return 'M'
   if(mese_nascita == '9'):
       return 'P'
   if (mese_nascita == '10'):
       return 'R'
   if (mese_nascita == '11'):
       return 'S'
   if (mese_nascita == '12'):
       return 'T'
print(calcolaMese(str(mese_nascita)),end=" ")


print('X X X X X X X')

        
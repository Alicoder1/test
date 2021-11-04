alifbo={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,	'H':8, 'I':9,
	'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,
	'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,
	'Z':26,	'\'':27,'_':28,'.':29,',':30}
alifbo1={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H', 9:'I',10:
	'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',
	18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',
	26:'Z',27:'\'',28:'_',29:'.',30:','}
savol=int(input('shifrlash uchun 1 ni, defisirlash uchun 2 ni bosing: '))
kalit=input('kalitni kiriting: ')
def shifr():
    matn=input('matnni kiriting: ')
    matn1=''
    s=len(kalit)
    j=-1
    m=0
    while True:
        
        for i in kalit.upper():
            m+=1
            j+=1

            n=int(alifbo[matn[j].upper()])-1    
            if int(alifbo[i])+n>30:
                matn1+=alifbo1[alifbo[i]+n-30]
            else: matn1+=alifbo1[alifbo[i]+n]
            if m==len(matn):
                break
        if m==len(matn):
            break
    print(matn1)
def deshifr():
    matn2=input('Shifrlangan matnni kiriting: ') 
    matn1=''
    s=len(kalit)
    j=-1
    m=0
    while True:
        
        for i in kalit.upper():
            m+=1
            j+=1

            n=int(alifbo[matn2[j].upper()])-alifbo[i]+1 
            if n<1:
                matn1+=alifbo1[n+30]  
            else:            
                matn1+=alifbo1[n]
            if m==len(matn2):
                break
        if m==len(matn2):
            break
    print(matn1)
if savol==1:
    print(shifr())
else: print(deshifr())

    
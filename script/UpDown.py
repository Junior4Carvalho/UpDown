import os
from time import sleep
ask = int(input("Deseja usar números positivos[1] ou negativos[0] ? "))

if ask == 1:
    
    sleep(.5)
    os.system('cls')
    sleep(.5)
    print("preparando o ambiente..")
    sleep(1)
    os.system('cls')
    sleep(.5)
    print("Ambiente PRONTO!!!")
    sleep(.7)
    os.system('cls')
    sleep(.5)
    print("Você escolheu [números positivos]")
    sleep(.5)
    print("-*"*20) 
    sleep(.7)
    
    #POSITVO
    def calc1():
        
        n = int(input("type a number: "))
        d = n
        
        if n == 0:
            sleep(.7)
            print("N é igual a 0.")
    
        if d > 0:
            while d > 0:
                d-=1
                sleep(.7)
                print("descendo:", int(d))
            
            sleep(.5)    
            print("-*"*10)         
                
        if d == 0:
            while d != n:
                d+=1
                sleep(.7)
                print("subindo:", int(d))
                
        else:
            sleep(.7)
            print("N é menor que 0!\nLogo N é negativo. ")
        
           
    calc1()
    

else:
    
    sleep(.5)
    os.system('cls')
    sleep(.5)
    print("preparando o ambiente..")
    sleep(1)
    os.system('cls')
    sleep(.5)
    print("Ambiente PRONTO!!!")
    sleep(.7)
    os.system('cls')
    sleep(.5)
    print("Você escolheu [números negativos]")
    sleep(.5)
    print("-*"*20) 
    sleep(.7)
   
    #NEGATIVO
    def calc2():
        
        n = int(input("type a number: "))
        
        if n >= 0:
            sleep(.7)
            print("N é igual ou maior que 0.")
            exit()
        else:
            pass
        
        sleep(.7)
        w = int(input("deseja subir para que número? "))
        r = n
        
       
            
    
        if r < 0:
            while r < 0:
                r+=1
                
                if r == 0:
                    sleep(.7)
                    print("Alcançamos o:", int(r))

                else:
                    sleep(.7)
                    print("subindo:", int(r))
                
            sleep(.5)    
            print("-*"*10)  
            
        if r == 0:
            while r != w:
                r+=1
                sleep(.7)
                print(f"subindo para {w}:", int(r))
            sleep(.5)
            print("-*"*10)
            print(f"Alcançamos o: {w}")
            sleep(.5)
            print("-*"*10)
            
        else:
            sleep(.7)
            print("N é maior que 0!\nLogo N é positivo.")
    
    calc2()

#aqui implemento el metodo lock para que en la seccion critica no entre otro hilo

import threading 
  
bandera = 0
  
def incrementar(): 
    global bandera 
    bandera += 1
  

def subproceso_princpal(lock): 
    for _ in range(100000): 
        #espero a que termine, para que no pueda acceder otro hilo
        lock.acquire() 
        incrementar() 
        lock.release() 
  

def main(): 
    global bandera 
    
    bandera = 0
  
    #creamos lock para bloquear
    lock = threading.Lock() 
  
    #paso como argumento lock
    subproceso1 = threading.Thread(target=subproceso_princpal, args=(lock,)) 
    subproceso2 = threading.Thread(target=subproceso_princpal, args=(lock,)) 
  
    
    subproceso1.start() 
    subproceso2.start() 
  
    
    subproceso1.join() 
    subproceso2.join() 
  
if __name__ == "__main__": 
    for i in range(10): 
        main() 
        print("Iteracion {0}: valor = {1}".format(i+1,bandera)) 
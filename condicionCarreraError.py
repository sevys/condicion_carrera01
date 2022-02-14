import threading 
  
bandera = 0
  
def incrementar_valor(): 
    global bandera 
    bandera += 1

  
def thread_task(): 

    for _ in range(100000): 
        incrementar_valor() 

  
def main(): 
    global bandera 
    
    bandera = 0

    #creamos los subprocesos
    hilo1 = threading.Thread(target=thread_task) 
    hilo2 = threading.Thread(target=thread_task) 
    
    hilo1.start() 
    hilo2.start() 
    
    hilo1.join() 
    hilo2.join() 
  

if __name__ == "__main__": 
    for i in range(10): 
        main() 
        print("Iteracion {0}: valor = {1}".format(i+1,bandera)) 


# El valor final esperado de la variable bandera es 200000, 
# pero lo que obtenemos en 10 iteraciones de la función main 
# son algunos valores diferentes.

# Esto sucede debido al acceso concurrente de subprocesos
#  a la variable compartida x . 
#  Esta imprevisibilidad en el valor de x no es más que una condición
# de carrera .
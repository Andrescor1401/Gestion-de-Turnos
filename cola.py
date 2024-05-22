class Cola:
    def __init__(self) -> None:
        self.turnoPrioritario = []
        self.turnoBuenaGente = []
        self.turnoClienteNormal = []
        self.contadorBuenaGente = 0
        self.contadorClienteNormal = 0
        
        
    def asignarTurno(self):
        try:
            id = int(input("Ingrese su id: "))
            categoria = input("Ingrese su categoria \n"
                      "P:Prioritario\n"
                      "B:Buena gente\n"
                      "C:Cliente normal\n"
                      "")
            
            
            if categoria == "P":
                self.turnoPrioritario.append(id)
            elif categoria == "B":
                self.turnoBuenaGente.append(id)
            elif categoria == "C":
                self.turnoClienteNormal.append(id)    
            else:
                print("Categoria no valida. Por favor solo ingrese las letras según su categoria.")     
        except ValueError:
            print("Id invalida. Ingrese solo números enteros")
               
    def llamarTurno(self):
        if self.turnoPrioritario:  
            return self.turnoPrioritario.pop(0)
        elif self.turnoBuenaGente and self.turnoClienteNormal:    
            if self.contadorBuenaGente <3:
                self.contadorBuenaGente+=1
                if self.contadorBuenaGente ==3:
                   self.contadorBuenaGente = 0 
                return self.turnoBuenaGente.pop(0)
            elif self.contadorClienteNormal < 2:
                self.contadorClienteNormal+=1
                if self.contadorClienteNormal == 2:
                    self.contadorClienteNormal = 0
                return self.turnoClienteNormal.pop(0)
        if self.turnoBuenaGente:
            return self.turnoBuenaGente.pop(0)
        
        if self.turnoClienteNormal:
            return self.turnoClienteNormal.pop(0)  
        
        return ("No hay turnos asignados")  
        
            
    
    
    
    
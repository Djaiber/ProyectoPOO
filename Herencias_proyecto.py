print("""
------------------------------HERENCIA---------------------------------------
""")
K = 1000
inicio = 0
def menu():
    
    opcion = int(input("""¿Desea registrar sus ventas para obtener recompensas?   
    1) SI   
    2) NO
    """))
    
    if opcion == 1:
       cliente1.registrar()



class Cliente:
    def __init__(self,nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo 
    
    def registrar(self):
        self.nombre = input("Escriba su nombre")
        
        self.telefono = int(input("Escriba su telefono"))
        []
        self.correo = input(intiba su correo")
   
class Puntos(Cliente):

    def __init__(self, nombre, telefono, correo) -> None:
        super().__init__(nombre, telefono, correo)
        self.compra = inicio
        self.puntos = inicio

    def conversion_puntos(self):
        self.compra = float(input("¿Total de la compra? "))
        self.puntos = self.compra/K

    def mostrar_puntos(self):
        print("Sus puntos en total son ",self.puntos)

    def menu_puntos(self):
        print("""
        ----------------MENU PUNTOS---------------------


        """)
cliente1 = Puntos("XXX",0,"XXXX")

menu()

print("Gracias por tu compra vuelve pronto")






    
print("""
------------------------------HERENCIA---------------------------------------
""")

class Cliente:
    def __init__(self,nombre,telefono,correo) -> None:
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def registrar(self):
        self.nombre = input("Escriba su nombre")
        print("hola",self.nombre)
        self.telefono = int(input("Escriba su telefono"))
        print("hola",self.telefono)
        self.correo = input("Escriba su correo")
        print("hola",self.nombre)

cliente1 = Cliente("XXX",0,"XXXX")

cliente1.registrar()
    
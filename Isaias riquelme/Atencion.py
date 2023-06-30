class Atencion:
    c_atencion=''
    nombre=''
    fecha=0
    costo=0
    descripcion=''
    lista_atencion=[]


    def __init__(self):
        self.c_atencion='A-001'
        self.nombre='S/N'
        self.fecha= 12/10/2020
        self.descripcion='hoila carlita'
        self.costo=20000

    def setC_atencion(self,c_atencion):
        if c_atencion[0:1].isalpha() and c_atencion[1:2]=='-' and c_atencion[2:4].isdigit():
            self.c_atencion=c_atencion
            return True
        else:
            print("Codigo invalido Ej. A-001")

    def setNombre(self,nombre):
        if len(nombre)>=5:
            self.nombre=nombre
            return True
        else:
            print("Minimo 5 caracteres")

    def setCosto(self,costo):
        if costo>=20000:
            self.costo=costo
            return True
        else:
            print("Costo minimo es de $20000")

    def setDescripcion(self,descripcion):
        if len(descripcion):
            self.descripcion=descripcion
            return True
        else:
            print("Minimo descripcion esperada es de 5 caracteres")





    def agregarcita(self,a):
        self.lista_atencion.append(a)
        print("Agrego cita:")

    def lista_atencion(self):
        for item in self.lista_atencion:
            print(f"Cita:{item}")

    def buscarcita(self,c_atencion):
        for Atencion in self.lista_atencion:
            if Atencion.c_atencion==c_atencion:
                return Atencion
            return None



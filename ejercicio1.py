
import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def __str__(self):
        return "({} , {})".format(self.x,self.y)
    
    def cuadrante(self):
        if self.x== 0 and self.y==0:
            print("el punto ({}, {}) esta sobre el origen".format(self.x, self.y))
        elif self.x<0 and self.y>= 0:
            print("el punto ({}, {}) esta sobre el cuadrante 2".format(self.x, self.y))
        elif self.x>=0 and self.y>= 0:
            print("el punto ({}, {}) esta sobre el cuadrante 1".format(self.x, self.y))
        elif self.x>=0 and self.y<=0:
            print("el punto ({}, {}) esta sobre el cuadrante 4".format(self.x, self.y))
        elif self.x<=0 and self.y<=0:
            print("el punto ({}, {}) esta sobre el cuadrante 3".format(self.x, self.y))
    
    def vector(self, punto):
        x= punto.x-self.x
        y= punto.y-self.y

        print("el vector es ({},{})".format(x,y))
    
    def distancia(self, punto):
        x= punto.x-self.x
        y= punto.y-self.y
        x=x*x
        y=y*y
        suma= x+y
        raiz = math.sqrt(suma)
        print(f"la distancia de los 2 puntos es: {raiz}")

class Rectangulo:
    def __init__(self, punto_inicio=Punto(), punto_final=Punto()):
        self.punto1=punto_inicio
        self.punto2 = punto_final
    
    def base(self):
        base= abs(self.punto2.x-self.punto1.x)
        return base

    def altura(self):
        altura = abs(self.punto2.y-self.punto1.y)
        return altura

    def area(self):
        area= self.base() * self.altura()
        return area

punto1 =Punto()
print(punto1.cuadrante())
punto2= Punto(10,3)
print(punto2.cuadrante())
punto3= Punto(-2,-5)
print(punto3.cuadrante())
punto4= Punto(-2,4)
print(punto4.cuadrante())
punto5 = Punto(3,-4)
print(punto5.cuadrante())

punto2.vector(punto3)
punto2.distancia(punto3)
rectangulo1 =Rectangulo(punto2, punto3)
print(rectangulo1.base())
print(rectangulo1.altura())
print(rectangulo1.area())
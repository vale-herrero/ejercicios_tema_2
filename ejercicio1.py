
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
        

punto1 =Punto()
print(punto1.cuadrante())
punto2= Punto(10,3)
print(punto2.cuadrante())
punto3= Punto(0,5)
print(punto3.cuadrante())
punto4= Punto(-2,0)
print(punto4.cuadrante())
punto5 = Punto(3,-4)
print(punto5.cuadrante())

punto2.vector(punto3)
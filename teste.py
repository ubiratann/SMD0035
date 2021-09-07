from math import sqrt, acos, asin, degrees


class Vector:

    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def dotProduct(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def crossProduct(self, v):
        return Vector(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        )

    def getNorm(self):
        return sqrt(self.dotProduct(self))

    def normalize(self):
        norm = self.getNorm()
        return Vector(self.x / norm, self.y / norm, self.z / norm)

    def getAngleByDot(self, v):
        dot = self.dotProduct(v)
    # //Evitando erros de aproximação que podem interferir na hora de calcular o acos
        dot = max(-1, dot) if dot < 0 else min(1, dot)
        return degrees(acos(dot))

    def getAngleByCross(self, v):
        uxv = self.crossProduct(v)
        return degrees(asin(uxv.getNorm() / (self.getNorm() * v.getNorm())))

    def isNull(self):
        return self.x == 0 and self.y == 0 and self.z == 0


u = Vector(0, 50, 0)
v = Vector(0, -50, 500)

if(u.isNull() or v.isNull()):
    print('Vetor u ou vetor v são nulos')
else:
    u = u.normalize()
    v = v.normalize()
    print(
        f'dotProduct angle: {u.getAngleByDot(v)} crossProduct angle:  {u.getAngleByCross(v)}')

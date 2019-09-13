#!/usr/bin/env python3
import math as mat

#    <n-body.py Solve the n-body probelem using Newton>
#    Copyright (C) <year>  <Brian Antonio Oseguera Mendoza Baomassu@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>

class Particle:
    G= 6.674e-11
    def __init__(self, p, v, m):
        self.p = p
        self.v = v
        self.m = m
     
    def computeR(self,p1):
        r=math.sqrt( (p1[0]-self.p[0])**2 + (p1[1]-self.p[1])**2 + (p1[2]-self.p[2])**2)
    
    def computeU(self,p1):
        u=[0,0,0]
        i=0
        for a,b in zip(self.p,p1):
            u[i] = b - a
            i+=1
        return u
    
    
    def integrate(self,dt, p1, m1):
        
        r = self.computeR(p1)
        u = self.computeU(p1)
        Vx= (G*m1*dt/(r**3))*u[0]
        Vy= (G*m1*dt/(r**3))*u[1]
        Vz= (G*m1*dt/(r**3))*u[2]
        
        self.p = [self.p[0]+ (self.v[0]+Vx)*dt,self.p[1]+ (self.v[1]+Vz)*dt,self.p[2]+ (self.v[2]+Vz)*dt]
        
    def getPosition(self):
        return self.p
    
    def getKineticEnergy():
        k = (1/2)*self.m*(mat.sqrt( self.v[0]^2 + self.v[1]^2 + self.v[2]^2))
        return k


p0=[0.0,0.0,0.0]  #m
v0=[1.0,.0,1.0]  #m/s
m=1.0            #kg

p0=[10.0,0.0,0.0]  #m
v0=[1.0,.0,1.0]  #m/s
m=1e24           #kg

dt = 1.0
    
#particulas

A = Particle(p0,v0,m)
#B = Particle(p0,v0,m)
print(A.getPosition())

for t in range(60):
    A.integrate(dt,p1,m1)
    print(A.getPosition())



    

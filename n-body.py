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
    def __init__(self, p, v, m):
        self.p = p
        self.v = v
        self.m = m
        
    def integrate(self,dt):
        self.p = [self.p[0]+ self.v[0]*dt,self.p[1]+ self.v[1]*dt,self.p[2]+ self.v[2]*dt]
        
    def getPosition(self):
        return self.p
    
    def getKineticEnergy():
        k = (1/2)*self.m*(mat.sqrt( self.v[0]^2 + self.v[1]^2 + self.v[2]^2))
        return k


p0=[0.0,0.0,0.0]  #cm
v0=[1.0,1.0,1.0]  #cm/s
m=1.0            #g
dt = 1.0
    
#particulas

A = Particle(p0,v0,m)
#B = Particle(p0,v0,m)
print(A.getPosition())

for t in range(60):
    A.integrate(dt)
    print(A.getPosition())



    

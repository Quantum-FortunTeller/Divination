# -*- coding: utf-8 -*-
"""
Spyder Editor

Bagua 
"""

import sys
import pygame
import time

from pygame.locals import QUIT

# Our Four Main Class
import numpy as np
from qiskit import *
class ClassicalOperator:
        
        def __init__(self):
            self.shangGua = np.array([[-1],[-1],[-1]])
            self.shiaGua = np.array([[-1],[-1],[-1]])
        '''
        變卦
        '''
        def bianGua(self): #shangGua: 上卦 shiaGua:下卦
            assert self.shangGua[0,0] != -1
            print("[classical變卦]")
            shangGua = np.where((self.shangGua==0)|(self.shangGua==1), self.shangGua^1, self.shangGua)
            shiaGua = np.where((self.shiaGua==0)|(self.shiaGua==1), self.shiaGua^1, self.shiaGua)
            return(shangGua, shiaGua) 
        '''
        互卦
        '''
        def huGua(self):
            assert self.shangGua[0,0] != -1
            print("[classical互卦]")
            shangGua = np.array([ [self.shangGua[1,0]],
                                  [self.shangGua[2,0]],
                                  [self.shiaGua[0,0]]])
            shiaGua = np.array([ [self.shangGua[2,0]],
                                 [self.shiaGua[0,0]],
                                 [self.shiaGua[2,0]]])
            return(shangGua, shiaGua)
        '''
        綜卦
        '''
        def tzungGua(self):
            assert self.shangGua[0,0] != -1
            print("[classical綜卦]")
            shangGua = np.flip(self.shiaGua)
            shiaGua = np.flip(self.shangGua)
            return(shangGua, shiaGua)
        '''
        正卦
        '''
        def zhenGua(self):
            print("[classical正卦]")
            self.getGua("shangGua")
            self.getGua("shiaGua")
            return(self.shangGua, self.shiaGua)
        def getGua(self,mode="shangGua"): #Two mode: shanGua or shiaGua
            qr = QuantumRegister(3)
            cr = ClassicalRegister(3)
            circuit = QuantumCircuit(qr, cr)
            circuit.h(qr)
            circuit.measure(qr, cr)
            circuit.draw(output='mpl')
            backend = Aer.get_backend('qasm_simulator')
            job = execute(circuit, backend, shots=1)
            result = job.result().get_counts(circuit)
            for x,y in result.items():
                Gua = x
                #print(Gua)
            if(mode=="shangGua"):
                self.shangGua[0,0] = Gua[2]
                self.shangGua[1,0] = Gua[1]
                self.shangGua[2,0] = Gua[0]
                #print(self.shangGua)
            elif(mode=="shiaGua"):
                self.shiaGua[0,0] = Gua[2]
                self.shiaGua[1,0] = Gua[1]
                self.shiaGua[2,0] = Gua[0]
                #print(self.shiaGua)
            else:
                print("mode error")

class QuantumOperator:
        
        def __init__(self):
            self.shangGua = np.array([[-1],[-1],[-1]])
            self.shiaGua = np.array([[-1],[-1],[-1]])
            self.shangGua_zhen = np.array([[-1],[-1],[-1]])
            self.shiaGua_zhen = np.array([[-1],[-1],[-1]])
            self.crBuffer = []
        '''
        變卦
        '''
        def bianGua(self): #shangGua: 上卦 shiaGua:下卦
            print("[Quantum變卦]")
            circ = QuantumCircuit(6)
            for i in range(6):
                circ.h(i)
                circ.x(i)
        
            circ.measure_all()
    
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(circ, simulator, shots=1)
            result = job.result().get_counts(circ)
            self.__resultToGua(result)
            return(self.shangGua, self.shiaGua)
        '''
        互卦
        '''
        def huGua(self):
            print("[Quantum互卦]")
            qr = QuantumRegister(6)
            cr = ClassicalRegister(8) # cr[6]: for qr[0] cr[7]: for qr[5]
            circ = QuantumCircuit(qr, cr)
            for i in range(6):
                circ.h(i)
    
            circ.measure(qr[1], cr[0])
            circ.measure(qr[2], cr[1])
            circ.measure(qr[3], cr[2])
            circ.measure(qr[2], cr[3])
            circ.measure(qr[3], cr[4])
            circ.measure(qr[4], cr[5])

            circ.measure(qr[0], cr[6])
            circ.measure(qr[1], cr[7])
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(circ, simulator, shots=1)
            result = job.result().get_counts(circ)
            
            for x,y in result.items():
                Gua = x
            self.shangGua[0,0]=Gua[7]
            self.shangGua[1,0]=Gua[6]
            self.shangGua[2,0]=Gua[5]
            self.shiaGua[2,0]=Gua[4]
            self.shiaGua[1,0]=Gua[3]
            self.shiaGua[0,0]=Gua[2]

            self.crBuffer.append(Gua[1])# q[0]
            self.crBuffer.append(Gua[0])# q[6]

            return(self.shangGua, self.shiaGua)
        '''
        綜卦
        '''
        def tzungGua(self):
            print("[Quantum綜卦]")
            circ = QuantumCircuit(6)
            for i in range(6):
                circ.h(i)
            circ.swap(0,5)
            circ.swap(1,4)
            circ.swap(2,3)
       
            circ.measure_all()
    
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(circ, simulator, shots=1)
            result = job.result().get_counts(circ)
            self.__resultToGua(result)
            return(self.shangGua, self.shiaGua)
        '''
        正卦
        '''
        def zhenGua(self):
            print("[Quantum正卦]")
            circ = QuantumCircuit(6) # 6 qubits
            for i in range(6):
                circ.h(i)
            circ.measure_all()
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(circ, simulator, shots=1)
            result = job.result().get_counts(circ)
            self.__resultToGua(result)
            return(self.shangGua, self.shiaGua)
        def __resultToGua(self, result): #string to shanGua & shiaGua
            for x,y in result.items():
                Gua = x
            self.shangGua[0,0]=Gua[5]
            self.shangGua[1,0]=Gua[4]
            self.shangGua[2,0]=Gua[3]
            self.shiaGua[2,0]=Gua[2]
            self.shiaGua[1,0]=Gua[1]
            self.shiaGua[0,0]=Gua[0]
        def transZhenGua(self, mode="huGua"): # mode = "huGua" or "bianGua" or "tzungGua" 
            if(mode=="huGua"):
                self.shangGua_zhen[0,0] = self.crBuffer[0]
                self.shangGua_zhen[1,0] = self.shangGua[0,0]
                self.shangGua_zhen[2,0] = self.shangGua[1,0]

                self.shiaGua_zhen[0,0] = self.shiaGua[1,0]
                self.shiaGua_zhen[1,0] = self.shiaGua[2,0]
                self.shiaGua_zhen[2,0] = self.crBuffer[1]

                return(self.shangGua_zhen, self.shiaGua_zhen)
            elif(mode=="bianGua"):
                self.shangGua_zhen = np.where((self.shangGua==0)|(self.shangGua==1), self.shangGua^1, self.shangGua)
                self.shiaGua_zhen = np.where((self.shiaGua==0)|(self.shiaGua==1), self.shiaGua^1, self.shiaGua)
                return(self.shangGua_zhen, self.shiaGua_zhen)
            elif(mode=="tzungGua"):
                self.shangGua_zhen = np.flip(self.shiaGua)
                self.shiaGua_zhen = np.flip(self.shangGua)
                return(self.shangGua_zhen, self.shiaGua_zhen)
            else:
                return -1 #error
class QuantumOperatorU3:
    def U3(self):
        circ = QuantumCircuit(7)
        for i in range(6):
            circ.h(i)
            circ.cx(i,6)

        circ.measure_all()

        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        b = result.items()
        for x, y in b:
            number = x
        number = str(number)

        def B(binary): 
            decimal = 0 
            for digit in binary: 
                decimal = decimal*2 + int(digit) 
            return decimal

        C = B(number)
        a = 1-(C/64)
        
        import numpy as np
        pi = np.pi
        b = np.arccos(a)
        return b
        
    def __init__(self):
        self.shangGua = np.array([[-1],[-1],[-1]])
        self.shiaGua = np.array([[-1],[-1],[-1]])
        self.shangGua_zhen = np.array([[-1],[-1],[-1]])
        self.shiaGua_zhen = np.array([[-1],[-1],[-1]])
        self.crBuffer = []
    def zhenGua(self):
        print("[Quantum正卦]")
        circ = QuantumCircuit(6) # 6 qubits
        for i in range(6):
            circ.u3(self.U3(), 0, 0,[i])
        circ.measure_all()
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        self.__resultToGua(result)
        return(self.shangGua, self.shiaGua)
        '''
        變卦
        '''
    def bianGua(self): #shangGua: 上卦 shiaGua:下卦
        print("[Quantum變卦]")
        circ = QuantumCircuit(6)
        for i in range(6):
            circ.u3(self.U3(), 0, 0,[i])
            circ.x(i)
        
        circ.measure_all()
    
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        self.__resultToGua(result)
        return(self.shangGua, self.shiaGua)
        '''
        互卦
        '''
    def huGua(self):
        print("[Quantum互卦]")
        qr = QuantumRegister(6)
        cr = ClassicalRegister(8) # cr[6]: for qr[0] cr[7]: for qr[5]
        circ = QuantumCircuit(qr, cr)
        for i in range(6):
            circ.u3(self.U3(), 0, 0,[i])
    
        circ.measure(qr[1], cr[0])
        circ.measure(qr[2], cr[1])
        circ.measure(qr[3], cr[2])
        circ.measure(qr[2], cr[3])
        circ.measure(qr[3], cr[4])
        circ.measure(qr[4], cr[5])

        circ.measure(qr[0], cr[6])
        circ.measure(qr[1], cr[7])
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
            
        for x,y in result.items():
            Gua = x
        self.shangGua[0,0]=Gua[7]
        self.shangGua[1,0]=Gua[6]
        self.shangGua[2,0]=Gua[5]
        self.shiaGua[2,0]=Gua[4]
        self.shiaGua[1,0]=Gua[3]
        self.shiaGua[0,0]=Gua[2]

        self.crBuffer.append(Gua[1])# q[0]
        self.crBuffer.append(Gua[0])# q[6]

        return(self.shangGua, self.shiaGua)
        '''
        綜卦
        '''
    def tzungGua(self):
        print("[Quantum綜卦]")
        circ = QuantumCircuit(6)
        for i in range(6):
            circ.u3(self.U3(), 0, 0,[i])
        circ.swap(0,5)
        circ.swap(1,4)
        circ.swap(2,3)
       
        circ.measure_all()
    
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        self.__resultToGua(result)
        return(self.shangGua, self.shiaGua)
    def __resultToGua(self, result): #string to shanGua & shiaGua
            for x,y in result.items():
                Gua = x
            self.shangGua[0,0]=Gua[5]
            self.shangGua[1,0]=Gua[4]
            self.shangGua[2,0]=Gua[3]
            self.shiaGua[2,0]=Gua[2]
            self.shiaGua[1,0]=Gua[1]
            self.shiaGua[0,0]=Gua[0]
    def transZhenGua(self, mode="huGua"): # mode = "huGua" or "bianGua" or "tzungGua" 
            if(mode=="huGua"):
                self.shangGua_zhen[0,0] = self.crBuffer[0]
                self.shangGua_zhen[1,0] = self.shangGua[0,0]
                self.shangGua_zhen[2,0] = self.shangGua[1,0]

                self.shiaGua_zhen[0,0] = self.shiaGua[1,0]
                self.shiaGua_zhen[1,0] = self.shiaGua[2,0]
                self.shiaGua_zhen[2,0] = self.crBuffer[1]

                return(self.shangGua_zhen, self.shiaGua_zhen)
            elif(mode=="bianGua"):
                self.shangGua_zhen = np.where((self.shangGua==0)|(self.shangGua==1), self.shangGua^1, self.shangGua)
                self.shiaGua_zhen = np.where((self.shiaGua==0)|(self.shiaGua==1), self.shiaGua^1, self.shiaGua)
                return(self.shangGua_zhen, self.shiaGua_zhen)
            elif(mode=="tzungGua"):
                self.shangGua_zhen = np.flip(self.shiaGua)
                self.shiaGua_zhen = np.flip(self.shangGua)
                return(self.shangGua_zhen, self.shiaGua_zhen)
            else:
                return -1 #error
class ClassicalOperatorU3:
        
    def U3(self):
        circ = QuantumCircuit(7)
        for i in range(6):
            circ.h(i)
            circ.cx(i,6)

        circ.measure_all()

        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        b = result.items()
        for x, y in b:
            number = x
        number = str(number)

        def B(binary): 
            decimal = 0 
            for digit in binary: 
                decimal = decimal*2 + int(digit) 
            return decimal

        C = B(number)
        a = 1-(C/64)

    #circ1 = QuantumCircuit(6)
        import numpy as np
        pi = np.pi
        b = np.arccos(a)
        return b
        
    def __init__(self):
        self.shangGua = np.array([[-1],[-1],[-1]])
        self.shiaGua = np.array([[-1],[-1],[-1]])
    '''
    變卦
    '''
    def bianGua(self): #shangGua: 上卦 shiaGua:下卦
        assert self.shangGua[0,0] != -1
        print("[classical變卦]")
        shangGua = np.where((self.shangGua==0)|(self.shangGua==1), self.shangGua^1, self.shangGua)
        shiaGua = np.where((self.shiaGua==0)|(self.shiaGua==1), self.shiaGua^1, self.shiaGua)
        return(shangGua, shiaGua) 
    '''
    互卦
    '''
    def huGua(self):
        assert self.shangGua[0,0] != -1
        print("[classical互卦]")
        shangGua = np.array([ [self.shangGua[1,0]],
                              [self.shangGua[2,0]],
                              [self.shiaGua[0,0]]])
        shiaGua = np.array([ [self.shangGua[2,0]],
                             [self.shiaGua[0,0]],
                             [self.shiaGua[2,0]]])
        return(shangGua, shiaGua)
    '''
    綜卦
    '''
    def tzungGua(self):
        assert self.shangGua[0,0] != -1
        print("[classical綜卦]")
        shangGua = np.flip(self.shiaGua)
        shiaGua = np.flip(self.shangGua)
        return(shangGua, shiaGua)
    '''
    正卦
    '''
    def zhenGua(self):
        print("[classical正卦]")
        self.getGua("shangGua")
        self.getGua("shiaGua")
        return(self.shangGua, self.shiaGua)
    def getGua(self,mode="shangGua"): #Two mode: shanGua or shiaGua
        qr = QuantumRegister(3)
        cr = ClassicalRegister(3)
        circuit = QuantumCircuit(qr, cr)
        for i in range(3):
            circuit.u3(self.U3(), 0, 0,[i])
        circuit.measure(qr, cr)
        circuit.draw(output='mpl')
        backend = Aer.get_backend('qasm_simulator')
        job = execute(circuit, backend, shots=1)
        result = job.result().get_counts(circuit)
        for x,y in result.items():
            Gua = x
                #print(Gua)
        if(mode=="shangGua"):
            self.shangGua[0,0] = Gua[2]
            self.shangGua[1,0] = Gua[1]
            self.shangGua[2,0] = Gua[0]
                #print(self.shangGua)
        elif(mode=="shiaGua"):
            self.shiaGua[0,0] = Gua[2]
            self.shiaGua[1,0] = Gua[1]
            self.shiaGua[2,0] = Gua[0]
                #print(self.shiaGua)
        else:
            print("mode error")
# class End
clock = pygame.time.Clock()
fps = 60
size = [200, 200]

HEIGHT = 8
WIDTH = 8
MINES = 7

BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
WHITE = (255, 255, 255)

pygame.init()
size = width, height = 1024, 984
screen = pygame.display.set_mode(size)
window_surface = pygame.display.set_mode((1024,984))


OPEN_SANS = "./Bagua_asset/OpenSans-Regular.tff"
smallFont = pygame.font.Font(OPEN_SANS, 20)
mediumFont = pygame.font.Font(OPEN_SANS, 28)
largeFont = pygame.font.Font(OPEN_SANS, 40)
window_surface.fill((255, 255, 255))
bg = pygame.image.load("./Bagua_asset/64.bmp")

    #INSIDE OF THE GAME LOOP
screen.blit(bg, (0, 0))

# For chinese word
#Place after the OPEN_SANS path
OPEN_mj = "./Bagua_asset/msjh.ttf"
miniFont = pygame.font.Font(OPEN_mj, 12)
smallFont2 = pygame.font.Font(OPEN_mj, 20)

head_font = pygame.font.SysFont(None, 60)
button = pygame.Rect(100, 100, 50, 50)
instructions = True

color11 = [120, 130, 120]
color12 = [120, 130, 120]
color21 = [120, 130, 120]
color22 = [120, 130, 120]

color31 = [120, 130, 120]
color32 = [120, 130, 120]
color41 = [120, 130, 120]
color42 = [120, 130, 120]

flag1 = -1
flag2 = -1
flag3 = -1

results1 = [""]
results2 = [""]
results3 = [""]
results4 = [""]
results5 = [""]
results6 = [""]
# User define function
def get64txt():
    zdic = {}
    with open('64.txt', encoding = 'utf8') as zfile:
        for line in zfile:
            z = line.split(' ', 1)
            key = z[0]
            value = z[1].split('，',1)
            zdic[key] = value
    return zdic 
zdic = get64txt()
def explanGua(shangGua, shiaGua):
    key = str(shangGua[0,0])+str(shangGua[1,0])+str(shangGua[2,0])+str(shiaGua[0,0])+str(shiaGua[1,0])+str(shiaGua[2,0])
    #print(key)
    #print(type(key))
    #print(zdic.get(key))
    return(zdic.get(key))

# greenButton = button((0,255,0),150,225,250,100,'Click Me')
while True:
    bg = pygame.image.load("./Bagua_asset/64.bmp")
    screen.blit(bg, (0, 0))
 # Show game instructions
    if instructions:

        # Title
        title = largeFont.render("Quantum-Classic All-In-One Oracle Machine", True, BLACK)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Rules
        rules = [
            "In order to reveal prophecy",
            "Select a mode",
            "Then, press REVEAL to get the prophercy:)"
        ]
        for i, rule in enumerate(rules):
            line = smallFont.render(rule, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 110 + 30 * i)
            screen.blit(line, lineRect)
        # your result gua
        # Results
        
        for i, result1 in enumerate(results1):
            line = smallFont2.render(result1, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 500 + 30 * i)
            screen.blit(line, lineRect)               
        

        for i, result2 in enumerate(results2):
            line = smallFont2.render(result2, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 525 + 30 * i)
            screen.blit(line, lineRect)
        

        for i, result3 in enumerate(results3):
            line = miniFont.render(result3, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 550 + 30 * i)
            screen.blit(line, lineRect)
        

        for i, result4 in enumerate(results4):
            line = smallFont2.render(result4, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 600 + 30 * i)
            screen.blit(line, lineRect)               
        

        for i, result5 in enumerate(results5):
            line = smallFont2.render(result5, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 625 + 30 * i)
            screen.blit(line, lineRect)
        
        for i, result6 in enumerate(results6):
            line = miniFont.render(result6, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2), 650 + 30 * i)
            screen.blit(line, lineRect)
        
        #Options
        option11 =["Superposition(H)"]
        option12 =["Entanglement(U3)"]
        option21 =["Just Measure"]
        option22 =["Stay Quantum"]
        option31 =["Zhèng Gua"]
        option32 =["Zōng Gua"]
        option41 =["Bian Gua"]
        option42 =["Hu Gua"]
        for i, options11 in enumerate(option11):            #Hadamard
            line = smallFont.render(options11, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 5), 250 + 30 * i)
            screen.blit(line, lineRect)
        for i, options12 in enumerate(option12):            #U3 Gate
            line = smallFont.render(options12, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 5), 350 + 30 * i)
            screen.blit(line, lineRect)
        for i, options21 in enumerate(option21):            #Just Measure
            line = smallFont.render(options21, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2.5), 250 + 30 * i)
            screen.blit(line, lineRect)
        for i, options22 in enumerate(option22):            #Stay Quantum
            line = smallFont.render(options22, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 2.5), 350 + 30 * i)
            screen.blit(line, lineRect)
        for i, options31 in enumerate(option31):            #Zhèng Gua
            line = smallFont.render(options31, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 1.6), 250 + 30 * i)
            screen.blit(line, lineRect)
        for i, options32 in enumerate(option32):            #Zōng Gua
            line = smallFont.render(options32, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 1.6), 350 + 30 * i)
            screen.blit(line, lineRect)
        for i, options41 in enumerate(option41):            #Bian Gua
            line = smallFont.render(options41, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 1.2), 250 + 30 * i)
            screen.blit(line, lineRect)
        for i, options42 in enumerate(option42):            #Hu Gua
            line = smallFont.render(options42, True, BLACK)
            lineRect = line.get_rect()
            lineRect.center = ((width / 1.2), 350 + 30 * i)
            screen.blit(line, lineRect)

        

        # Play game button
        buttonRect = pygame.Rect((width / 4), (3 / 4) * height, width / 2, 60)
        buttonText = mediumFont.render("REVEAL", True, WHITE)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = buttonRect.center
        pygame.draw.rect(screen, BLACK, buttonRect)
        screen.blit(buttonText, buttonTextRect)

        # click, _, _ = pygame.mouse.get_pressed()
        # flag = 1
        # if click == 1:
        #     mouse = pygame.mouse.get_pos()
        #     if buttonRect.collidepoint(mouse):
        #         instructions = False
        #         print("Hello",flag)
        #         flag = flag +1
        #         time.sleep(0.3)
                
                    
    buttonRect11 = pygame.Rect((width / 8.9), 275, width / 6, 50)
    buttonRect12 = pygame.Rect((width / 8.9), 375, width / 6, 50)   
    buttonRect21 = pygame.Rect((width / 3.2), 275, width / 6, 50)   
    buttonRect22 = pygame.Rect((width / 3.2), 375, width / 6, 50)        
    buttonRect31 = pygame.Rect((width / 1.85), 275, width / 6, 50)
    buttonRect32 = pygame.Rect((width / 1.85), 375, width / 6, 50)   
    buttonRect41 = pygame.Rect((width / 1.32), 275, width / 6, 50)   
    buttonRect42 = pygame.Rect((width / 1.32), 375, width / 6, 50) 

    pygame.draw.rect(screen, color11, buttonRect11)  # draw button
    pygame.draw.rect(screen, color12, buttonRect12) 
    pygame.draw.rect(screen, color21, buttonRect21) 
    pygame.draw.rect(screen, color22, buttonRect22)
    pygame.draw.rect(screen, color31, buttonRect31)  # draw button
    pygame.draw.rect(screen, color32, buttonRect32) 
    pygame.draw.rect(screen, color41, buttonRect41) 
    pygame.draw.rect(screen, color42, buttonRect42) 
    
    pygame.display.flip()
    for event in pygame.event.get():
        #if event.type == pygame.MOUSEBUTTONDOWN
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MouseDown")
            mouse_pos = event.pos
            print("mouse pos: ",mouse_pos)
            if buttonRect11.collidepoint(mouse_pos):
                print("Hadamard")
                flag1 = 1
                color11 = [50, 60, 50]
                color12 = [120, 130, 120]
            if buttonRect21.collidepoint(mouse_pos):
                print("JustMeasure")
                flag2 = 1
                color21 = [50, 60, 50]
                color22 = [120, 130, 120]
            if buttonRect12.collidepoint(mouse_pos):
                print("U3")
                flag1 = 2
                color11 = [120, 130, 120]
                color12 = [50, 60, 50]
            if buttonRect22.collidepoint(mouse_pos):
                print("StayQuantum")
                flag2 = 2
                color21 = [120, 130, 120]
                color22 = [50, 60, 50]
            
            if buttonRect31.collidepoint(mouse_pos):
                print("Zheng Gua")
                flag3 = 1
                color31 = [50, 60, 50]
                color32 = [120, 130, 120]
                color41 = [120, 130, 120]
                color42 = [120, 130, 120]
            if buttonRect32.collidepoint(mouse_pos):
                print("Zōng Gua")
                flag3 = 4
                color31 = [120, 130, 120]
                color32 = [50, 60, 50]
                color41 = [120, 130, 120]
                color42 = [120, 130, 120]
            if buttonRect41.collidepoint(mouse_pos):
                print("Bian Gua")
                flag3 = 2
                color31 = [120, 130, 120]
                color32 = [120, 130, 120]
                color41 = [50, 60, 50]
                color42 = [120, 130, 120]
            if buttonRect42.collidepoint(mouse_pos):
                print("Hu Gua")
                flag3 = 3
                color31 = [120, 130, 120]
                color32 = [120, 130, 120]
                color41 = [120, 130, 120]
                color42 = [50, 60, 50]

            if buttonRect.collidepoint(mouse_pos):
                print("REVEAL")
                
                color11 = [120, 130, 120]
                color12 = [120, 130, 120]
                color21 = [120, 130, 120]
                color22 = [120, 130, 120]
                color31 = [120, 130, 120]
                color32 = [120, 130, 120]
                color41 = [120, 130, 120]
                color42 = [120, 130, 120]
                if(flag1==1 and flag2==1):
                    print(11)
                    print("flag3: ", flag3)
                elif(flag1==1 and flag2==2):
                    print(12)
                    print("flag3: ", flag3)
                elif(flag1==2 and flag2==1):
                    print(21)
                    print("flag3: ", flag3)
                elif(flag1==2 and flag2==2):
                    print(22)
                    print("flag3: ", flag3)
                if(flag1==1 and flag2==1):# H3 and Just Measure
                    COP = ClassicalOperator()
                    x = flag3
                    if(x==1): # 正卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        results4 = [""]
                        results5 = [""]
                        results6 = [""]
                    elif(x==2): # 變卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        Gua1, Gua2 = COP.bianGua()
                        ExplanGua = explanGua(Gua1, Gua2)
                        print("[Bian Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[變卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                    elif(x==3): #互卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        Gua1, Gua2 = COP.huGua()
                        ExplanGua = explanGua(Gua1, Gua2)
                        print("[Hu Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[互卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                    elif(x==4): # 綜卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        Gua1, Gua2 = COP.tzungGua()
                        ExplanGua = explanGua(Gua1, Gua2)
                        print("[Tzung Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[綜卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]
                    else:
                        pass
                elif(flag1==1 and flag2==2):
                    QOP = QuantumOperator()
                    x = flag3
                    if(x==1): # 正卦
                        print("[-----Prophecy-----]")
                        QOP.zhenGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
            
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        results4 = [""]
                        results5 = [""]
                        results6 = [""]
                    elif(x==2): # 變卦
                        print("[-----Prophecy-----]")
                        QOP.bianGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
                        print("[Bian Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[變卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                        QOP.transZhenGua("bianGua")
                        ExplanGua = explanGua(QOP.shangGua_zhen, QOP.shiaGua_zhen)
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                    elif(x==3): #互卦
                        print("[-----Prophecy-----]")
                        QOP.huGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
            
                        print("[Hu Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[互卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                        QOP.transZhenGua("huGua")
                        ExplanGua = explanGua(QOP.shangGua_zhen, QOP.shiaGua_zhen)
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]

                    elif(x==4): # 綜卦
                        print("[-----Prophecy-----]")
                        QOP.tzungGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
                        print("[Tzung Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[綜卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                        QOP.transZhenGua("tzungGua")
                        ExplanGua = explanGua(QOP.shangGua_zhen, QOP.shiaGua_zhen)
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]

                    else:
                        pass
                if(flag1==2 and flag2==1):# H3 and Just Measure
                    COP = ClassicalOperatorU3()
                    x = flag3
                    if(x==1): # 正卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        results4 = [""]
                        results5 = [""]
                        results6 = [""]
                    elif(x==2): # 變卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        Gua1, Gua2 = COP.bianGua()
                        ExplanGua = explanGua(Gua1, Gua2)
                        print("[Bian Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[變卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                    elif(x==3): #互卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        Gua1, Gua2 = COP.huGua()
                        ExplanGua = explanGua(Gua1, Gua2)
                        print("[Hu Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[互卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                    elif(x==4): # 綜卦
                        print("[-----Prophecy-----]")
                        COP.zhenGua()
                        ExplanGua = explanGua(COP.shangGua, COP.shiaGua)
        
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        Gua1, Gua2 = COP.tzungGua()
                        ExplanGua = explanGua(Gua1, Gua2)
                        print("[Tzung Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[綜卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]
                    else:
                        pass
                elif(flag1==2 and flag2==2):
                    QOP = QuantumOperatorU3()
                    x = flag3
                    if(x==1): # 正卦
                        print("[-----Prophecy-----]")
                        QOP.zhenGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
            
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                        results4 = [""]
                        results5 = [""]
                        results6 = [""]
                    elif(x==2): # 變卦
                        print("[-----Prophecy-----]")
                        QOP.bianGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
                        print("[Bian Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[變卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                        QOP.transZhenGua("bianGua")
                        ExplanGua = explanGua(QOP.shangGua_zhen, QOP.shiaGua_zhen)
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]
                    elif(x==3): #互卦
                        print("[-----Prophecy-----]")
                        QOP.huGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
            
                        print("[Hu Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[互卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                        QOP.transZhenGua("huGua")
                        ExplanGua = explanGua(QOP.shangGua_zhen, QOP.shiaGua_zhen)
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]

                    elif(x==4): # 綜卦
                        print("[-----Prophecy-----]")
                        QOP.tzungGua()
                        ExplanGua = explanGua(QOP.shangGua, QOP.shiaGua)
                        print("[Tzung Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results4 = ['[綜卦]']
                        results5 = [ExplanGua[0]]
                        results6 = [ExplanGua[1]]

                        QOP.transZhenGua("tzungGua")
                        ExplanGua = explanGua(QOP.shangGua_zhen, QOP.shiaGua_zhen)
                        print("[Zhen Gua]: ", ExplanGua[0])
                        print("Oracle: ", ExplanGua[1])
                        results1 = ['[正卦]']
                        results2 = [ExplanGua[0]]
                        results3 = [ExplanGua[1]]

                    else:
                        pass
                if(flag1!=-1 and flag2!=-1 and flag3!=-1):
                    flag1=-1
                    flag2=-1
                    flag3=-1
                
                    
#     clock.tick(fps)

 
#     break

# pygame.display.update()
print("here")
while True:
    pass
    
            
       
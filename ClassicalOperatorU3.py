#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from qiskit import *
class ClassicalOperator:
        
        def U3():
            from qiskit import *
            get_ipython().run_line_magic('matplotlib', 'inline')

            circ = QuantumCircuit(6)
            for i in range(5):
                circ.h(i)
                circ.cx(i,5)

            circ.measure_all()

            simulator = Aer.get_backend('qasm_simulator')
            job = execute(circ, simulator, shots=1)
            result = job.result().get_counts(circ)
            b = result.items()
        
            for x, y in b:
                number = x
                number = int(number)

        def decimalToBinary(n): 
            return bin(n).replace("0b","") 

        a = 1/int(decimalToBinary(number))

        circ1 = QuantumCircuit(6)
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
            shangGua = np.flip(self.shangGua)
            shiaGua = np.flip(self.shiaGua)
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
                circuit.u3(U3(), 0, 0,[i])
            circuit.measure(qr, cr)
            get_ipython().run_line_magic('matplotlib', 'inline')
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


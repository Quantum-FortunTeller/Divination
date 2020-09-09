#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class QuantumOperatorU3:
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
            circ.u3(U3(), 0, 0,[i])
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
            circ.u3(U3(), 0, 0,[i])
    
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
        print("[classical綜卦]")
        circ = QuantumCircuit(6)
        for i in range(6):
            circ.u3(U3(), 0, 0,[i])
        circ.swap(0,2)
        circ.swap(3,5)
       
        circ.measure_all()
    
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(circ, simulator, shots=1)
        result = job.result().get_counts(circ)
        self.__resultToGua(result)
        return(self.shangGua, self.shiaGua)


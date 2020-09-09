#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

def zhenGua():
    from qiskit import *
    get_ipython().run_line_magic('matplotlib', 'inline')
    circ = QuantumCircuit(6)
    for i in range(5):
        circ.u3(b, 0, 0,[i])
        circ.cx(i,5)
        
    circ.measure_all()
    
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circ, simulator, shots=1)
    result = job.result().get_counts(circ)
    return result

def bianGua():
    from qiskit import *
    get_ipython().run_line_magic('matplotlib', 'inline')
    circ = QuantumCircuit(6)
    for i in range(5):
        circ.u3(b, 0, 0,[i])
        circ.x(i)
        circ.cx(i,5)
        
    circ.measure_all()
    
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circ, simulator, shots=1)
    result = job.result().get_counts(circ)
    return result

def huGua():
    from qiskit import *
    get_ipython().run_line_magic('matplotlib', 'inline')
    qr = QuantumRegister(6)
    cr = ClassicalRegister(6)
    circ = QuantumCircuit(qr, cr)
    for i in range(5):
        circ.u3(b, 0, 0,[i])
        circ.cx(i,5)
    
    circ.measure(qr[1], cr[0])
    circ.measure(qr[2], cr[1])
    circ.measure(qr[3], cr[2])
    circ.measure(qr[2], cr[3])
    circ.measure(qr[3], cr[4])
    circ.measure(qr[4], cr[5])

    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circ, simulator, shots=1)
    result = job.result().get_counts(circ)
    return result

def tzunGhua():
    from qiskit import *
    get_ipython().run_line_magic('matplotlib', 'inline')
    circ = QuantumCircuit(6)
    for i in range(5):
        circ.u3(b, 0, 0,[i])
        circ.x(i)
        circ.cx(i,5)
    circ.swap(0,2)
    circ.swap(3,5)
       
    circ.measure_all()
    
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circ, simulator, shots=1)
    result = job.result().get_counts(circ)
    return result


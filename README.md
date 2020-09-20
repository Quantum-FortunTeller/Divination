# Quantum Bagua divination machine
> [Intro slide](https://drive.google.com/file/d/1ycKo9GAHGDbsEMPtwJm76HVLrKz8L5du/view?usp=sharing)
![image](https://github.com/Quantum-FortunTeller/Divination/blob/master/imgForReadMe/sampleImg.PNG)
## How to run this pygame?
First, you need to install <code>pygame</code> and <code>Qiskit</code> package.\
Let's start the game! \
run <code>python Gamev1.0.py</code>
## Feature
* Inspiration from ancient Chinese Divination
* Limited quantum random number generator (QRNG)
> ![image](https://github.com/Quantum-FortunTeller/Divination/blob/master/imgForReadMe/QRNG.png)
> Ref: Jacak, Janusz E., et al. "Quantum random number generators with entanglement for public randomness testing." Scientific Reports 10.1 (2020): 1-9.
* Operations
> Swap gate (綜卦) and Pauil – X (變卦)
## Major Opeations Associated to Qiskit
* Rotating Eight Trigrams 綜卦(SWAP Gate)
![image](https://github.com/Quantum-FortunTeller/Divination/blob/master/imgForReadMe/Zong.png)
* Inverse Eight Trigrams 變卦(Pauli-X Gate)
![image](https://github.com/Quantum-FortunTeller/Divination/blob/master/imgForReadMe/Bian.png)
* Partial Eight Trigrams 互卦(Permutation)
![image](https://github.com/Quantum-FortunTeller/Divination/blob/master/imgForReadMe/Hu.png)\
Regarding the double measurement of the partial eight trigrams problem, we are fully aware that it is indeed weird to perform measurement twice. However, we aim to **reflect the exact calculation of the original "Hù guà"**.
Therefore, in order to fully demonstrate the Hù guà calculation, we perform the measurement twice on the qubit 3 and qubit 4, although it does not alter the result.

## Implications of applying Qiskit on Bagua 
1. The successful implementation of Qiskit to ancient Chinese culture could promote the visibility of Qiskit and open educational channel to publics, welcoming more Qiskitters joining the community as developers with interdisciplinary background.
2. By utilizing the true randomness of quantum world, we proposed a pygame interface to prevent fraudulent mediums services.
3. The myth of the mechanism of ancient Chinese wisdom may be revealed through quantum computing, moreover, one may find connections and similarities on these two ideology that both serves to describe and to obtain better understanding of Nature.



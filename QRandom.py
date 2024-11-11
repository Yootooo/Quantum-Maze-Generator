import math
import pygame
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def random_int(initial, final):
    if final == initial:
        return final 
    m = int(math.log2(final - initial)) + 1
    qc = QuantumCircuit(m,m)
    i = 0
    while i < m :
        qc.h(i)
        i += 1
    qc.barrier()
    i = 0
    while i < m:
        qc.measure(i,i)
        i+=1
    simulator = AerSimulator()
    job = simulator.run(qc, shots = 1)
    result = job.result()
    measured_value = list(result.get_counts(qc).keys())[0]
    i = 0
    left = initial
    right = final - initial +1
    mid = left + (right - left)//2
    while i < len(measured_value) :
        if measured_value[i] == '1':
            left = mid
        else :
            right = mid 
        i+=1
        mid = left + (right - left)//2
    random_value = mid
    return  random_value

def random_letter_digit_puctuation():
    return chr(random_int(33,126))

def random_emoji():
    choice = random_int(0,1)
    if choice == 0:
        return chr(random_int(128512,128591))
    else:
        return chr(random_int(127744,128511))
    
def random_currency():
    choice = random_int(0,1)
    if choice == 0 :
        return chr(random_int(162,165))
    else:
        return chr(random_int(8352,8399))
def random_character():
    choice = random_int(0,2)
    match(choice):
        case 0: return random_letter_digit_puctuation()
        case 1: return random_currency()
        case 2: return random_emoji()

def random_password(length):
    password = ""
    i = 0
    while(i < length):
        password += random_character()
        i += 1
    return password

def random_choice(array):
    if(len(array)==0):
       return False
    return array[random_int(0,len(array) - 1)]


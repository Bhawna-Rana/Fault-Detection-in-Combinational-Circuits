# Fault-Detection-in-Combinational-Circuits
This is made for Google Girl Hackathon 2023
## How to run the code
Download the zip file from this repository. Run the code using any Python IDE, I have used PyCharm. The input files must be named circuit.txt and fault.txt. The format of the above files must be:
Circuit File:
net_e = A & B
net_f = C | D
net_g = ~ net_f
Z = net_g ^ net_e

Fault File:
FAULT_AT = net_f
FAULT_TYPE = SA0

## Problem Statement
Manufactured chips may have structural faults at certain places/nodes, which must be tested before being delivered to end users. Even a single fault can alter the output in some input scenarios. This may be disastrous to the aim for which the chip was made. That is why testing is indispensable and we are trying to reduce the cost, time, and effort it takes to test a circuit and to increase the efficiency of the end product. 
The task is to design an algorithm and write its code to identify the input vector required to identify the fault at a given node in a given combinational circuit.
In this case, there would only be a single stuck-at-fault in the design. The number of inputs is four and the output is one. The logic gates used are AND, OR, XOR, and NOT.

## Introduction
The problem can be divided into two smaller sub-problems: <I>Controllability</I> and <I>Observability</i> at the faulty net. <br>
For Controllability, we find all the test vectors that excite the faulty node with the boolean value opposite to what it is stuck at. It is important because the behavior of the circuit will deviate from ideal case behavior in these cases only.
For Observability, we see if a change in the value at the faulty net is propagated to the output or not. As we cannot observe the values of internal nets, so if a faulty value at a net is not causing the output to take a false value then we cannot detect the presence of such a fault.
## Flowchart
<p align="center">
<img src = "https://github.com/Bhawna-Rana/Fault-Detection-in-Combinational-Circuits/blob/master/flowchart%20for%20algorithm.png" width ="500/" height="800/">
</p>

## Alternative Solutions
Alternative 1: Since the number of inputs is four, this fixes the total possible input combinations. We can evaluate the circuit output, for all these 16 input combinations, for a fault-free circuit and a faulty circuit. Then compare the two outputs. The input vector will be the answer if it results in different outputs in the above two cases.
Disadvantages: This is a very basic approach that tests for every possible input combination. Hence the time complexity of this approach is poor.

Alternative 2: This is similar to the implemented approach. In this, two separate lists are formed. One is for storing test vectors that bring that signal to the faulty node which it never gets due to the stuck-at-fault. Another is for storing the test vectors which sensitizes the path from the faulty node to the output. Any change in signal at the faulty node will change the output with these vectors. The required list will be the intersection of these two lists.

## Demonstration
To help visualize the working of the algorithm:
Circuit File:
net_e = A & B
net_f = C | D
net_g = ~ net_f
Z = net_g ^ net_e
For this circuit file, the graph would look like, <be>
<p align="center">
  <img src="https://github.com/Bhawna-Rana/Fault-Detection-in-Combinational-Circuits/blob/master/graph%20example.png" width="500/" height="300/">
</p>
The list that contains those inputs that bring signal value 1 to net_f is:
<p align="center">
 <img src = "https://github.com/Bhawna-Rana/Fault-Detection-in-Combinational-Circuits/blob/master/controllability%20function%20output.png" width="500/" height="300/">
</p>
The corresponding output for the program is:
<p align="center">
 <img src = "https://github.com/Bhawna-Rana/Fault-Detection-in-Combinational-Circuits/blob/master/test_vectors.png" width="500/" height="300/">
</p>


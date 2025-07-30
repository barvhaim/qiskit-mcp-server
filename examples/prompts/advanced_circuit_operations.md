# Advanced Circuit Operations - Prompt Examples

This file contains example prompts for advanced MCP tools including state analysis, optimization, and advanced gates.

## Quantum State Analysis

### Statevector Analysis
```
Analyze the quantum state vector of my Bell state circuit. I want to see:
- The probability of each computational basis state
- The most probable measurement outcome
- The amplitude magnitudes
- Overall state properties
```

### Bell State Analysis
```
I created a Bell state circuit (H on qubit 0, CNOT 0→1). Analyze its statevector to confirm it's properly entangled with 50% probability for |00⟩ and |11⟩.
```

### Superposition State Check
```
Analyze the statevector of my single-qubit circuit after applying a Hadamard gate. Verify it shows equal probability for |0⟩ and |1⟩ states.
```

### Multi-Qubit State Analysis
```
I have a 3-qubit GHZ state circuit. Analyze its statevector and tell me:
- Which states have non-zero probability
- Whether it's maximally entangled
- The distribution of measurement probabilities
```

## Density Matrix Analysis

### Entanglement Detection
```
Compute the density matrix for my Bell state circuit and check:
- Is it a pure state (purity = 1)?
- Is it entangled (check partial trace entropy)?
- What's the von Neumann entropy?
```

### Mixed State Analysis
```
I have a quantum circuit that might create a mixed state. Compute its density matrix and analyze:
- Purity value
- Entropy
- Whether entanglement is present
- Trace value (should be 1)
```

### Quantum State Purity Check
```
Analyze the density matrix of my quantum circuit to determine if I have a pure state or if decoherence/mixing has occurred.
```

### Partial Trace Analysis
```
For my 2-qubit entangled circuit, compute the density matrix and analyze the partial trace. I want to understand the entanglement between the qubits.
```

## Circuit Optimization

### Basic Optimization
```
I have a circuit with redundant gates (like X followed by X). Optimize it using level 1 optimization and show me the improvement in gate count and depth.
```

### Comprehensive Optimization
```
Optimize my quantum circuit using the highest optimization level (level 3). Compare the original and optimized versions:
- Gate count reduction
- Depth improvement
- Percentage improvement
- New optimized circuit name
```

### Optimization Level Comparison
```
Take my circuit and optimize it at all levels (0, 1, 2, 3). Show me how the circuit improves at each level in terms of size and depth.
```

### Performance Analysis
```
I have a complex quantum circuit. Optimize it and provide detailed metrics:
- Original vs optimized gate counts
- Circuit depth reduction
- Which optimization passes were most effective
- Overall performance improvement percentage
```

## Advanced Gate Operations

### Rotation Gates
```
Add advanced rotation gates to my circuit:
- RX(π/4) on qubit 0
- RY(π/2) on qubit 1  
- RZ(π/3) on qubit 2
Then analyze the resulting quantum state.
```

### Two-Qubit Rotations
```
Apply two-qubit rotation gates to create entanglement:
- RXX(π/4) between qubits 0 and 1
- RYY(π/6) between qubits 1 and 2
- RZZ(π/8) between qubits 0 and 2
```

### Universal Gate Sequence
```
Add these advanced gates to demonstrate universality:
1. U(π/2, 0, π) on qubit 0
2. S gate on qubit 1
3. T gate on qubit 2
4. SWAP between qubits 0 and 1
5. S† (S-dagger) on qubit 1
6. T† (T-dagger) on qubit 2
```

### Clifford Group Operations
```
Create a sequence using Clifford gates:
- S and S† gates on different qubits
- T and T† gates for π/8 rotations
- H gates for basis changes
- CNOT gates for entanglement
Show me how these generate the Clifford group.
```

### Parameterized Gate Exploration
```
I want to explore parameterized gates. Add:
- RX gates with different angles (0, π/4, π/2, π)
- RY gates with the same angles
- Compare their effects on quantum states
```

## Variational Circuits

### Basic Variational Circuit
```
Create a variational quantum circuit for machine learning:
- 4 qubits
- 2 layers of the EfficientSU2 ansatz
- Full entanglement pattern
Then show me how many parameters it has.
```

### Entanglement Pattern Comparison
```
Create three variational circuits with 3 qubits and 1 layer, but different entanglement patterns:
1. Full entanglement
2. Linear entanglement  
3. Circular entanglement
Compare their structures and parameter counts.
```

### Custom Named VQC
```
Create a variational quantum circuit for my quantum machine learning experiment:
- 6 qubits
- 3 layers
- Linear entanglement
- Name it "my_qml_ansatz"
```

### VQC Analysis
```
I created a variational circuit. Now:
1. Analyze its initial statevector (before parameter optimization)
2. Show me the circuit structure
3. Tell me how many parameters need to be optimized
4. Suggest how to use it for quantum machine learning
```

## Quantum Fourier Transform

### Standard QFT
```
Implement a Quantum Fourier Transform on 4 qubits. Show me:
- The circuit structure
- Circuit depth and size
- How it could be used for period finding
```

### Inverse QFT
```
Create an inverse Quantum Fourier Transform for 3 qubits and name it "my_iqft". This will be used in quantum phase estimation.
```

### QFT Scaling Analysis
```
Create QFT circuits for 2, 3, 4, and 5 qubits. Compare:
- How circuit depth scales with qubit number
- Gate count growth
- Practical limitations for larger systems
```

### QFT in Quantum Algorithms
```
I'm implementing quantum phase estimation. Create:
1. A 3-qubit inverse QFT circuit
2. Show how it fits into the QPE algorithm
3. Explain its role in extracting phase information
```

## Complete Advanced Workflows

### Quantum State Tomography Prep
```
Prepare for quantum state tomography:
1. Create a 2-qubit Bell state
2. Analyze its statevector
3. Compute density matrix
4. Create multiple measurement circuits (X, Y, Z basis)
5. Optimize all circuits
```

### VQE Algorithm Setup
```
Set up a Variational Quantum Eigensolver workflow:
1. Create a variational ansatz (4 qubits, 2 layers)
2. Analyze the initial state
3. Add Pauli string measurements
4. Optimize the circuit
5. Prepare for classical optimization loop
```

### Quantum Error Correction Demo
```
Demonstrate basic quantum error correction concepts:
1. Create a 3-qubit repetition code circuit
2. Add noise simulation (X gates as bit flips)
3. Add syndrome measurement
4. Show error detection capability
```

### Quantum Algorithm Comparison
```
Compare different quantum approaches:
1. Create a Grover search circuit (2 qubits)
2. Create a variational circuit for the same problem
3. Create a QFT-based approach
4. Analyze and compare their quantum states
5. Optimize all circuits
```

## Error Analysis and Debugging

### State Verification
```
I think my circuit creates the wrong quantum state. Please:
1. Analyze its statevector
2. Check if it matches my expected probabilities
3. Verify entanglement properties
4. Suggest corrections if needed
```

### Optimization Effectiveness
```
I optimized my circuit but want to verify the optimization worked:
1. Compare original vs optimized circuits
2. Verify they produce the same quantum state
3. Confirm gate count reduction
4. Check for any optimization artifacts
```

### Parameter Sensitivity Analysis
```
For my variational circuit with rotation gates:
1. Analyze the state with current parameters
2. Show how sensitive the state is to parameter changes
3. Identify which parameters most affect the outcome
```
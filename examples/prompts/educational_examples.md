# Educational Examples - Prompt Examples

This file contains educational prompts designed to teach quantum computing concepts using the MCP server.

## Quantum Computing Fundamentals

### Quantum Superposition
```
Help me understand quantum superposition:
1. Create a single qubit circuit
2. Show the initial state (should be |0⟩)
3. Apply a Hadamard gate
4. Analyze the statevector - explain why it's 1/√2(|0⟩ + |1⟩)
5. Run measurements to show probabilistic outcomes
6. Explain why we get 50% |0⟩ and 50% |1⟩
```

### Quantum Interference
```
Demonstrate quantum interference:
1. Create a 1-qubit circuit
2. Apply Hadamard (creates superposition)
3. Apply Hadamard again (should return to |0⟩)
4. Analyze the statevector at each step
5. Run measurements to confirm 100% |0⟩
6. Explain how quantum amplitudes interfered constructively
```

### No-Cloning Theorem Demo
```
Illustrate why quantum states cannot be cloned:
1. Create a superposition state |+⟩ = H|0⟩
2. Try to "copy" it using CNOT operations
3. Show that perfect cloning is impossible
4. Analyze the resulting entangled state
5. Explain the fundamental limits of quantum information
```

### Quantum Measurement Effects
```
Show how measurement affects quantum states:
1. Create a Bell state (maximally entangled)
2. Analyze the full 2-qubit statevector
3. Simulate measuring just one qubit
4. Explain how measurement collapses the state
5. Discuss quantum non-locality implications
```

## Quantum Entanglement

### Bell State Creation and Analysis
```
Teach me about quantum entanglement:
1. Create a 2-qubit circuit in |00⟩
2. Apply H gate to first qubit (creates superposition)
3. Apply CNOT gate (creates entanglement)
4. Analyze the resulting Bell state
5. Show that measuring one qubit instantly affects the other
6. Explain why Einstein called this "spooky action at a distance"
```

### GHZ State (3-Qubit Entanglement)
```
Explore multi-qubit entanglement:
1. Create a 3-qubit GHZ state
2. Compare it to Bell state entanglement
3. Analyze the statevector
4. Show all three qubits are maximally entangled
5. Discuss applications in quantum error correction
```

### Entanglement vs Classical Correlation
```
Help me distinguish quantum entanglement from classical correlation:
1. Create a Bell state (quantum entanglement)
2. Create a classical mixed state preparation
3. Compare their density matrices
4. Show entanglement measures (entropy of partial trace)
5. Explain why quantum entanglement is fundamentally different
```

### Entanglement Breaking
```
Show how entanglement can be broken:
1. Create a maximally entangled Bell state
2. Apply noise or decoherence (single-qubit rotations)
3. Analyze how entanglement degrades
4. Show transition from pure to mixed states
5. Discuss quantum error correction needs
```

## Quantum Gates and Operations

### Universal Gate Set
```
Teach me about quantum universality:
1. Show that H and T gates are universal for single qubits
2. Add CNOT for universal quantum computation
3. Decompose complex gates into H, T, CNOT
4. Create the same unitary using different gate sequences
5. Explain why some gate sets are universal
```

### Clifford vs Non-Clifford Gates
```
Explain the difference between Clifford and non-Clifford gates:
1. Use Clifford gates (H, S, CNOT) to create circuits
2. Show these can be simulated efficiently classically
3. Add T gates (non-Clifford) to achieve quantum advantage
4. Explain the role of "magic" states in quantum computation
5. Discuss implications for quantum supremacy
```

### Rotation Gate Exploration
```
Help me understand parameterized quantum gates:
1. Apply RX gates with angles 0, π/4, π/2, π
2. Analyze the resulting states for each angle
3. Show how rotation angle affects measurement probabilities
4. Demonstrate continuous parameter space
5. Explain applications in variational quantum algorithms
```

### Controlled Operations
```
Explore controlled quantum operations:
1. Start with basic CNOT gate
2. Create controlled-Z, controlled-H gates
3. Build multi-controlled operations
4. Show how control qubits affect target operations
5. Explain quantum logic gate implementation
```

## Quantum Algorithms - Educational

### Deutsch Algorithm (Simplest Case)
```
Walk me through the simplest quantum algorithm:
1. Implement Deutsch's algorithm for 1-bit functions
2. Test both constant functions (f(0)=f(1)=0 and f(0)=f(1)=1)
3. Test both balanced functions (f(0)≠f(1))
4. Show how quantum superposition determines function type in one query
5. Compare with classical approach (needs 2 queries)
```

### Phase Kickback Phenomenon
```
Help me understand phase kickback:
1. Create a controlled-Z operation
2. Put control in superposition, target in |1⟩
3. Show how phase appears on control qubit
4. Analyze statevector before and after
5. Explain why this is crucial for many quantum algorithms
```

### Quantum Fourier Transform Intuition
```
Build intuition for Quantum Fourier Transform:
1. Start with classical discrete Fourier transform
2. Create simple periodic quantum states
3. Apply QFT and analyze results
4. Show how QFT reveals frequency content
5. Connect to period-finding applications
```

### Grover's Algorithm Step-by-Step
```
Break down Grover's algorithm:
1. Start with uniform superposition (why?)
2. Apply oracle rotation (marks target)
3. Apply diffusion operator (amplifies marked state)
4. Show geometric interpretation on Bloch sphere
5. Explain optimal number of iterations
```

## Quantum Machine Learning

### Variational Circuit Training
```
Introduce variational quantum algorithms:
1. Create a parameterized quantum circuit
2. Show how parameters affect output states
3. Define a cost function to minimize
4. Demonstrate parameter optimization concept
5. Explain hybrid classical-quantum approach
```

### Quantum Feature Maps
```
Explore quantum feature encoding:
1. Encode classical data into quantum states
2. Use different encoding strategies (amplitude, angle)
3. Show how quantum states represent data
4. Analyze expressivity of quantum feature maps
5. Discuss quantum kernel methods
```

### Quantum Neural Networks
```
Build intuition for quantum neural networks:
1. Create layered variational circuits
2. Show information flow through quantum layers
3. Demonstrate parameter sharing and locality
4. Compare with classical neural network concepts
5. Discuss quantum advantage possibilities
```

## Quantum Error Correction

### Bit-Flip Code
```
Introduce quantum error correction:
1. Encode logical |0⟩ as |000⟩, logical |1⟩ as |111⟩
2. Introduce single bit-flip error
3. Measure syndrome without destroying logical state
4. Apply correction based on syndrome
5. Verify logical state recovery
```

### Phase-Flip Code
```
Complement bit-flip with phase-flip correction:
1. Create phase-flip code using Hadamard conjugation
2. Show how it protects against Z errors
3. Combine concepts for general Pauli errors
4. Explain why both X and Z protection is needed
```

### Quantum Error Correction Threshold
```
Explore error correction thresholds:
1. Show that perfect error correction is impossible
2. Demonstrate error correction with noisy operations
3. Find threshold error rate for beneficial correction
4. Discuss scaling requirements for fault-tolerance
```

## Quantum Complexity

### BQP vs Classical Complexity
```
Explore quantum computational complexity:
1. Implement problems in BQP (bounded-error quantum polynomial)
2. Show polynomial quantum algorithms for hard classical problems
3. Demonstrate quantum query complexity advantages
4. Discuss relationship to NP and other complexity classes
```

### Quantum Speedups
```
Classify different types of quantum speedups:
1. Exponential: Deutsch-Jozsa, Simon's algorithm
2. Polynomial: Grover search (quadratic)
3. Constant factor: Some structured problems
4. Analyze resource requirements for each
5. Discuss practical quantum advantage thresholds
```

## Interactive Learning Exercises

### Quantum State Quiz
```
Create an interactive quantum state identification game:
1. Generate random quantum states
2. Ask me to predict measurement probabilities
3. Let me test hypotheses with different measurements
4. Provide feedback on quantum intuition
5. Build understanding through practice
```

### Circuit Design Challenges
```
Give me quantum circuit design challenges:
1. "Create a state with 75% probability of |0⟩"
2. "Make two qubits anti-correlated"
3. "Design a quantum coin flip that's biased 2:1"
4. "Create maximum entanglement with minimum gates"
5. Check my solutions and provide feedback
```

### Algorithm Implementation Practice
```
Guide me through implementing quantum algorithms from scratch:
1. Give me algorithm descriptions (not implementations)
2. Let me work out the quantum circuit
3. Help debug my implementation
4. Compare with optimal implementations
5. Explain trade-offs and improvements
```

## Conceptual Understanding

### Quantum vs Classical Information
```
Help me understand the fundamental differences:
1. Show classical bit states vs quantum qubit states
2. Demonstrate superposition vs probabilistic mixtures
3. Compare classical correlation vs quantum entanglement
4. Explain information-theoretic advantages
5. Discuss physical implementation challenges
```

### Quantum Measurement Theory
```
Dive deep into quantum measurement:
1. Show projection operators for different measurements
2. Demonstrate Born rule probability calculations
3. Explore partial measurements and conditional states
4. Show measurement disturbance effects
5. Connect to quantum foundations and interpretations
```

### Decoherence and Noise
```
Understand quantum decoherence:
1. Start with perfect quantum states
2. Add realistic noise models
3. Show how coherence is lost over time
4. Demonstrate mixed state evolution
5. Connect to quantum error correction needs
```

### Quantum Advantage Requirements
```
Analyze when quantum computers provide advantages:
1. Problem structure requirements
2. Error rate thresholds
3. Overhead considerations
4. Classical algorithm improvements
5. Practical quantum advantage criteria
```
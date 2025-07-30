# Quantum Algorithms - Prompt Examples

This file contains example prompts for implementing famous quantum algorithms using the MCP server tools.

## Grover's Search Algorithm

### Basic 2-Qubit Grover Search
```
Help me implement Grover's algorithm to search for the state |11⟩ in a 2-qubit space:

1. Create a 2-qubit circuit
2. Initialize superposition with H gates on both qubits
3. Implement the oracle that marks |11⟩ (flip phase)
4. Apply the diffusion operator (inversion about average)
5. Measure and run with 1000 shots

I expect to see a high probability of measuring |11⟩.
```

### 3-Qubit Grover Search
```
Implement Grover's search for finding |101⟩ in a 3-qubit space:
- Create the initial superposition
- Design an oracle for the target state |101⟩
- Apply the diffusion operator
- Run multiple iterations if needed
- Analyze the success probability
```

### Grover Operator Analysis
```
I want to understand Grover's algorithm better:
1. Create the initial superposition state
2. Analyze its statevector (should be uniform)
3. Apply one Grover iteration
4. Analyze the state after iteration
5. Show how the target state probability increases
```

### Amplitude Amplification
```
Use Grover's technique for general amplitude amplification:
1. Create a circuit that prepares a state with small amplitude for |00⟩
2. Use Grover-style operations to amplify this amplitude
3. Measure the probability enhancement
4. Compare before and after amplification
```

## Deutsch-Jozsa Algorithm

### Constant Function Test
```
Implement Deutsch-Jozsa to test a constant function:
1. Create a 4-qubit circuit (3 input + 1 ancilla)
2. Initialize ancilla in |−⟩ state (X then H)
3. Create superposition on input qubits
4. Implement constant function (oracle does nothing)
5. Apply final Hadamards
6. Measure input qubits only
7. Verify 100% probability of |000⟩
```

### Balanced Function Test
```
Test a balanced function with Deutsch-Jozsa:
1. Set up the same initial state as constant case
2. Implement a balanced oracle (e.g., flip ancilla if first input is |1⟩)
3. Complete the algorithm
4. Verify non-zero probability for non-|000⟩ states
5. Compare with constant function results
```

### Algorithm Advantage Demo
```
Demonstrate Deutsch-Jozsa's exponential advantage:
1. Show that classical algorithm needs 2^(n-1) + 1 queries
2. Implement quantum version with just 1 query
3. Test with different function types
4. Analyze the measurement results to classify function type
```

## Quantum Phase Estimation

### Simple Phase Estimation
```
Implement quantum phase estimation for the Z gate:
1. Create a 4-qubit circuit (3 counting + 1 eigenstate)
2. Prepare eigenstate |1⟩ (Z gate eigenstate with eigenvalue -1)
3. Initialize counting qubits in superposition
4. Apply controlled-Z operations (Z^1, Z^2, Z^4)
5. Apply inverse QFT to counting qubits
6. Measure counting qubits
7. Interpret result (should give phase π = binary 0.1...)
```

### T Gate Phase Estimation
```
Estimate the phase of the T gate (π/4):
1. Set up QPE with T gate as the unitary
2. Prepare |1⟩ as eigenstate (eigenvalue e^(iπ/4))
3. Use sufficient counting qubits for precision
4. Apply controlled-T operations
5. Measure and interpret the phase
```

### Phase Estimation Precision
```
Explore phase estimation precision:
1. Implement QPE with different numbers of counting qubits (2, 3, 4)
2. Estimate the same phase for each
3. Compare precision and accuracy
4. Show how more counting qubits improve estimation
```

## Variational Quantum Eigensolver (VQE)

### H₂ Molecule VQE Setup
```
Set up VQE for hydrogen molecule simulation:
1. Create a 4-qubit variational ansatz (2 layers, full entanglement)
2. This represents the molecular orbitals
3. Analyze the initial state before optimization
4. Set up measurement circuits for energy expectation
5. Prepare for classical parameter optimization
```

### VQE Ansatz Comparison
```
Compare different VQE ansätze:
1. Create hardware-efficient ansatz (EfficientSU2)
2. Create a chemistry-inspired ansatz
3. Compare parameter counts and circuit depths
4. Analyze initial state preparations
5. Discuss trade-offs between expressibility and trainability
```

### VQE Energy Landscape
```
Explore VQE energy landscape:
1. Create a simple VQE ansatz
2. Fix some parameters and vary others
3. Create multiple parameter configurations
4. Analyze resulting quantum states
5. Show how parameters affect energy expectation
```

## Quantum Approximate Optimization Algorithm (QAOA)

### Max-Cut QAOA
```
Implement QAOA for a 3-node Max-Cut problem:
1. Create a 3-qubit circuit
2. Initialize in superposition (equal probability for all cuts)
3. Apply problem Hamiltonian (ZZ rotations for graph edges)
4. Apply mixer Hamiltonian (X rotations)
5. Measure and analyze cut quality
6. Show bias toward good cut solutions
```

### QAOA Parameter Analysis
```
Analyze QAOA parameter sensitivity:
1. Create Max-Cut QAOA circuit
2. Test different γ (problem) parameters
3. Test different β (mixer) parameters
4. Show how parameters affect solution quality
5. Identify optimal parameter regions
```

### Multi-Layer QAOA
```
Implement multi-layer QAOA (p=2):
1. Create initial superposition
2. Apply first layer (problem + mixer)
3. Apply second layer with different parameters
4. Compare p=1 vs p=2 performance
5. Analyze circuit depth vs solution quality trade-off
```

## Quantum Fourier Sampling

### Period Finding
```
Use QFT for period finding:
1. Create a register in superposition
2. Apply a periodic function (period = 2)
3. Apply QFT to reveal period information
4. Measure and analyze frequency peaks
5. Extract period from measurement statistics
```

### Discrete Fourier Analysis
```
Demonstrate quantum discrete Fourier transform:
1. Prepare a state with specific frequency content
2. Apply QFT to transform to frequency domain
3. Measure to see frequency peaks
4. Compare with classical DFT expectations
```

### Hidden Subgroup Problem
```
Solve a simple hidden subgroup problem:
1. Create a function that hides a subgroup structure
2. Use QFT-based approach to find the subgroup
3. Analyze measurement results for subgroup generators
4. Verify the hidden structure is revealed
```

## Quantum Simulation

### Ising Model Simulation
```
Simulate quantum Ising model:
1. Create a chain of qubits
2. Apply Ising Hamiltonian evolution (ZZ + X terms)
3. Use Trotter decomposition for time evolution
4. Measure spin correlations
5. Study quantum phase transitions
```

### Quantum Chemistry Simulation
```
Simulate a simple molecule:
1. Map molecular Hamiltonian to qubits
2. Create trial wavefunction with variational circuit
3. Measure Pauli string expectation values
4. Estimate ground state energy
5. Compare with classical methods
```

### Many-Body Dynamics
```
Study quantum many-body dynamics:
1. Prepare initial product state
2. Apply entangling evolution
3. Measure entanglement growth over time
4. Study thermalization and equilibration
5. Analyze information scrambling
```

## Quantum Error Correction

### 3-Qubit Repetition Code
```
Demonstrate basic quantum error correction:
1. Encode logical |0⟩ in 3-qubit code (|000⟩)
2. Introduce bit-flip errors
3. Measure syndrome qubits
4. Implement error correction logic
5. Verify logical state recovery
```

### Surface Code Basics
```
Explore surface code concepts:
1. Create minimal surface code patch
2. Set up stabilizer measurements
3. Introduce and detect errors
4. Show error correction capability
5. Analyze error threshold concepts
```

## Algorithm Comparison and Analysis

### Complexity Comparison
```
Compare quantum algorithm complexities:
1. Implement Grover (√N speedup)
2. Implement Deutsch-Jozsa (exponential speedup)
3. Implement QPE (polynomial in precision)
4. Analyze circuit depths and gate counts
5. Discuss practical quantum advantage
```

### Near-term vs Fault-tolerant
```
Compare NISQ vs fault-tolerant algorithms:
1. VQE/QAOA (near-term, variational)
2. Grover/Shor (fault-tolerant, exact)
3. Analyze noise sensitivity
4. Discuss current feasibility
5. Resource requirement comparison
```

### Hybrid Classical-Quantum
```
Demonstrate hybrid algorithms:
1. Set up VQE with classical optimizer
2. Show parameter update loop structure
3. Implement QAOA with classical preprocessing
4. Analyze classical-quantum communication
5. Discuss co-design opportunities
```

## Educational Examples

### Quantum Algorithm Learning Path
```
Create a learning sequence:
1. Start with simple superposition and measurement
2. Build to Deutsch-Jozsa (first exponential speedup)
3. Progress to Grover (practical search speedup)
4. Advanced: QPE and its applications
5. Modern: VQE and QAOA for near-term devices
```

### Interactive Algorithm Exploration
```
Create interactive quantum algorithm exploration:
1. Let me modify oracle functions
2. Change algorithm parameters
3. Observe effects on success probability
4. Analyze quantum state evolution
5. Compare different quantum strategies
```

### Quantum Advantage Demonstration
```
Show clear quantum advantage examples:
1. Deutsch-Jozsa: 1 query vs exponential classical
2. Grover: quadratic speedup for search
3. Simon's algorithm: exponential separation
4. Quantum simulation: exponential classical difficulty
5. Discuss limitations and requirements
```
# Basic Circuit Operations - Prompt Examples

This file contains example prompts you can use with Claude Desktop to interact with the Qiskit MCP server's basic tools.

## Circuit Creation

### Simple Circuit Creation
```
Create a 2-qubit quantum circuit with 2 classical bits for measurement.
```

### Multi-Qubit Circuit
```
I need a quantum circuit with 5 qubits and 5 classical bits. Can you create one for me?
```

### Circuit with Default Classical Bits
```
Create a quantum circuit with 3 qubits. Use the default number of classical bits.
```

## Adding Basic Gates

### Bell State Creation
```
I have a quantum circuit. Add the following gates to create a Bell state:
1. Apply a Hadamard gate to qubit 0
2. Apply a CNOT gate from qubit 0 to qubit 1  
3. Measure all qubits
```

### Superposition Demo
```
Add a Hadamard gate to qubit 0 of my circuit, then measure all qubits to demonstrate superposition.
```

### Multi-Qubit Entanglement
```
Create a 3-qubit GHZ state by:
- Applying H gate to qubit 0
- CNOT from qubit 0 to qubit 1
- CNOT from qubit 0 to qubit 2
- Measure all qubits
```

### Sequential Gate Operations
```
Add these gates to my circuit in sequence:
1. X gate on qubit 0
2. Y gate on qubit 1  
3. Z gate on qubit 0
4. Hadamard on qubit 1
5. CNOT from qubit 1 to qubit 0
6. Measure qubit 0 to classical bit 0
7. Measure qubit 1 to classical bit 1
```

## Circuit Visualization

### Basic Visualization
```
Show me what my quantum circuit looks like. I want to see the ASCII diagram.
```

### Multiple Circuit Comparison
```
Visualize all the circuits I've created so far. I want to compare their structures.
```

## Circuit Information

### Detailed Circuit Analysis
```
Give me detailed information about my quantum circuit including:
- Number of qubits and classical bits
- Circuit depth and width
- Gate counts for each type
- Total number of operations
```

### Circuit Metrics
```
What's the depth and size of my current circuit? Also show me how many of each type of gate I'm using.
```

## Running Circuits

### Basic Simulation
```
Run my quantum circuit with 1000 shots and show me the measurement results.
```

### High-Precision Sampling
```
Execute my Bell state circuit with 10000 measurement shots to get precise probability estimates.
```

### Quick Test Run
```
Run my circuit with just 100 shots for a quick test of the results.
```

### Statistical Analysis Request
```
Run my quantum circuit and analyze the results. I want to see:
- The measurement outcomes and their counts
- Which states are most probable
- The total number of measurements taken
```

## Circuit Management

### List All Circuits
```
Show me all the quantum circuits I've created in this session, including their basic properties.
```

### Circuit Inventory
```
List all my circuits with their qubit counts, classical bit counts, and gate counts.
```

## Error Handling Examples

### Wrong Circuit Name
```
Add a Hadamard gate to qubit 0 of a circuit called "nonexistent_circuit".
```
*Expected response: Error message about circuit not found*

### Invalid Gate Type
```
Add a "quantum_magic" gate to qubit 0 of my circuit.
```
*Expected response: Error about unsupported gate type*

## Complex Workflows

### Complete Bell State Workflow
```
I want to create and analyze a Bell state. Please:
1. Create a 2-qubit circuit
2. Add H gate to qubit 0
3. Add CNOT from qubit 0 to qubit 1
4. Add measurements
5. Show me the circuit diagram
6. Run it with 1000 shots
7. Analyze the results
```

### Quantum Coin Flip
```
Create a quantum coin flip:
1. Make a 1-qubit circuit
2. Put the qubit in superposition with H gate
3. Measure it
4. Run 1000 times
5. Show me if it's fair (50/50 split)
```

### Three-Qubit W State
```
Help me create a W state with 3 qubits. The W state should have equal superposition of |001⟩, |010⟩, and |100⟩. Then visualize and run the circuit.
```

## Educational Examples

### Quantum Interference Demo
```
Create a circuit that demonstrates quantum interference:
1. Start with 1 qubit
2. Apply H gate (create superposition)  
3. Apply H gate again (should return to |0⟩)
4. Measure and run to verify interference
```

### Pauli Gate Exploration
```
Create a circuit to test all Pauli gates:
1. Make a 3-qubit circuit
2. Apply X gate to qubit 0
3. Apply Y gate to qubit 1  
4. Apply Z gate to qubit 2
5. Measure all and run to see the effects
```

### Phase Kickback Demo
```
Create a circuit showing phase kickback:
1. 2-qubit circuit
2. H on qubit 0 (control)
3. X on qubit 1 (set target to |1⟩)
4. CNOT from qubit 0 to qubit 1
5. H on qubit 0 again
6. Measure and analyze
```
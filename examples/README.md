# Qiskit MCP Server Examples

This directory contains comprehensive examples and test scripts for the Qiskit MCP Server, demonstrating all 13 MCP tools and their applications in quantum computing.

## Directory Structure

```
examples/
├── README.md                          # This file
├── test_scripts/                      # Test scripts and demonstrations
│   ├── test_basic_operations.py       # Basic MCP tools testing
│   ├── test_advanced_operations.py    # Advanced features testing
│   └── test_quantum_algorithms.py     # Quantum algorithms implementation
└── prompts/                          # Example prompts for Claude Desktop
    ├── basic_circuit_operations.md    # Basic circuit creation and manipulation
    ├── advanced_circuit_operations.md # State analysis and optimization
    ├── quantum_algorithms.md          # Famous quantum algorithms
    └── educational_examples.md        # Learning-focused examples
```

## Available MCP Tools

### Core Tools (Original 7)
1. **`create_quantum_circuit`** - Create quantum circuits with unique names
2. **`add_gates`** - Add basic gates (H, X, Y, Z, CNOT, measure)
3. **`run_circuit`** - Execute circuits on quantum simulator
4. **`get_circuit_info`** - Get circuit metadata and statistics
5. **`visualize_circuit`** - Generate ASCII circuit diagrams
6. **`list_circuits`** - List all created circuits

### Advanced Tools (New 6)
7. **`analyze_statevector`** - Quantum state analysis with probabilities
8. **`compute_density_matrix`** - Density matrix analysis and entanglement detection
9. **`optimize_circuit`** - Circuit optimization with performance metrics
10. **`add_advanced_gates`** - Rotation gates, universal gates, Clifford gates
11. **`create_variational_circuit`** - Parameterized circuits for quantum ML
12. **`implement_qft`** - Quantum Fourier Transform implementation

## Test Scripts

### test_basic_operations.py
**Purpose**: Validate core functionality and demonstrate basic quantum circuits

**Key Features**:
- Circuit creation with unique names
- Basic gate operations (H, X, Y, Z, CNOT)
- Circuit simulation and measurement
- Error handling examples
- Simple quantum algorithms (Bell states, GHZ states)

**Usage**:
```bash
python examples/test_scripts/test_basic_operations.py
```

**Example Quantum Circuits**:
- **Bell State**: H(0), CNOT(0,1) → 50% |00⟩ + 50% |11⟩
- **GHZ State**: H(0), CNOT(0,1), CNOT(0,2) → superposition of |000⟩ and |111⟩  
- **Superposition**: H(0) → 50% |0⟩ + 50% |1⟩

### test_advanced_operations.py
**Purpose**: Demonstrate advanced quantum computing capabilities

**Key Features**:
- Quantum state analysis (statevector, density matrix)
- Circuit optimization at multiple levels
- Advanced gate operations (rotations, universal gates)
- Variational quantum circuits
- Quantum Fourier Transform

**Example Workflows**:
- **State Analysis**: Create Bell state → Analyze entanglement → Verify purity
- **Optimization**: Create redundant circuit → Optimize → Compare performance
- **VQE Setup**: Create ansatz → Analyze parameters → Prepare for optimization

### test_quantum_algorithms.py
**Purpose**: Implement famous quantum algorithms

**Quantum Algorithms Covered**:
- **Grover's Search**: Quadratic speedup for database search
- **Deutsch-Jozsa**: Exponential speedup for function evaluation
- **Quantum Phase Estimation**: Eigenvalue estimation for quantum operators
- **VQE**: Variational quantum eigensolver for quantum chemistry
- **QAOA**: Quantum approximate optimization algorithm
- **Quantum Fourier Sampling**: Period finding and frequency analysis

## Prompt Examples

### basic_circuit_operations.md
**Target Audience**: Beginners to quantum computing
**Content**: Simple prompts for circuit creation, gate addition, measurement

**Example Prompts**:
- "Create a 2-qubit quantum circuit and make a Bell state"
- "Add Hadamard gates to create superposition"
- "Run my circuit with 1000 shots and analyze results"

### advanced_circuit_operations.md
**Target Audience**: Intermediate users exploring quantum states
**Content**: State analysis, optimization, advanced gates

**Example Prompts**:
- "Analyze the statevector of my Bell state to verify entanglement"
- "Optimize my circuit and show the improvement metrics"
- "Add rotation gates with specific angles to explore parameter space"

### quantum_algorithms.md
**Target Audience**: Advanced users implementing algorithms
**Content**: Complete algorithm implementations with explanations

**Example Prompts**:
- "Implement Grover's algorithm to search for |11⟩ in 2-qubit space"
- "Set up quantum phase estimation for the Z gate"
- "Create a VQE ansatz for molecular simulation"

### educational_examples.md
**Target Audience**: Students and educators
**Content**: Concept-focused prompts with detailed explanations

**Example Prompts**:
- "Help me understand quantum superposition with step-by-step analysis"
- "Show me why quantum interference allows Hadamard gates to undo themselves"
- "Demonstrate quantum entanglement and explain non-locality"

## Getting Started

### Prerequisites
- Qiskit MCP Server running (see main README.md)
- Claude Desktop with MCP configuration
- Basic understanding of quantum computing concepts

### Quick Start

1. **Start the MCP Server**:
   ```bash
   uv run python main.py
   ```

2. **Use with Claude Desktop**:
   - Copy prompts from the `prompts/` directory
   - Paste into Claude Desktop chat
   - The MCP server will execute the quantum operations

3. **Run Test Scripts** (for validation):
   ```bash
   python examples/test_scripts/test_basic_operations.py
   python examples/test_scripts/test_advanced_operations.py
   python examples/test_scripts/test_quantum_algorithms.py
   ```

### Example Session

```
User: Create a 2-qubit circuit and make a Bell state by applying H to qubit 0 and CNOT from 0 to 1, then measure both qubits.

Claude: I'll create a Bell state circuit for you.

[MCP Tool: create_quantum_circuit]
Parameters: {"num_qubits": 2, "num_classical_bits": 2}
Result: Created quantum circuit 'circuit_1234567890_abcd1234'

[MCP Tool: add_gates]
Parameters: {
  "circuit_name": "circuit_1234567890_abcd1234",
  "gates": [
    {"type": "h", "qubits": [0]},
    {"type": "cx", "qubits": [0, 1]},
    {"type": "measure_all"}
  ]
}
Result: Applied gates: H gate on qubit 0, CNOT gate from qubit 0 to 1, Measure all qubits

[MCP Tool: run_circuit]
Parameters: {"circuit_name": "circuit_1234567890_abcd1234", "shots": 1000}
Result: {"00": 498, "11": 502} (approximately 50% each, confirming Bell state)
```

## Learning Path

### Beginner (Start Here)
1. **Basic Operations**: Circuit creation, simple gates, measurements
2. **Quantum States**: Superposition, measurement probabilities
3. **Two-Qubit Systems**: Entanglement, Bell states
4. **Circuit Analysis**: Visualization, information extraction

### Intermediate
1. **Advanced Gates**: Rotation gates, parameterized operations
2. **State Analysis**: Statevector analysis, density matrices
3. **Circuit Optimization**: Performance improvement techniques
4. **Simple Algorithms**: Deutsch-Jozsa, basic Grover

### Advanced
1. **Complex Algorithms**: Multi-qubit Grover, QPE, VQE
2. **Variational Circuits**: Parameterized quantum circuits
3. **Quantum Machine Learning**: VQE, QAOA applications
4. **Algorithm Development**: Custom quantum algorithms

## Use Cases

### Education
- **Quantum Computing Courses**: Use prompts for homework and demonstrations
- **Research**: Prototype quantum algorithms quickly
- **Self-Learning**: Interactive exploration of quantum concepts

### Development
- **Algorithm Prototyping**: Test quantum algorithms before full implementation
- **Circuit Optimization**: Find optimal circuit implementations
- **State Analysis**: Debug quantum circuits and understand their behavior

### Research
- **Quantum Algorithm Development**: Rapid prototyping and testing
- **Quantum State Engineering**: Design specific quantum states
- **Performance Analysis**: Compare different quantum approaches

## Tips for Effective Use

### Best Practices
1. **Start Simple**: Begin with single-qubit operations before moving to multi-qubit
2. **Analyze States**: Use statevector analysis to understand what your circuits do
3. **Optimize Circuits**: Always check if circuit optimization improves performance
4. **Verify Results**: Use multiple measurement shots for statistical confidence

### Common Patterns
1. **Create → Add Gates → Analyze → Run → Optimize**
2. **Build Algorithm → Test Components → Analyze States → Measure Performance**
3. **Prototype → Optimize → Scale → Validate**

### Troubleshooting
- **Circuit Not Found**: Always create circuits before adding gates
- **Invalid Gates**: Check gate names and parameter formats
- **Analysis Errors**: Remove measurements before state analysis
- **Optimization Issues**: Some circuits may not benefit from optimization

## Contributing

We welcome contributions to expand the examples:

### Adding New Examples
1. Create new test scripts in `test_scripts/`
2. Add corresponding prompts in `prompts/`
3. Update this README with new content
4. Ensure examples are well-documented

### Example Categories Needed
- Quantum error correction demonstrations
- Noise modeling and mitigation
- Quantum supremacy examples
- Advanced quantum algorithms (Shor's, HHL)
- Real-world applications

## Support

- **Main Documentation**: See `/CLAUDE.md` for technical details
- **Qiskit Documentation**: https://qiskit.org/documentation/
- **Quantum Computing Learning**: IBM Qiskit Textbook
- **Issues**: Report bugs and request features via GitHub issues

## License

Same as main project - see project root for license information.
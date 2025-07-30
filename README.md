# Qiskit MCP Server

Unofficial Model Context Protocol (MCP) server that enables LLMs to build and execute quantum circuits using Qiskit.

## Features

The server provides **13 MCP tools** for comprehensive quantum circuit operations:

### Core Tools (8)

### 1. `create_quantum_circuit`
Create a new quantum circuit with specified qubits and classical bits.

**Parameters:**
- `num_qubits` (int): Number of quantum bits
- `num_classical_bits` (int, optional): Number of classical bits (defaults to num_qubits)
- `name` (string, optional): Custom name for the circuit (auto-generated if not provided)

### 2. `add_gates`
Add quantum gates to an existing circuit.

**Parameters:**
- `circuit_name` (string): Name of the circuit to modify
- `gates` (array): List of gate operations

**Supported gates:**
- `h`: Hadamard gate - `{'type': 'h', 'qubits': [0]}`
- `x`: Pauli-X gate - `{'type': 'x', 'qubits': [0]}`
- `y`: Pauli-Y gate - `{'type': 'y', 'qubits': [0]}`
- `z`: Pauli-Z gate - `{'type': 'z', 'qubits': [0]}`
- `cx`: CNOT gate - `{'type': 'cx', 'qubits': [0, 1]}`
- `measure`: Measure specific qubit - `{'type': 'measure', 'qubits': [0], 'classical_bit': 0}`
- `measure_all`: Measure all qubits - `{'type': 'measure_all'}`

### 3. `run_circuit`
Execute a quantum circuit on the BasicSimulator.

**Parameters:**
- `circuit_name` (string): Name of the circuit to run
- `shots` (int, optional): Number of measurement shots (default: 1000)

**Returns:** JSON with measurement results and counts

### 4. `get_circuit_info`
Get detailed information about a circuit.

**Parameters:**
- `circuit_name` (string): Name of the circuit

**Returns:** JSON with circuit properties (qubits, depth, gate counts, etc.)

### 5. `visualize_circuit`
Get a text visualization of the quantum circuit.

**Parameters:**
- `circuit_name` (string): Name of the circuit

**Returns:** ASCII art representation of the circuit

### 6. `visualize_circuit_mermaid`
Generate a Mermaid flowchart diagram of the quantum circuit.

**Parameters:**
- `circuit_name` (string): Name of the circuit to visualize

**Returns:** Mermaid flowchart syntax representing the quantum circuit

### 7. `list_circuits`
List all created circuits with basic information.

**Returns:** JSON with all circuit names and their properties

### Advanced Tools (6)

### 8. `analyze_statevector`
Analyze the quantum state vector of a circuit.

**Parameters:**
- `circuit_name` (string): Name of the circuit to analyze

**Returns:** JSON with probabilities, amplitudes, and state analysis

### 9. `compute_density_matrix`
Compute and analyze the density matrix including purity and entanglement.

**Parameters:**
- `circuit_name` (string): Name of the circuit to analyze

**Returns:** JSON with purity, entropy, and entanglement information

### 10. `optimize_circuit`
Optimize a quantum circuit using Qiskit transpiler passes.

**Parameters:**
- `circuit_name` (string): Name of the circuit to optimize
- `optimization_level` (int): Optimization level 0-3

**Returns:** JSON with optimization results and performance metrics

### 11. `add_advanced_gates`
Add advanced quantum gates beyond basic H, X, Y, Z, CX.

**Parameters:**
- `circuit_name` (string): Name of the circuit to modify
- `gates` (array): List of advanced gate operations

**Supported advanced gates:**
- Rotation gates: `rx`, `ry`, `rz`, `rxx`, `ryy`, `rzz`
- Universal gate: `u`
- Clifford gates: `s`, `sdg`, `t`, `tdg`
- `swap`: SWAP gate

### 12. `create_variational_circuit`
Create a variational quantum circuit for quantum machine learning.

**Parameters:**
- `num_qubits` (int): Number of qubits
- `num_layers` (int): Number of layers (default: 1)
- `entanglement` (string): Entanglement pattern ('full', 'linear', 'circular')
- `name` (string, optional): Custom name for the circuit

**Returns:** Success message with circuit details and parameter count

### 13. `implement_qft`
Implement Quantum Fourier Transform circuit.

**Parameters:**
- `num_qubits` (int): Number of qubits for QFT
- `inverse` (bool): Whether to implement inverse QFT (default: false)
- `name` (string, optional): Custom name for the circuit

**Returns:** Success message with QFT circuit details

## Examples and Documentation

### 📚 Comprehensive Examples
We provide extensive examples and prompts to help you get started:

- **[Examples Folder](./examples/)** - Complete collection of examples and prompts
- **[Examples README](./examples/README.md)** - Detailed guide with learning paths

### 📋 Test Scripts
- **[Basic Operations Tests](./examples/test_scripts/test_basic_operations.py)** - Test cases for core 6 tools
- **[Advanced Operations Tests](./examples/test_scripts/test_advanced_operations.py)** - Test cases for advanced 6 tools  
- **[Quantum Algorithms Tests](./examples/test_scripts/test_quantum_algorithms.py)** - Famous quantum algorithms

### 💬 Ready-to-Use Prompts (130+ Examples)
- **[Basic Circuit Operations](./examples/prompts/basic_circuit_operations.md)** - Beginner-friendly prompts
- **[Advanced Circuit Operations](./examples/prompts/advanced_circuit_operations.md)** - State analysis & optimization
- **[Quantum Algorithms](./examples/prompts/quantum_algorithms.md)** - Algorithm implementations
- **[Educational Examples](./examples/prompts/educational_examples.md)** - Learning-focused prompts

### Quick Start Examples

#### Creating a Bell State
```
Create a 2-qubit quantum circuit and make a Bell state by applying H to qubit 0 and CNOT from 0 to 1, then measure both qubits and run with 1000 shots.
```

#### Advanced State Analysis
```
I have a Bell state circuit. Analyze its statevector to show the probabilities, then compute the density matrix to verify it's entangled with purity=1.0.
```

#### Circuit Optimization
```
Create a circuit with redundant gates (X followed by X), then optimize it at level 2 and show me the improvement metrics.
```

#### Variational Quantum Circuit
```
Create a variational quantum circuit with 4 qubits, 2 layers, and full entanglement for quantum machine learning. Show me how many parameters it has.
```

## Running the Server

### Standalone
```bash
# Install dependencies
uv sync

# Start the MCP server
uv run python main.py
```

### Claude Desktop Integration

Add this configuration to your Claude Desktop config file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "qiskit-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/qiskit-mcp-server",
        "run",
        "main.py"
      ]
    }
  }
}
```

Replace `/path/to/qiskit-mcp-server` with the actual path to this project directory.

After adding the configuration, restart Claude Desktop. You can then ask Claude to:
- "Create a quantum Bell state circuit"
- "Build a Grover search algorithm for 2 qubits"  
- "Analyze the statevector of my circuit to show entanglement"
- "Optimize my circuit and show performance improvements"
- "Create a variational circuit for quantum machine learning"
- "Implement a 3-qubit Quantum Fourier Transform"

## Testing and Validation

### Run Test Scripts
```bash
# Test basic functionality
uv run python examples/test_scripts/test_basic_operations.py

# Test advanced features  
uv run python examples/test_scripts/test_advanced_operations.py

# Test quantum algorithms
uv run python examples/test_scripts/test_quantum_algorithms.py
```

### Direct Testing (Legacy)
```bash
uv run python test_direct.py  # If available
```

## Dependencies

- **qiskit** (≥2.1.1): Quantum computing framework with quantum_info, circuit.library, and transpiler modules
- **fastmcp** (≥2.10.6): MCP server implementation  
- **numpy**: Required for numerical computations in state analysis

## Quantum Computing Concepts Supported

### Core Quantum Mechanics
- **Superposition**: Create quantum superposition with Hadamard gates
- **Entanglement**: Create entangled states with CNOT and advanced gates
- **Measurement**: Collapse quantum states to classical bits
- **Quantum Interference**: Demonstrate constructive/destructive interference

### Advanced Quantum Operations  
- **Parameterized Gates**: RX, RY, RZ rotations with arbitrary angles
- **Two-Qubit Rotations**: RXX, RYY, RZZ for direct entanglement creation
- **Universal Quantum Computation**: Complete gate sets for any quantum algorithm
- **Clifford Operations**: S, T gates for quantum error correction

### Quantum State Analysis
- **Statevector Analysis**: Complete quantum state information with probabilities
- **Density Matrix**: Mixed state analysis, purity, and entropy calculations  
- **Entanglement Detection**: Partial trace entropy to verify quantum correlations
- **State Tomography**: Comprehensive quantum state characterization

### Quantum Algorithms
- **Search Algorithms**: Grover's quadratic speedup for database search
- **Decision Algorithms**: Deutsch-Jozsa exponential advantage
- **Fourier Analysis**: Quantum Fourier Transform for period finding
- **Variational Algorithms**: VQE, QAOA for near-term quantum advantage
- **Phase Estimation**: Extract eigenvalues and phases from quantum operators

### Circuit Optimization & Analysis
- **Transpiler Integration**: Multi-level optimization (0-3) with performance metrics
- **Circuit Depth Analysis**: Critical path analysis and parallelization
- **Gate Count Optimization**: Redundancy removal and commutation analysis
- **Resource Estimation**: Quantum resource requirements for algorithms

### Quantum Machine Learning
- **Variational Circuits**: Parameterized ansätze with different entanglement patterns
- **Quantum Feature Maps**: Encoding classical data into quantum states
- **Hybrid Algorithms**: Classical-quantum optimization loops

The server enables LLMs to interactively build quantum circuits by describing the desired quantum operations in natural language, which get translated into specific gate sequences, analyzed for quantum properties, optimized for performance, and executed on quantum simulators with comprehensive results analysis.

## Project Structure

```
qiskit-mcp-server/
├── main.py                     # MCP server with 13 quantum tools
├── pyproject.toml             # Dependencies and project config
├── examples/                  # Comprehensive examples and documentation
│   ├── README.md             # Learning guide and examples overview  
│   ├── test_scripts/         # Test cases and demonstrations
│   │   ├── test_basic_operations.py      # Core tools testing
│   │   ├── test_advanced_operations.py   # Advanced features testing
│   │   └── test_quantum_algorithms.py    # Algorithm implementations
│   └── prompts/              # 130+ ready-to-use prompt examples
│       ├── basic_circuit_operations.md   # Beginner prompts
│       ├── advanced_circuit_operations.md # State analysis prompts
│       ├── quantum_algorithms.md         # Algorithm prompts
│       └── educational_examples.md       # Learning prompts
└── README.md                  # This file
```

## Getting Help

- **Examples**: Start with the [examples folder](./examples/) for comprehensive guides
- **Qiskit Documentation**: https://qiskit.org/documentation/
- **Quantum Computing Learning**: IBM Qiskit Textbook
- **Issues**: Report bugs and request features via GitHub issues

## Contributing

Contributions are welcome! Areas for expansion:
- Additional quantum algorithms (Shor's, HHL, quantum simulation)
- Noise modeling and error mitigation tools
- Advanced visualization capabilities
- Hardware backend integration
- Educational content and examples

## License

This project is open source. See license file for details.
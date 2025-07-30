from typing import Dict, Any, List, Optional
from fastmcp import FastMCP
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicProvider
from qiskit.quantum_info import Statevector, DensityMatrix, Operator, Pauli
from qiskit.circuit.library import QFTGate, efficient_su2
from qiskit.transpiler.passes import Optimize1qGates, CommutativeCancellation
from qiskit.transpiler import PassManager
import json
import uuid
import time
import numpy as np

# Global circuit storage
circuits: Dict[str, QuantumCircuit] = {}

# Initialize MCP server
mcp = FastMCP("Qiskit MCP Server")

def _generate_unique_circuit_name() -> str:
    """Generate a unique circuit name using timestamp and UUID."""
    timestamp = int(time.time() * 1000)  # milliseconds since epoch
    short_uuid = str(uuid.uuid4())[:8]  # first 8 chars of UUID
    return f"circuit_{timestamp}_{short_uuid}"

@mcp.tool()
def create_quantum_circuit(
    num_qubits: int,
    num_classical_bits: int = None,
    name: str = None
) -> str:
    """
    Create a new quantum circuit with auto-generated unique name.
    
    Args:
        num_qubits: Number of quantum bits (must be an integer)
        num_classical_bits: Number of classical bits (must be an integer, defaults to num_qubits if not provided)
        name: Optional custom name for the circuit (auto-generated if not provided)
    
    Returns:
        Success message with circuit details and generated name
    """
    if num_classical_bits is None:
        num_classical_bits = num_qubits
    
    # Generate unique name if not provided
    if name is None:
        name = _generate_unique_circuit_name()
    else:
        # If custom name is provided, ensure it's unique by appending suffix if needed
        original_name = name
        counter = 1
        while name in circuits:
            name = f"{original_name}_{counter}"
            counter += 1
    
    circuit = QuantumCircuit(num_qubits, num_classical_bits)
    circuits[name] = circuit
    
    return f"Created quantum circuit '{name}' with {num_qubits} qubits and {num_classical_bits} classical bits"

@mcp.tool()
def add_gates(
    circuit_name: str,
    gates: List[Dict[str, Any]]
) -> str:
    """
    Add quantum gates to a circuit.
    
    Args:
        circuit_name: Name of the circuit to modify
        gates: List of gate operations, each with 'type' and 'qubits' keys
               Supported gates: 'h', 'x', 'y', 'z', 'cx', 'measure', 'measure_all'
    
    Returns:
        Success message with applied gates
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found. Create it first."
    
    circuit = circuits[circuit_name]
    applied_gates = []
    
    for gate in gates:
        gate_type = gate.get('type', '').lower()
        qubits = gate.get('qubits', [])
        
        if gate_type == 'h':
            circuit.h(qubits[0])
            applied_gates.append(f"H gate on qubit {qubits[0]}")
        elif gate_type == 'x':
            circuit.x(qubits[0])
            applied_gates.append(f"X gate on qubit {qubits[0]}")
        elif gate_type == 'y':
            circuit.y(qubits[0])
            applied_gates.append(f"Y gate on qubit {qubits[0]}")
        elif gate_type == 'z':
            circuit.z(qubits[0])
            applied_gates.append(f"Z gate on qubit {qubits[0]}")
        elif gate_type == 'cx':
            circuit.cx(qubits[0], qubits[1])
            applied_gates.append(f"CNOT gate from qubit {qubits[0]} to {qubits[1]}")
        elif gate_type == 'measure':
            circuit.measure(qubits[0], gate.get('classical_bit', qubits[0]))
            applied_gates.append(f"Measure qubit {qubits[0]}")
        elif gate_type == 'measure_all':
            circuit.measure_all()
            applied_gates.append("Measure all qubits")
        else:
            return f"Unsupported gate type: {gate_type}"
    
    return f"Applied gates to '{circuit_name}': {', '.join(applied_gates)}"

@mcp.tool()
def run_circuit(
    circuit_name: str,
    shots: int = 1000
) -> str:
    """
    Run a quantum circuit on the simulator.
    
    Args:
        circuit_name: Name of the circuit to run
        shots: Number of measurement shots
    
    Returns:
        JSON string with measurement results
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    circuit = circuits[circuit_name]
    provider = BasicProvider()
    backend = provider.get_backend('basic_simulator')
    
    # Transpile and run
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=shots)
    result = job.result()
    counts = result.get_counts()
    
    return json.dumps({
        "circuit": circuit_name,
        "shots": shots,
        "results": counts,
        "total_counts": sum(counts.values())
    }, indent=2)

@mcp.tool()
def get_circuit_info(circuit_name: str) -> str:
    """
    Get information about a quantum circuit.
    
    Args:
        circuit_name: Name of the circuit
    
    Returns:
        JSON string with circuit information
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    circuit = circuits[circuit_name]
    
    info = {
        "name": circuit_name,
        "num_qubits": circuit.num_qubits,
        "num_classical_bits": circuit.num_clbits,
        "depth": circuit.depth(),
        "size": circuit.size(),
        "width": circuit.width(),
        "gate_counts": dict(circuit.count_ops())
    }
    
    return json.dumps(info, indent=2)

@mcp.tool()
async def visualize_circuit(circuit_name: str) -> str:
    """
    Get a text visualization of the quantum circuit.
    
    Args:
        circuit_name: Name of the circuit to visualize
    
    Returns:
        Text representation of the circuit
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    circuit = circuits[circuit_name]
    return str(circuit.draw(output='text'))

@mcp.tool()
async def visualize_circuit_mermaid(circuit_name: str) -> str:
    """
    Generate a Mermaid flowchart diagram of the quantum circuit.
    
    Args:
        circuit_name: Name of the circuit to visualize
    
    Returns:
        Mermaid flowchart syntax representing the quantum circuit
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    circuit = circuits[circuit_name]
    
    # Start building the Mermaid flowchart
    mermaid_lines = ["flowchart TD"]
    
    # Create nodes for each qubit initialization
    num_qubits = circuit.num_qubits
    num_clbits = circuit.num_clbits
    
    # Add qubit initialization nodes
    for i in range(num_qubits):
        mermaid_lines.append(f"    Q{i}_start[|0⟩ Q{i}]")
    
    # Add classical bit nodes if needed
    for i in range(num_clbits):
        mermaid_lines.append(f"    C{i}_start[0 C{i}]")
    
    # Track current state of each qubit for proper chaining
    qubit_current_nodes = {i: f"Q{i}_start" for i in range(num_qubits)}
    
    # Process circuit instructions
    gate_counter = 0
    for instruction in circuit.data:
        gate = instruction.operation
        qubits = [circuit.find_bit(qubit).index for qubit in instruction.qubits]
        clbits = [circuit.find_bit(clbit).index for clbit in instruction.clbits] if instruction.clbits else []
        
        gate_counter += 1
        gate_name = gate.name.upper()
        
        if gate_name == 'H':
            # Hadamard gate
            node_id = f"H{gate_counter}"
            mermaid_lines.append(f"    {node_id}[H Gate]")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[0]]} --> {node_id}")
            qubit_current_nodes[qubits[0]] = node_id
            
        elif gate_name in ['X', 'Y', 'Z']:
            # Pauli gates
            node_id = f"{gate_name}{gate_counter}"
            mermaid_lines.append(f"    {node_id}[{gate_name} Gate]")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[0]]} --> {node_id}")
            qubit_current_nodes[qubits[0]] = node_id
            
        elif gate_name == 'CX' or gate_name == 'CNOT':
            # CNOT gate
            node_id = f"CNOT{gate_counter}"
            mermaid_lines.append(f"    {node_id}[CNOT Gate]")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[0]]} --> {node_id}")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[1]]} --> {node_id}")
            qubit_current_nodes[qubits[0]] = node_id
            qubit_current_nodes[qubits[1]] = node_id
            
        elif gate_name == 'MEASURE':
            # Measurement
            node_id = f"M{gate_counter}"
            mermaid_lines.append(f"    {node_id}[Measure]")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[0]]} --> {node_id}")
            if clbits:
                mermaid_lines.append(f"    {node_id} --> C{clbits[0]}_end{gate_counter}")
            qubit_current_nodes[qubits[0]] = node_id
            
        elif gate_name.startswith('R'):
            # Rotation gates
            params = getattr(gate, 'params', [])
            param_str = f"({params[0]:.3f})" if params else ""
            node_id = f"{gate_name}{gate_counter}"
            mermaid_lines.append(f"    {node_id}[{gate_name}{param_str}]")
            for qubit in qubits:
                mermaid_lines.append(f"    {qubit_current_nodes[qubit]} --> {node_id}")
                qubit_current_nodes[qubit] = node_id
                
        elif gate_name == 'SWAP':
            # SWAP gate
            node_id = f"SWAP{gate_counter}"
            mermaid_lines.append(f"    {node_id}[SWAP Gate]")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[0]]} --> {node_id}")
            mermaid_lines.append(f"    {qubit_current_nodes[qubits[1]]} --> {node_id}")
            qubit_current_nodes[qubits[0]] = node_id
            qubit_current_nodes[qubits[1]] = node_id
            
        else:
            # Generic gate
            node_id = f"{gate_name}{gate_counter}"
            mermaid_lines.append(f"    {node_id}[{gate_name} Gate]")
            for qubit in qubits:
                mermaid_lines.append(f"    {qubit_current_nodes[qubit]} --> {node_id}")
                qubit_current_nodes[qubit] = node_id
    
    # Add final qubit states
    for i in range(num_qubits):
        mermaid_lines.append(f"    Q{i}_final[Q{i} Final]")
        mermaid_lines.append(f"    {qubit_current_nodes[i]} --> Q{i}_final")
    
    # Add styling
    mermaid_lines.extend([
        "",
        "    %% Styling",
        "    classDef qubitNode fill:#e1f5fe,stroke:#01579b,stroke-width:2px",
        "    classDef gateNode fill:#f3e5f5,stroke:#4a148c,stroke-width:2px",
        "    classDef measureNode fill:#fff3e0,stroke:#e65100,stroke-width:2px",
        "    classDef classicalNode fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px"
    ])
    
    return "\n".join(mermaid_lines)

@mcp.tool()
def list_circuits() -> str:
    """
    List all created circuits.
    
    Returns:
        JSON string with circuit names and basic info
    """
    if not circuits:
        return "No circuits created yet"
    
    circuit_list = {}
    for name, circuit in circuits.items():
        circuit_list[name] = {
            "qubits": circuit.num_qubits,
            "classical_bits": circuit.num_clbits,
            "gates": circuit.size()
        }
    
    return json.dumps(circuit_list, indent=2)

@mcp.tool()
def analyze_statevector(circuit_name: str) -> str:
    """
    Analyze the quantum state vector of a circuit.
    
    Args:
        circuit_name: Name of the circuit to analyze
    
    Returns:
        JSON string with state vector analysis including probabilities and amplitudes
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    circuit = circuits[circuit_name]
    
    # Remove measurements for statevector simulation
    circuit_copy = circuit.copy()
    circuit_copy.remove_final_measurements(inplace=True)
    
    try:
        # Get the statevector
        statevector = Statevector(circuit_copy)
        
        # Calculate probabilities for each computational basis state
        probabilities = statevector.probabilities()
        
        # Get amplitudes
        amplitudes = statevector.data
        
        # Find most probable states
        prob_dict = statevector.probabilities_dict()
        sorted_probs = sorted(prob_dict.items(), key=lambda x: x[1], reverse=True)
        
        analysis = {
            "circuit": circuit_name,
            "num_qubits": circuit.num_qubits,
            "state_dimension": len(amplitudes),
            "probabilities": {state: float(prob) for state, prob in sorted_probs[:10]},  # Top 10
            "total_probability": float(np.sum(probabilities)),
            "most_probable_state": sorted_probs[0][0] if sorted_probs else None,
            "max_probability": float(sorted_probs[0][1]) if sorted_probs else 0.0,
            "amplitudes_magnitude": [float(abs(amp)) for amp in amplitudes[:16]]  # First 16
        }
        
        return json.dumps(analysis, indent=2)
        
    except Exception as e:
        return f"Error analyzing statevector for '{circuit_name}': {str(e)}"

@mcp.tool()
def compute_density_matrix(circuit_name: str) -> str:
    """
    Compute and analyze the density matrix of a quantum circuit.
    
    Args:
        circuit_name: Name of the circuit to analyze
    
    Returns:
        JSON string with density matrix analysis including purity and entropy
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    circuit = circuits[circuit_name]
    
    # Remove measurements for density matrix computation
    circuit_copy = circuit.copy()
    circuit_copy.remove_final_measurements(inplace=True)
    
    try:
        # Get the density matrix via statevector
        statevector = Statevector(circuit_copy)
        density_matrix = DensityMatrix(statevector)
        
        # Compute properties
        purity = density_matrix.purity()
        # Calculate von Neumann entropy manually for density matrix
        eigenvals = np.linalg.eigvals(density_matrix.data)
        eigenvals = eigenvals[eigenvals > 1e-12]  # Remove near-zero eigenvalues
        entropy = -np.sum(eigenvals * np.log2(eigenvals)) if len(eigenvals) > 0 else 0.0
        
        # Get partial traces for entanglement analysis (if multi-qubit)
        analysis = {
            "circuit": circuit_name,
            "num_qubits": circuit.num_qubits,
            "purity": float(purity),
            "entropy": float(entropy),
            "is_pure_state": float(purity) > 0.99,
            "trace": float(np.trace(density_matrix.data))
        }
        
        # Add partial trace analysis for 2+ qubits
        if circuit.num_qubits >= 2:
            try:
                from qiskit.quantum_info import partial_trace
                # Partial trace over first qubit
                partial_trace_dm = partial_trace(density_matrix, [0])
                # Calculate partial trace entropy manually
                pt_eigenvals = np.linalg.eigvals(partial_trace_dm.data)
                pt_eigenvals = pt_eigenvals[pt_eigenvals > 1e-12]
                pt_entropy = -np.sum(pt_eigenvals * np.log2(pt_eigenvals)) if len(pt_eigenvals) > 0 else 0.0
                analysis["partial_trace_entropy"] = float(pt_entropy)
                analysis["entangled"] = float(pt_entropy) > 0.01
            except ImportError:
                analysis["partial_trace_entropy"] = "unavailable"
                analysis["entangled"] = "unknown"
        
        return json.dumps(analysis, indent=2)
        
    except Exception as e:
        return f"Error computing density matrix for '{circuit_name}': {str(e)}"

@mcp.tool()
def optimize_circuit(circuit_name: str, optimization_level: int = 1) -> str:
    """
    Optimize a quantum circuit using Qiskit transpiler passes.
    
    Args:
        circuit_name: Name of the circuit to optimize
        optimization_level: Optimization level (0-3, where 0 is no optimization)
    
    Returns:
        Success message with optimization results and new circuit name
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found"
    
    if optimization_level not in [0, 1, 2, 3]:
        return "Optimization level must be 0, 1, 2, or 3"
    
    circuit = circuits[circuit_name]
    
    try:
        # Create optimization pass manager
        if optimization_level == 0:
            # No optimization
            optimized_circuit = circuit.copy()
        elif optimization_level == 1:
            # Basic optimization
            pass_manager = PassManager([
                Optimize1qGates(),
                CommutativeCancellation()
            ])
            optimized_circuit = pass_manager.run(circuit)
        elif optimization_level == 2:
            # Medium optimization
            pass_manager = PassManager([
                Optimize1qGates(),
                CommutativeCancellation()
            ])
            optimized_circuit = pass_manager.run(circuit)
        else:  # optimization_level == 3
            # High optimization using transpiler
            optimized_circuit = transpile(circuit, optimization_level=3)
        
        # Generate new name for optimized circuit
        optimized_name = f"{circuit_name}_opt{optimization_level}_{str(uuid.uuid4())[:8]}"
        circuits[optimized_name] = optimized_circuit
        
        # Compare circuits
        original_size = circuit.size()
        original_depth = circuit.depth()
        optimized_size = optimized_circuit.size()
        optimized_depth = optimized_circuit.depth()
        
        result = {
            "original_circuit": circuit_name,
            "optimized_circuit": optimized_name,
            "optimization_level": optimization_level,
            "original_size": original_size,
            "optimized_size": optimized_size,
            "size_reduction": original_size - optimized_size,
            "original_depth": original_depth,
            "optimized_depth": optimized_depth,
            "depth_reduction": original_depth - optimized_depth,
            "improvement_percentage": round(((original_size - optimized_size) / original_size * 100), 2) if original_size > 0 else 0
        }
        
        return json.dumps(result, indent=2)
        
    except Exception as e:
        return f"Error optimizing circuit '{circuit_name}': {str(e)}"

@mcp.tool()
def add_advanced_gates(
    circuit_name: str,
    gates: List[Dict[str, Any]]
) -> str:
    """
    Add advanced quantum gates to a circuit beyond basic H, X, Y, Z, CX.
    
    Args:
        circuit_name: Name of the circuit to modify
        gates: List of advanced gate operations
               Supported gates: 'rx', 'ry', 'rz', 'rxx', 'ryy', 'rzz', 'u', 'swap', 's', 'sdg', 't', 'tdg'
    
    Returns:
        Success message with applied gates
    """
    if circuit_name not in circuits:
        return f"Circuit '{circuit_name}' not found. Create it first."
    
    circuit = circuits[circuit_name]
    applied_gates = []
    
    try:
        for gate in gates:
            gate_type = gate.get('type', '').lower()
            qubits = gate.get('qubits', [])
            params = gate.get('params', [])
            
            if gate_type == 'rx':
                angle = params[0] if params else 0
                circuit.rx(angle, qubits[0])
                applied_gates.append(f"RX({angle}) gate on qubit {qubits[0]}")
            elif gate_type == 'ry':
                angle = params[0] if params else 0
                circuit.ry(angle, qubits[0])
                applied_gates.append(f"RY({angle}) gate on qubit {qubits[0]}")
            elif gate_type == 'rz':
                angle = params[0] if params else 0
                circuit.rz(angle, qubits[0])
                applied_gates.append(f"RZ({angle}) gate on qubit {qubits[0]}")
            elif gate_type == 'rxx':
                angle = params[0] if params else 0
                circuit.rxx(angle, qubits[0], qubits[1])
                applied_gates.append(f"RXX({angle}) gate on qubits {qubits[0]}, {qubits[1]}")
            elif gate_type == 'ryy':
                angle = params[0] if params else 0
                circuit.ryy(angle, qubits[0], qubits[1])
                applied_gates.append(f"RYY({angle}) gate on qubits {qubits[0]}, {qubits[1]}")
            elif gate_type == 'rzz':
                angle = params[0] if params else 0
                circuit.rzz(angle, qubits[0], qubits[1])
                applied_gates.append(f"RZZ({angle}) gate on qubits {qubits[0]}, {qubits[1]}")
            elif gate_type == 'u':
                theta = params[0] if len(params) > 0 else 0
                phi = params[1] if len(params) > 1 else 0
                lam = params[2] if len(params) > 2 else 0
                circuit.u(theta, phi, lam, qubits[0])
                applied_gates.append(f"U({theta}, {phi}, {lam}) gate on qubit {qubits[0]}")
            elif gate_type == 'swap':
                circuit.swap(qubits[0], qubits[1])
                applied_gates.append(f"SWAP gate on qubits {qubits[0]}, {qubits[1]}")
            elif gate_type == 's':
                circuit.s(qubits[0])
                applied_gates.append(f"S gate on qubit {qubits[0]}")
            elif gate_type == 'sdg':
                circuit.sdg(qubits[0])
                applied_gates.append(f"S† gate on qubit {qubits[0]}")
            elif gate_type == 't':
                circuit.t(qubits[0])
                applied_gates.append(f"T gate on qubit {qubits[0]}")
            elif gate_type == 'tdg':
                circuit.tdg(qubits[0])
                applied_gates.append(f"T† gate on qubit {qubits[0]}")
            else:
                return f"Unsupported advanced gate type: {gate_type}"
        
        return f"Applied advanced gates to '{circuit_name}': {', '.join(applied_gates)}"
        
    except Exception as e:
        return f"Error adding advanced gates to '{circuit_name}': {str(e)}"

@mcp.tool()
def create_variational_circuit(
    num_qubits: int,
    num_layers: int = 1,
    entanglement: str = "full",
    name: str = None
) -> str:
    """
    Create a variational quantum circuit (ansatz) for quantum machine learning.
    
    Args:
        num_qubits: Number of qubits
        num_layers: Number of repetitions of the ansatz
        entanglement: Entanglement strategy ('full', 'linear', 'circular')
        name: Optional custom name for the circuit
    
    Returns:
        Success message with circuit details
    """
    try:
        # Generate unique name if not provided
        if name is None:
            name = _generate_unique_circuit_name()
        else:
            # Ensure uniqueness
            original_name = name
            counter = 1
            while name in circuits:
                name = f"{original_name}_{counter}"
                counter += 1
        
        # Create variational circuit using EfficientSU2 ansatz
        ansatz = efficient_su2(
            num_qubits=num_qubits,
            reps=num_layers,
            entanglement=entanglement
        )
        
        circuits[name] = ansatz
        
        return f"Created variational quantum circuit '{name}' with {num_qubits} qubits, {num_layers} layers, {entanglement} entanglement. Parameters: {ansatz.num_parameters}"
        
    except Exception as e:
        return f"Error creating variational circuit: {str(e)}"

@mcp.tool()
def implement_qft(num_qubits: int, inverse: bool = False, name: str = None) -> str:
    """
    Implement Quantum Fourier Transform circuit.
    
    Args:
        num_qubits: Number of qubits for QFT
        inverse: Whether to implement inverse QFT
        name: Optional custom name for the circuit
    
    Returns:
        Success message with QFT circuit details
    """
    try:
        # Generate unique name if not provided
        if name is None:
            qft_type = "iqft" if inverse else "qft"
            name = f"{qft_type}_{num_qubits}q_{str(uuid.uuid4())[:8]}"
        else:
            # Ensure uniqueness
            original_name = name
            counter = 1
            while name in circuits:
                name = f"{original_name}_{counter}"
                counter += 1
        
        # Create QFT circuit
        qft_circuit = QuantumCircuit(num_qubits)
        if inverse:
            qft_gate = QFTGate(num_qubits=num_qubits).inverse()
        else:
            qft_gate = QFTGate(num_qubits=num_qubits)
        qft_circuit.append(qft_gate, range(num_qubits))
        
        circuits[name] = qft_circuit
        
        qft_type_str = "Inverse Quantum Fourier Transform" if inverse else "Quantum Fourier Transform"
        
        return f"Created {qft_type_str} circuit '{name}' with {num_qubits} qubits. Depth: {qft_circuit.depth()}, Size: {qft_circuit.size()}"
        
    except Exception as e:
        return f"Error creating QFT circuit: {str(e)}"

if __name__ == "__main__":
    mcp.run()
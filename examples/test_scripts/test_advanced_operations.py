#!/usr/bin/env python3
"""
Test script for advanced MCP tools: state analysis, optimization, and advanced gates.
This demonstrates the extended functionality of the Qiskit MCP server.
"""

import json
import math

def test_state_analysis():
    """Test quantum state analysis tools."""
    print("🔬 Testing Quantum State Analysis")
    print("=" * 50)
    
    # Test 1: Statevector analysis of Bell state
    print("\n1. Analyzing Bell state statevector...")
    bell_setup = {
        "steps": [
            {"tool": "create_quantum_circuit", "params": {"num_qubits": 2}},
            {"tool": "add_gates", "params": {
                "gates": [
                    {"type": "h", "qubits": [0]},
                    {"type": "cx", "qubits": [0, 1]}
                ]
            }},
            {"tool": "analyze_statevector", "params": {"circuit_name": "<circuit_name>"}}
        ]
    }
    print(f"   Workflow: {json.dumps(bell_setup, indent=2)}")
    print("   Expected: probabilities={'00': 0.5, '11': 0.5}, total_probability=1.0")
    
    # Test 2: Density matrix analysis
    print("\n2. Computing density matrix...")
    density_params = {
        "circuit_name": "<bell_circuit>"
    }
    print(f"   Parameters: {json.dumps(density_params, indent=2)}")
    print("   Expected: purity=1.0 (pure state), entropy=0.0, entangled=true")
    
    # Test 3: Mixed state analysis
    print("\n3. Analyzing mixed state (single qubit)...")
    mixed_setup = {
        "steps": [
            {"tool": "create_quantum_circuit", "params": {"num_qubits": 1}},
            {"tool": "add_gates", "params": {
                "gates": [{"type": "h", "qubits": [0]}]
            }},
            {"tool": "compute_density_matrix", "params": {"circuit_name": "<circuit_name>"}}
        ]
    }
    print(f"   Workflow: {json.dumps(mixed_setup, indent=2)}")
    print("   Expected: purity=1.0, entropy=0.0 (still pure state)")

def test_circuit_optimization():
    """Test circuit optimization capabilities."""
    print("\n\n⚡ Testing Circuit Optimization")
    print("=" * 50)
    
    # Test 1: Basic optimization
    print("\n1. Optimizing redundant circuit...")
    redundant_setup = {
        "steps": [
            {"tool": "create_quantum_circuit", "params": {"num_qubits": 2}},
            {"tool": "add_gates", "params": {
                "gates": [
                    {"type": "x", "qubits": [0]},
                    {"type": "x", "qubits": [0]},  # Redundant - cancels out
                    {"type": "h", "qubits": [1]},
                    {"type": "h", "qubits": [1]}   # Redundant - cancels out
                ]
            }},
            {"tool": "optimize_circuit", "params": {
                "circuit_name": "<circuit_name>",
                "optimization_level": 1
            }}
        ]
    }
    print(f"   Workflow: {json.dumps(redundant_setup, indent=2)}")
    print("   Expected: original_size=4, optimized_size=0, improvement_percentage=100%")
    
    # Test 2: Different optimization levels
    print("\n2. Testing optimization levels...")
    opt_levels = [
        {"level": 0, "description": "No optimization"},
        {"level": 1, "description": "Basic optimization (1-qubit gates, commutation)"},
        {"level": 2, "description": "Medium optimization (+ CNOT cancellation)"},
        {"level": 3, "description": "High optimization (full transpiler)"}
    ]
    
    for opt in opt_levels:
        params = {
            "circuit_name": "<complex_circuit>",
            "optimization_level": opt["level"]
        }
        print(f"   Level {opt['level']}: {opt['description']}")
        print(f"   Parameters: {json.dumps(params, indent=2)}")

def test_advanced_gates():
    """Test advanced gate operations."""
    print("\n\n🎛️  Testing Advanced Gates")
    print("=" * 50)
    
    # Test 1: Rotation gates
    print("\n1. Testing rotation gates...")
    rotation_gates = {
        "circuit_name": "<circuit_name>",
        "gates": [
            {"type": "rx", "qubits": [0], "params": [math.pi/4]},
            {"type": "ry", "qubits": [1], "params": [math.pi/2]},
            {"type": "rz", "qubits": [0], "params": [math.pi/3]}
        ]
    }
    print(f"   Parameters: {json.dumps(rotation_gates, indent=2)}")
    print("   Expected: RX(π/4), RY(π/2), RZ(π/3) gates applied")
    
    # Test 2: Two-qubit rotation gates
    print("\n2. Testing two-qubit rotation gates...")
    two_qubit_rotations = {
        "circuit_name": "<circuit_name>",
        "gates": [
            {"type": "rxx", "qubits": [0, 1], "params": [math.pi/4]},
            {"type": "ryy", "qubits": [0, 1], "params": [math.pi/6]},
            {"type": "rzz", "qubits": [0, 1], "params": [math.pi/8]}
        ]
    }
    print(f"   Parameters: {json.dumps(two_qubit_rotations, indent=2)}")
    print("   Expected: RXX(π/4), RYY(π/6), RZZ(π/8) gates applied")
    
    # Test 3: Universal and Clifford gates
    print("\n3. Testing universal and Clifford gates...")
    universal_gates = {
        "circuit_name": "<circuit_name>",
        "gates": [
            {"type": "u", "qubits": [0], "params": [math.pi/2, 0, math.pi]},
            {"type": "s", "qubits": [1]},
            {"type": "sdg", "qubits": [1]},
            {"type": "t", "qubits": [0]},
            {"type": "tdg", "qubits": [0]},
            {"type": "swap", "qubits": [0, 1]}
        ]
    }
    print(f"   Parameters: {json.dumps(universal_gates, indent=2)}")
    print("   Expected: U(π/2,0,π), S, S†, T, T†, SWAP gates applied")

def test_variational_circuits():
    """Test variational quantum circuit creation."""
    print("\n\n🧬 Testing Variational Circuits")
    print("=" * 50)
    
    # Test 1: Basic variational circuit
    print("\n1. Creating EfficientSU2 ansatz...")
    basic_variational = {
        "num_qubits": 4,
        "num_layers": 2,
        "entanglement": "full"
    }
    print(f"   Parameters: {json.dumps(basic_variational, indent=2)}")
    print("   Expected: Circuit with ~16-18 parameters, depth ~12")
    
    # Test 2: Different entanglement patterns
    print("\n2. Testing entanglement patterns...")
    entanglement_types = ["full", "linear", "circular"]
    
    for ent in entanglement_types:
        params = {
            "num_qubits": 3,
            "num_layers": 1,
            "entanglement": ent
        }
        print(f"   {ent.capitalize()} entanglement: {json.dumps(params, indent=2)}")
    
    # Test 3: Custom named variational circuit
    print("\n3. Creating custom named variational circuit...")
    custom_params = {
        "num_qubits": 2,
        "num_layers": 3,
        "entanglement": "linear",
        "name": "my_vqc_ansatz"
    }
    print(f"   Parameters: {json.dumps(custom_params, indent=2)}")
    print("   Expected: Circuit named 'my_vqc_ansatz' (or 'my_vqc_ansatz_1' if duplicate)")

def test_qft_circuits():
    """Test Quantum Fourier Transform implementation."""
    print("\n\n🌊 Testing Quantum Fourier Transform")
    print("=" * 50)
    
    # Test 1: Standard QFT
    print("\n1. Creating standard QFT...")
    qft_params = {
        "num_qubits": 3,
        "inverse": False
    }
    print(f"   Parameters: {json.dumps(qft_params, indent=2)}")
    print("   Expected: QFT circuit with name like 'qft_3q_abcd1234'")
    
    # Test 2: Inverse QFT
    print("\n2. Creating inverse QFT...")
    iqft_params = {
        "num_qubits": 4,
        "inverse": True,
        "name": "my_iqft"
    }
    print(f"   Parameters: {json.dumps(iqft_params, indent=2)}")
    print("   Expected: Inverse QFT circuit named 'my_iqft'")
    
    # Test 3: QFT size comparison
    print("\n3. QFT scaling with qubit count...")
    for n_qubits in [2, 3, 4, 5]:
        print(f"   {n_qubits} qubits: Expected depth ~O(n²), size ~O(n²)")

def demo_complete_workflow():
    """Demonstrate a complete quantum circuit workflow."""
    print("\n\n🔄 Complete Workflow Example")
    print("=" * 50)
    
    workflow = {
        "description": "Create, optimize, and analyze a quantum algorithm",
        "steps": [
            {
                "step": 1,
                "action": "Create variational circuit",
                "tool": "create_variational_circuit",
                "params": {"num_qubits": 3, "num_layers": 2}
            },
            {
                "step": 2,
                "action": "Add measurement",
                "tool": "add_gates",
                "params": {"gates": [{"type": "measure_all"}]}
            },
            {
                "step": 3,
                "action": "Analyze original state",
                "tool": "analyze_statevector",
                "params": {"circuit_name": "<before_measure>"}
            },
            {
                "step": 4,
                "action": "Optimize circuit",
                "tool": "optimize_circuit",
                "params": {"optimization_level": 2}
            },
            {
                "step": 5,
                "action": "Run simulation",
                "tool": "run_circuit",
                "params": {"shots": 1000}
            },
            {
                "step": 6,
                "action": "Get final info",
                "tool": "get_circuit_info",
                "params": {}
            }
        ]
    }
    
    print(f"Complete Workflow: {json.dumps(workflow, indent=2)}")

if __name__ == "__main__":
    print("Qiskit MCP Server - Advanced Operations Test Guide")
    print("=" * 60)
    print("This script provides test cases for advanced MCP tools including")
    print("state analysis, optimization, advanced gates, and quantum algorithms.")
    
    test_state_analysis()
    test_circuit_optimization()
    test_advanced_gates()
    test_variational_circuits()
    test_qft_circuits()
    demo_complete_workflow()
    
    print("\n\n✅ Advanced Test Guide Complete!")
    print("These examples showcase the full capabilities of the MCP server.")
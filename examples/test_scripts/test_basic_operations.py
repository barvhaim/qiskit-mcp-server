#!/usr/bin/env python3
"""
Test script for basic MCP tools: circuit creation, gate addition, and execution.
This demonstrates the core functionality of the Qiskit MCP server.
"""

import json

def test_basic_operations():
    """Test basic circuit operations."""
    print("🧪 Testing Basic Circuit Operations")
    print("=" * 50)
    
    # Test 1: Create a quantum circuit
    print("\n1. Creating a quantum circuit...")
    # This would be called via MCP in practice, showing the expected parameters
    circuit_params = {
        "num_qubits": 2,
        "num_classical_bits": 2
    }
    print(f"   Parameters: {json.dumps(circuit_params, indent=2)}")
    print("   Expected: Circuit created with unique name like 'circuit_1234567890_abcd1234'")
    
    # Test 2: Add basic gates
    print("\n2. Adding basic gates to create a Bell state...")
    gates_params = {
        "circuit_name": "<circuit_name_from_step_1>",
        "gates": [
            {"type": "h", "qubits": [0]},
            {"type": "cx", "qubits": [0, 1]},
            {"type": "measure_all"}
        ]
    }
    print(f"   Parameters: {json.dumps(gates_params, indent=2)}")
    print("   Expected: Hadamard on qubit 0, CNOT from 0→1, measure all qubits")
    
    # Test 3: Get circuit information
    print("\n3. Getting circuit information...")
    info_params = {
        "circuit_name": "<circuit_name>"
    }
    print(f"   Parameters: {json.dumps(info_params, indent=2)}")
    print("   Expected: Circuit depth=2, size=3, gate_counts={'h': 1, 'cx': 1, 'measure': 2}")
    
    # Test 4: Visualize circuit
    print("\n4. Visualizing the circuit...")
    viz_params = {
        "circuit_name": "<circuit_name>"
    }
    print(f"   Parameters: {json.dumps(viz_params, indent=2)}")
    print("   Expected: ASCII art showing H gate, CNOT, and measurements")
    
    # Test 5: Run circuit simulation
    print("\n5. Running circuit simulation...")
    run_params = {
        "circuit_name": "<circuit_name>",
        "shots": 1000
    }
    print(f"   Parameters: {json.dumps(run_params, indent=2)}")
    print("   Expected: Results showing ~50% '00' and ~50% '11' (Bell state)")
    
    # Test 6: List all circuits
    print("\n6. Listing all circuits...")
    print("   Parameters: None")
    print("   Expected: JSON with all created circuits and their properties")

def test_error_handling():
    """Test error handling scenarios."""
    print("\n\n🚨 Testing Error Handling")
    print("=" * 50)
    
    # Test invalid circuit name
    print("\n1. Testing invalid circuit name...")
    invalid_params = {
        "circuit_name": "nonexistent_circuit",
        "gates": [{"type": "h", "qubits": [0]}]
    }
    print(f"   Parameters: {json.dumps(invalid_params, indent=2)}")
    print("   Expected: 'Circuit 'nonexistent_circuit' not found. Create it first.'")
    
    # Test invalid gate type
    print("\n2. Testing invalid gate type...")
    invalid_gate_params = {
        "circuit_name": "<circuit_name>",
        "gates": [{"type": "invalid_gate", "qubits": [0]}]
    }
    print(f"   Parameters: {json.dumps(invalid_gate_params, indent=2)}")
    print("   Expected: 'Unsupported gate type: invalid_gate'")

def demo_quantum_algorithms():
    """Demonstrate creating common quantum algorithms."""
    print("\n\n🔬 Quantum Algorithm Examples")
    print("=" * 50)
    
    # Bell State
    print("\n1. Bell State (Quantum Entanglement)")
    bell_example = {
        "steps": [
            {"tool": "create_quantum_circuit", "params": {"num_qubits": 2}},
            {"tool": "add_gates", "params": {
                "gates": [
                    {"type": "h", "qubits": [0]},
                    {"type": "cx", "qubits": [0, 1]},
                    {"type": "measure_all"}
                ]
            }},
            {"tool": "run_circuit", "params": {"shots": 1000}}
        ]
    }
    print(f"   Workflow: {json.dumps(bell_example, indent=2)}")
    
    # GHZ State
    print("\n2. GHZ State (3-qubit entangled state)")
    ghz_example = {
        "steps": [
            {"tool": "create_quantum_circuit", "params": {"num_qubits": 3}},
            {"tool": "add_gates", "params": {
                "gates": [
                    {"type": "h", "qubits": [0]},
                    {"type": "cx", "qubits": [0, 1]},
                    {"type": "cx", "qubits": [0, 2]},
                    {"type": "measure_all"}
                ]
            }},
            {"tool": "run_circuit", "params": {"shots": 1000}}
        ]
    }
    print(f"   Workflow: {json.dumps(ghz_example, indent=2)}")
    
    # Quantum Superposition
    print("\n3. Superposition Demo")
    superposition_example = {
        "steps": [
            {"tool": "create_quantum_circuit", "params": {"num_qubits": 1}},
            {"tool": "add_gates", "params": {
                "gates": [
                    {"type": "h", "qubits": [0]},
                    {"type": "measure_all"}
                ]
            }},
            {"tool": "run_circuit", "params": {"shots": 1000}}
        ]
    }
    print(f"   Workflow: {json.dumps(superposition_example, indent=2)}")
    print("   Expected: ~50% '0' and ~50% '1' outcomes")

if __name__ == "__main__":
    print("Qiskit MCP Server - Basic Operations Test Guide")
    print("=" * 60)
    print("This script provides test cases and expected outcomes for basic MCP tools.")
    print("Use these examples with Claude Desktop or direct MCP calls.")
    
    test_basic_operations()
    test_error_handling()
    demo_quantum_algorithms()
    
    print("\n\n✅ Test Guide Complete!")
    print("Use these examples as templates for testing the MCP server.")
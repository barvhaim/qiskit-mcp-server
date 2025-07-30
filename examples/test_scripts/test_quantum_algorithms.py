#!/usr/bin/env python3
"""
Test script for implementing famous quantum algorithms using the MCP tools.
This demonstrates practical applications and algorithm implementations.
"""

import json
import math

def test_grover_algorithm():
    """Test Grover's search algorithm implementation."""
    print("🔍 Grover's Search Algorithm")
    print("=" * 50)
    
    print("\n1. Two-qubit Grover search (searching for |11⟩)...")
    grover_2q = {
        "description": "Search for state |11⟩ in 2-qubit space",
        "steps": [
            {
                "step": 1,
                "action": "Create circuit",
                "tool": "create_quantum_circuit",
                "params": {"num_qubits": 2, "num_classical_bits": 2}
            },
            {
                "step": 2,
                "action": "Initialize superposition",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]}
                    ]
                }
            },
            {
                "step": 3,
                "action": "Oracle: mark |11⟩",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "cz", "qubits": [0, 1]}  # Would need to add CZ support
                    ]
                }
            },
            {
                "step": 4,
                "action": "Diffusion operator",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]},
                        {"type": "x", "qubits": [0]},
                        {"type": "x", "qubits": [1]},
                        {"type": "h", "qubits": [1]},
                        {"type": "cx", "qubits": [0, 1]},
                        {"type": "h", "qubits": [1]},
                        {"type": "x", "qubits": [0]},
                        {"type": "x", "qubits": [1]},
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]}
                    ]
                }
            },
            {
                "step": 5,
                "action": "Measure and run",
                "tool": "add_gates",
                "params": {"gates": [{"type": "measure_all"}]}
            },
            {
                "step": 6,
                "action": "Execute",
                "tool": "run_circuit",
                "params": {"shots": 1000}
            }
        ]
    }
    print(f"   Implementation: {json.dumps(grover_2q, indent=2)}")
    print("   Expected: High probability of measuring |11⟩ (~85-90%)")

def test_deutsch_jozsa():
    """Test Deutsch-Jozsa algorithm."""
    print("\n\n🎯 Deutsch-Jozsa Algorithm")
    print("=" * 50)
    
    print("\n1. Testing constant function (always 0)...")
    dj_constant = {
        "description": "Distinguish constant vs balanced function",
        "steps": [
            {
                "step": 1,
                "action": "Create circuit (3 input + 1 ancilla)",
                "tool": "create_quantum_circuit",
                "params": {"num_qubits": 4, "num_classical_bits": 3}
            },
            {
                "step": 2,
                "action": "Initialize ancilla in |−⟩",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "x", "qubits": [3]},
                        {"type": "h", "qubits": [3]}
                    ]
                }
            },
            {
                "step": 3,
                "action": "Initialize inputs in superposition",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]},
                        {"type": "h", "qubits": [2]}
                    ]
                }
            },
            {
                "step": 4,
                "action": "Oracle (constant function - do nothing)",
                "tool": "add_gates",
                "params": {"gates": []}  # No gates for constant 0
            },
            {
                "step": 5,
                "action": "Final Hadamards",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]},
                        {"type": "h", "qubits": [2]}
                    ]
                }
            },
            {
                "step": 6,
                "action": "Measure inputs only",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "measure", "qubits": [0], "classical_bit": 0},
                        {"type": "measure", "qubits": [1], "classical_bit": 1},
                        {"type": "measure", "qubits": [2], "classical_bit": 2}
                    ]
                }
            },
            {
                "step": 7,
                "action": "Execute",
                "tool": "run_circuit",
                "params": {"shots": 1000}
            }
        ]
    }
    print(f"   Implementation: {json.dumps(dj_constant, indent=2)}")
    print("   Expected: 100% probability of measuring |000⟩ (constant function)")

def test_quantum_phase_estimation():
    """Test Quantum Phase Estimation algorithm."""
    print("\n\n📐 Quantum Phase Estimation")
    print("=" * 50)
    
    print("\n1. Estimating phase of Z gate (eigenvalue -1, phase π)...")
    qpe_z_gate = {
        "description": "Estimate phase π of Z gate eigenstate |1⟩",
        "steps": [
            {
                "step": 1,
                "action": "Create circuit (3 counting + 1 eigenstate)",
                "tool": "create_quantum_circuit",
                "params": {"num_qubits": 4, "num_classical_bits": 3}
            },
            {
                "step": 2,
                "action": "Prepare eigenstate |1⟩",
                "tool": "add_gates",
                "params": {"gates": [{"type": "x", "qubits": [3]}]}
            },
            {
                "step": 3,
                "action": "Initialize counting qubits",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]},
                        {"type": "h", "qubits": [2]}
                    ]
                }
            },
            {
                "step": 4,
                "action": "Controlled unitary operations",
                "tool": "add_advanced_gates",
                "params": {
                    "gates": [
                        # CZ^1 (controlled by qubit 2)
                        {"type": "cz", "qubits": [2, 3]},
                        # CZ^2 (controlled by qubit 1)
                        {"type": "cz", "qubits": [1, 3]},
                        {"type": "cz", "qubits": [1, 3]},
                        # CZ^4 (controlled by qubit 0)
                        {"type": "cz", "qubits": [0, 3]},
                        {"type": "cz", "qubits": [0, 3]},
                        {"type": "cz", "qubits": [0, 3]},
                        {"type": "cz", "qubits": [0, 3]}
                    ]
                }
            },
            {
                "step": 5,
                "action": "Inverse QFT on counting qubits",
                "tool": "implement_qft",
                "params": {"num_qubits": 3, "inverse": True, "name": "iqft_qpe"}
            },
            {
                "step": 6,
                "action": "Measure counting qubits",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "measure", "qubits": [0], "classical_bit": 0},
                        {"type": "measure", "qubits": [1], "classical_bit": 1},
                        {"type": "measure", "qubits": [2], "classical_bit": 2}
                    ]
                }
            }
        ]
    }
    print(f"   Implementation: {json.dumps(qpe_z_gate, indent=2)}")
    print("   Expected: High probability of measuring |100⟩ (binary: 0.1 = phase 1/2 = π)")

def test_variational_quantum_eigensolver():
    """Test VQE-style variational optimization."""
    print("\n\n🧬 Variational Quantum Eigensolver (VQE) Style")
    print("=" * 50)
    
    print("\n1. VQE ansatz for H₂ molecule simulation...")
    vqe_h2 = {
        "description": "VQE ansatz for hydrogen molecule",
        "steps": [
            {
                "step": 1,
                "action": "Create variational ansatz",
                "tool": "create_variational_circuit",
                "params": {
                    "num_qubits": 4,
                    "num_layers": 2,
                    "entanglement": "full",
                    "name": "h2_vqe_ansatz"
                }
            },
            {
                "step": 2,
                "action": "Analyze initial state",
                "tool": "analyze_statevector",
                "params": {"circuit_name": "h2_vqe_ansatz"}
            },
            {
                "step": 3,
                "action": "Add measurement for energy expectation",
                "tool": "add_gates",
                "params": {"gates": [{"type": "measure_all"}]}
            },
            {
                "step": 4,
                "action": "Optimize circuit",
                "tool": "optimize_circuit",
                "params": {"optimization_level": 2}
            },
            {
                "step": 5,
                "action": "Run multiple parameter sets",
                "note": "In practice, would iterate over different parameter values"
            }
        ]
    }
    print(f"   Implementation: {json.dumps(vqe_h2, indent=2)}")
    print("   Note: Parameter optimization would be done externally")

def test_quantum_approximate_optimization():
    """Test QAOA-style algorithm."""
    print("\n\n📊 Quantum Approximate Optimization Algorithm (QAOA)")
    print("=" * 50)
    
    print("\n1. QAOA for Max-Cut problem...")
    qaoa_maxcut = {
        "description": "QAOA circuit for 3-node Max-Cut",
        "steps": [
            {
                "step": 1,
                "action": "Create circuit",
                "tool": "create_quantum_circuit",
                "params": {"num_qubits": 3, "num_classical_bits": 3}
            },
            {
                "step": 2,
                "action": "Initialize superposition",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]},
                        {"type": "h", "qubits": [2]}
                    ]
                }
            },
            {
                "step": 3,
                "action": "Problem Hamiltonian (ZZ interactions)",
                "tool": "add_advanced_gates",
                "params": {
                    "gates": [
                        # ZZ rotations for edges (0,1), (1,2), (0,2)
                        {"type": "rzz", "qubits": [0, 1], "params": [0.5]},  # γ parameter
                        {"type": "rzz", "qubits": [1, 2], "params": [0.5]},
                        {"type": "rzz", "qubits": [0, 2], "params": [0.5]}
                    ]
                }
            },
            {
                "step": 4,
                "action": "Mixer Hamiltonian (X rotations)",
                "tool": "add_advanced_gates",
                "params": {
                    "gates": [
                        {"type": "rx", "qubits": [0], "params": [1.0]},  # β parameter
                        {"type": "rx", "qubits": [1], "params": [1.0]},
                        {"type": "rx", "qubits": [2], "params": [1.0]}
                    ]
                }
            },
            {
                "step": 5,
                "action": "Measure and run",
                "tool": "add_gates",
                "params": {"gates": [{"type": "measure_all"}]}
            },
            {
                "step": 6,
                "action": "Execute",
                "tool": "run_circuit",
                "params": {"shots": 1000}
            }
        ]
    }
    print(f"   Implementation: {json.dumps(qaoa_maxcut, indent=2)}")
    print("   Expected: Biased towards Max-Cut solutions like |101⟩ or |010⟩")

def test_quantum_fourier_sampling():
    """Test quantum Fourier sampling."""
    print("\n\n🌊 Quantum Fourier Sampling")
    print("=" * 50)
    
    print("\n1. Period finding with QFT...")
    qft_sampling = {
        "description": "Use QFT to find periodicity",
        "steps": [
            {
                "step": 1,
                "action": "Create register",
                "tool": "create_quantum_circuit",
                "params": {"num_qubits": 4, "num_classical_bits": 4}
            },
            {
                "step": 2,
                "action": "Initialize superposition",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "h", "qubits": [0]},
                        {"type": "h", "qubits": [1]},
                        {"type": "h", "qubits": [2]},
                        {"type": "h", "qubits": [3]}
                    ]
                }
            },
            {
                "step": 3,
                "action": "Apply periodic function (example: period 2)",
                "tool": "add_gates",
                "params": {
                    "gates": [
                        {"type": "x", "qubits": [0]},  # Flip every other state
                        {"type": "x", "qubits": [2]}
                    ]
                }
            },
            {
                "step": 4,
                "action": "Apply QFT",
                "tool": "implement_qft",
                "params": {"num_qubits": 4, "inverse": False}
            },
            {
                "step": 5,
                "action": "Measure",
                "tool": "add_gates",
                "params": {"gates": [{"type": "measure_all"}]}
            }
        ]
    }
    print(f"   Implementation: {json.dumps(qft_sampling, indent=2)}")
    print("   Expected: Enhanced probability at multiples of N/period")

def demo_algorithm_comparison():
    """Compare different quantum algorithms."""
    print("\n\n⚖️  Algorithm Comparison")
    print("=" * 50)
    
    algorithms = {
        "grover": {
            "qubits": "log₂(N) + O(1)",
            "depth": "O(√N)",
            "advantage": "Quadratic speedup for search",
            "classical_complexity": "O(N)"
        },
        "deutsch_jozsa": {
            "qubits": "n + 1",
            "depth": "O(1)",
            "advantage": "Exponential speedup (1 vs 2^(n-1) queries)",
            "classical_complexity": "O(2^n)"
        },
        "phase_estimation": {
            "qubits": "n + m (n counting, m eigenstate)",
            "depth": "O(2^n)",
            "advantage": "Efficient phase/eigenvalue estimation",
            "classical_complexity": "Difficult"
        },
        "vqe": {
            "qubits": "Problem dependent",
            "depth": "O(p) (p = circuit depth)",
            "advantage": "Near-term quantum advantage",
            "classical_complexity": "Exponential (exact)"
        },
        "qaoa": {
            "qubits": "n (problem size)",
            "depth": "O(p) layers",
            "advantage": "Approximate optimization",
            "classical_complexity": "NP-hard problems"
        }
    }
    
    print(f"Algorithm Comparison: {json.dumps(algorithms, indent=2)}")

if __name__ == "__main__":
    print("Qiskit MCP Server - Quantum Algorithms Test Guide")
    print("=" * 60)
    print("This script provides implementations of famous quantum algorithms")
    print("using the MCP server tools.")
    
    test_grover_algorithm()
    test_deutsch_jozsa()
    test_quantum_phase_estimation()
    test_variational_quantum_eigensolver()
    test_quantum_approximate_optimization()
    test_quantum_fourier_sampling()
    demo_algorithm_comparison()
    
    print("\n\n✅ Quantum Algorithms Guide Complete!")
    print("These examples show how to implement major quantum algorithms.")
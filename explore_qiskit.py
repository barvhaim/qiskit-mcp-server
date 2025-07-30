#!/usr/bin/env python3
"""
Comprehensive Qiskit exploration script to identify potential MCP server tools.
This script systematically explores Qiskit modules and identifies key functionality.
"""

import inspect
import sys
from typing import Dict, List, Any, Tuple
import json

def explore_module(module, module_name: str, max_depth: int = 2, current_depth: int = 0) -> Dict[str, Any]:
    """Explore a module and extract its structure."""
    if current_depth >= max_depth:
        return {}
    
    result = {
        "classes": {},
        "functions": {},
        "submodules": {},
        "constants": {}
    }
    
    try:
        for name in dir(module):
            if name.startswith('_'):
                continue
                
            try:
                obj = getattr(module, name)
                
                # Classes
                if inspect.isclass(obj) and obj.__module__.startswith('qiskit'):
                    class_info = {
                        "doc": inspect.getdoc(obj) or "No documentation",
                        "methods": [],
                        "properties": []
                    }
                    
                    # Get public methods
                    for method_name in dir(obj):
                        if not method_name.startswith('_'):
                            try:
                                method = getattr(obj, method_name)
                                if callable(method):
                                    sig = None
                                    try:
                                        sig = str(inspect.signature(method))
                                    except:
                                        sig = "signature_unavailable"
                                    
                                    class_info["methods"].append({
                                        "name": method_name,
                                        "signature": sig,
                                        "doc": inspect.getdoc(method) or "No documentation"
                                    })
                                elif isinstance(method, property):
                                    class_info["properties"].append({
                                        "name": method_name,
                                        "doc": inspect.getdoc(method) or "No documentation"
                                    })
                            except:
                                continue
                    
                    result["classes"][name] = class_info
                
                # Functions
                elif inspect.isfunction(obj) and obj.__module__.startswith('qiskit'):
                    try:
                        sig = str(inspect.signature(obj))
                    except:
                        sig = "signature_unavailable"
                    
                    result["functions"][name] = {
                        "signature": sig,
                        "doc": inspect.getdoc(obj) or "No documentation"
                    }
                
                # Submodules
                elif inspect.ismodule(obj) and obj.__name__.startswith('qiskit'):
                    if current_depth < max_depth - 1:
                        result["submodules"][name] = explore_module(
                            obj, f"{module_name}.{name}", max_depth, current_depth + 1
                        )
                
                # Constants and other objects
                elif not callable(obj) and not inspect.ismodule(obj):
                    result["constants"][name] = {
                        "type": type(obj).__name__,
                        "value": str(obj) if len(str(obj)) < 100 else f"{str(obj)[:100]}..."
                    }
                    
            except Exception as e:
                continue
                
    except Exception as e:
        print(f"Error exploring {module_name}: {e}")
    
    return result

def main():
    """Main exploration function."""
    print("Starting comprehensive Qiskit exploration...")
    
    # Import main Qiskit modules
    modules_to_explore = [
        'qiskit',
        'qiskit.circuit',
        'qiskit.quantum_info', 
        'qiskit.transpiler',
        'qiskit.primitives',
        'qiskit.providers',
        'qiskit.visualization',
        'qiskit.algorithms',
        'qiskit.opflow',
        'qiskit.pulse',
        'qiskit.extensions',
        'qiskit.utils'
    ]
    
    exploration_results = {}
    
    for module_name in modules_to_explore:
        print(f"\n=== Exploring {module_name} ===")
        try:
            module = __import__(module_name, fromlist=[''])
            print(f"Successfully imported {module_name}")
            
            # Get basic module info
            module_doc = inspect.getdoc(module) or "No documentation"
            print(f"Module documentation: {module_doc[:200]}...")
            
            # Explore the module
            exploration_results[module_name] = {
                "doc": module_doc,
                "structure": explore_module(module, module_name)
            }
            
        except ImportError as e:
            print(f"Could not import {module_name}: {e}")
            exploration_results[module_name] = {"error": str(e)}
        except Exception as e:
            print(f"Error exploring {module_name}: {e}")
            exploration_results[module_name] = {"error": str(e)}
    
    # Save detailed results
    with open('/Users/barha/Desktop/IBM/qiskit-mcp-server/qiskit_exploration.json', 'w') as f:
        json.dump(exploration_results, f, indent=2)
    
    print("\n" + "="*80)
    print("QISKIT MCP SERVER TOOL ANALYSIS")
    print("="*80)
    
    # Analyze and categorize potential tools
    potential_tools = {
        "Circuit Creation & Manipulation": [],
        "Quantum State Analysis": [],
        "Simulation & Execution": [],
        "Transpilation & Optimization": [],
        "Visualization": [],
        "Quantum Algorithms": [],
        "Measurement & Results": [],
        "Pulse Control": [],
        "Provider Management": [],
        "Utilities": []
    }
    
    # Circuit tools
    if 'qiskit.circuit' in exploration_results:
        circuit_module = exploration_results['qiskit.circuit']
        if 'structure' in circuit_module:
            classes = circuit_module['structure'].get('classes', {})
            functions = circuit_module['structure'].get('functions', {})
            
            # Key circuit classes
            important_classes = ['QuantumCircuit', 'QuantumRegister', 'ClassicalRegister', 'Gate', 'Instruction']
            for class_name in important_classes:
                if class_name in classes:
                    potential_tools["Circuit Creation & Manipulation"].append({
                        "type": "class",
                        "name": f"qiskit.circuit.{class_name}",
                        "description": classes[class_name]["doc"][:200] + "...",
                        "key_methods": [m["name"] for m in classes[class_name]["methods"][:5]]
                    })
            
            # Key circuit functions
            for func_name, func_info in functions.items():
                if any(keyword in func_name.lower() for keyword in ['circuit', 'gate', 'compose']):
                    potential_tools["Circuit Creation & Manipulation"].append({
                        "type": "function", 
                        "name": f"qiskit.circuit.{func_name}",
                        "signature": func_info["signature"],
                        "description": func_info["doc"][:200] + "..."
                    })
    
    # Quantum info tools
    if 'qiskit.quantum_info' in exploration_results:
        qi_module = exploration_results['qiskit.quantum_info']
        if 'structure' in qi_module:
            classes = qi_module['structure'].get('classes', {})
            functions = qi_module['structure'].get('functions', {})
            
            # Key quantum info classes
            important_classes = ['Statevector', 'DensityMatrix', 'Operator', 'Pauli', 'SparsePauliOp']
            for class_name in important_classes:
                if class_name in classes:
                    potential_tools["Quantum State Analysis"].append({
                        "type": "class",
                        "name": f"qiskit.quantum_info.{class_name}",
                        "description": classes[class_name]["doc"][:200] + "...",
                        "key_methods": [m["name"] for m in classes[class_name]["methods"][:5]]
                    })
    
    # Primitives for simulation
    if 'qiskit.primitives' in exploration_results:
        prim_module = exploration_results['qiskit.primitives']
        if 'structure' in prim_module:
            classes = prim_module['structure'].get('classes', {})
            
            # Key primitive classes
            important_classes = ['Sampler', 'Estimator', 'BackendSampler', 'BackendEstimator']
            for class_name in important_classes:
                if class_name in classes:
                    potential_tools["Simulation & Execution"].append({
                        "type": "class",
                        "name": f"qiskit.primitives.{class_name}",
                        "description": classes[class_name]["doc"][:200] + "...",
                        "key_methods": [m["name"] for m in classes[class_name]["methods"][:5]]
                    })
    
    # Transpiler tools
    if 'qiskit.transpiler' in exploration_results:
        trans_module = exploration_results['qiskit.transpiler']
        if 'structure' in trans_module:
            classes = trans_module['structure'].get('classes', {})
            functions = trans_module['structure'].get('functions', {})
            
            # Key transpiler functionality
            for func_name, func_info in functions.items():
                if 'transpile' in func_name.lower():
                    potential_tools["Transpilation & Optimization"].append({
                        "type": "function",
                        "name": f"qiskit.transpiler.{func_name}",
                        "signature": func_info["signature"],
                        "description": func_info["doc"][:200] + "..."
                    })
    
    # Visualization tools
    if 'qiskit.visualization' in exploration_results:
        viz_module = exploration_results['qiskit.visualization']
        if 'structure' in viz_module:
            functions = viz_module['structure'].get('functions', {})
            
            # Key visualization functions
            viz_functions = ['circuit_drawer', 'plot_histogram', 'plot_bloch_vector', 'plot_state_qsphere']
            for func_name in viz_functions:
                if func_name in functions:
                    potential_tools["Visualization"].append({
                        "type": "function",
                        "name": f"qiskit.visualization.{func_name}",
                        "signature": functions[func_name]["signature"],
                        "description": functions[func_name]["doc"][:200] + "..."
                    })
    
    # Print categorized analysis
    for category, tools in potential_tools.items():
        if tools:
            print(f"\n{category}:")
            print("-" * len(category))
            for tool in tools[:3]:  # Show top 3 per category
                print(f"  • {tool['name']} ({tool['type']})")
                if 'signature' in tool:
                    print(f"    Signature: {tool['signature']}")
                if 'key_methods' in tool and tool['key_methods']:
                    print(f"    Key methods: {', '.join(tool['key_methods'])}")
                print(f"    Description: {tool['description']}")
                print()
    
    print("\n" + "="*80)
    print("MCP TOOL RECOMMENDATIONS")
    print("="*80)
    
    recommendations = [
        {
            "tool_name": "create_quantum_circuit",
            "description": "Create a new quantum circuit with specified qubits and classical bits",
            "qiskit_class": "qiskit.circuit.QuantumCircuit",
            "example_usage": "create_quantum_circuit(num_qubits=3, num_clbits=3)"
        },
        {
            "tool_name": "add_gate_to_circuit", 
            "description": "Add quantum gates to a circuit (H, CNOT, RZ, etc.)",
            "qiskit_methods": "QuantumCircuit.h(), .cx(), .rz(), etc.",
            "example_usage": "add_gate_to_circuit(circuit_id, gate_type='h', qubit=0)"
        },
        {
            "tool_name": "simulate_circuit",
            "description": "Simulate a quantum circuit and get results",
            "qiskit_class": "qiskit.primitives.Sampler",
            "example_usage": "simulate_circuit(circuit_id, shots=1024)"
        },
        {
            "tool_name": "get_statevector",
            "description": "Get the statevector of a quantum circuit",
            "qiskit_class": "qiskit.quantum_info.Statevector",
            "example_usage": "get_statevector(circuit_id)"
        },
        {
            "tool_name": "transpile_circuit",
            "description": "Transpile circuit for specific backend or optimization",
            "qiskit_function": "qiskit.transpile",
            "example_usage": "transpile_circuit(circuit_id, optimization_level=2)"
        },
        {
            "tool_name": "visualize_circuit",
            "description": "Generate visual representation of quantum circuit",
            "qiskit_function": "qiskit.visualization.circuit_drawer",
            "example_usage": "visualize_circuit(circuit_id, output='mpl')"
        },
        {
            "tool_name": "analyze_quantum_state",
            "description": "Analyze properties of quantum states (entanglement, fidelity, etc.)",
            "qiskit_module": "qiskit.quantum_info",
            "example_usage": "analyze_quantum_state(state, properties=['entanglement', 'purity'])"
        }
    ]
    
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec['tool_name']}")
        print(f"   Description: {rec['description']}")
        print(f"   Qiskit backing: {rec.get('qiskit_class', rec.get('qiskit_function', rec.get('qiskit_module', 'Multiple')))}")
        print(f"   Example: {rec['example_usage']}")
        print()
    
    print("Detailed exploration saved to: qiskit_exploration.json")

if __name__ == "__main__":
    main()
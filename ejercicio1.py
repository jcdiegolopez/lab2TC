from afd import AFD


afd1 = AFD([], [], '', [], {})
afd1.loadNewAFN(0, 'maquinas/afd.json')
print(afd1.final_state("A", "11222"))
print(afd1.is_accepted("A", "11222"))
print(afd1.derivation("A", "11222"))

afd2 = AFD([], [], '', [], {})
afd2.loadNewAFN(1, 'maquinas/afd.json')
print(afd2.final_state("S0", "abba"))
print(afd2.is_accepted("S0", "abba"))
print(afd2.derivation("S0", "abba"))

print("Derivaciones del ejercicio 2B:")
afdEj2 = AFD([], [], '', [], {})
afdEj2.loadNewAFN(2, 'maquinas/afd.json')
print(afdEj2.derivation("A", "+0.1234567"))
print(afdEj2.derivation("A", "9273."))
print(afdEj2.derivation("A", "2025.333"))

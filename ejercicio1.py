from afd import AFD


afd1 = AFD([], [], '', [], {})
afd1.readJson('maquinas/afd1.json')
print(afd1.final_state("A", "11222"))
print(afd1.is_accepted("A", "11222"))
print(afd1.derivation("A", "11222"))

afd2 = AFD([], [], '', [], {})
afd2.readJson('maquinas/afd2.json')
print(afd2.final_state("S0", "abba"))
print(afd2.is_accepted("S0", "abba"))
print(afd2.derivation("S0", "abba"))

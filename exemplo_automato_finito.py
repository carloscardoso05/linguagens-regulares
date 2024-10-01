from automato_finito import AutomatoFinitoDeterministico
from enum import Enum

Estados = Enum("Estados", ["q0", "q1", "q2", "q3"])

# a(a|b)*ba
adf: AutomatoFinitoDeterministico = AutomatoFinitoDeterministico(
    set(Estados),
    {"a", "b"},
    {
        Estados.q0: {"a": Estados.q1},
        Estados.q1: {"a": Estados.q1, "b": Estados.q2},
        Estados.q2: {"a": Estados.q3, "b": Estados.q2},
        Estados.q3: {"a": Estados.q1, "b": Estados.q2},
    },
    Estados.q0,
    {Estados.q3},
)

adf.verbose = True
adf.interactive = True

print(adf.valida_cadeia("aaaabbcabbbcacc"), end="\n\n")
# print(adf.valida_cadeia("aaaaaaaba"), end="\n\n")
# print(adf.valida_cadeia("aba"), end="\n\n")
# print(adf.valida_cadeia("ba"), end="\n\n")
# print(adf.valida_cadeia("ab"), end="\n\n")
# print(adf.valida_cadeia("abbabababa"), end="\n\n")

from automato_finito import AutomatoFinito, Transicao
from enum import Enum

Estados = Enum("Estados", ["q0", "q1", "q2"])

# a[ab](ba)?
adf: AutomatoFinito = AutomatoFinito(
    set(Estados),
    {"a", "b", "c"},
    {
        Transicao(Estados.q0, "a", Estados.q1),
        Transicao(Estados.q1, "a", Estados.q1),
        Transicao(Estados.q1, "b", Estados.q1),
        Transicao(Estados.q1, "c", Estados.q2),
        Transicao(Estados.q2, "c", Estados.q2),
        Transicao(Estados.q2, "a", Estados.q1),
    },
    Estados.q0,
    {Estados.q0, Estados.q1, Estados.q2},
)

print(adf.valida_cadeia([c for c in "aaaabbcabbbcacc"], verbose=True))

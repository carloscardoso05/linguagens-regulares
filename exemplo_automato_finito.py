from automato_finito import AutomatoFinito, Transicao
from enum import Enum

Estados = Enum("Estados", ["q0", "q1", "q2", "q3", "q4"])

# a[ab](ba)?
adf: AutomatoFinito = AutomatoFinito(
    set(Estados),
    {"a", "b"},
    {
        Transicao(Estados.q0, "a", Estados.q1),
        Transicao(Estados.q0, "", Estados.q2),
        Transicao(Estados.q1, "a", Estados.q2),
        Transicao(Estados.q1, "b", Estados.q2),
        Transicao(Estados.q2, "b", Estados.q3),
        Transicao(Estados.q3, "a", Estados.q4),
    },
    Estados.q0,
    {Estados.q2, Estados.q4},
)

print(adf.valida_cadeia([c for c in "ba"], verbose=True))

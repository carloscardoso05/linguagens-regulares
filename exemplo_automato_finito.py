from automato_finito import AutomatoFinitoDeterministico, Transicao
from enum import Enum

Estados = Enum("Estados", ["q0", "q1", "q2", "q3"])

# a(a|b)*ba
adf: AutomatoFinitoDeterministico = AutomatoFinitoDeterministico(
    set(Estados),
    {"a", "b"},
    {
        Transicao(Estados.q0, "a", Estados.q1),
        Transicao(Estados.q1, "a", Estados.q1),
        Transicao(Estados.q1, "b", Estados.q2),
        Transicao(Estados.q2, "a", Estados.q3),
        Transicao(Estados.q2, "b", Estados.q2),
        Transicao(Estados.q3, "a", Estados.q1),
        Transicao(Estados.q3, "b", Estados.q2),
    },
    Estados.q0,
    {Estados.q3},
)

print(adf.valida_cadeia("aaaabbcabbbcacc", verbose=True), end="\n\n")
print(adf.valida_cadeia("aaaaaaaba", verbose=True), end="\n\n")
print(adf.valida_cadeia("aba", verbose=True), end="\n\n")
print(adf.valida_cadeia("ba", verbose=True), end="\n\n")
print(adf.valida_cadeia("ab", verbose=True), end="\n\n")
print(adf.valida_cadeia("abbabababa", verbose=True), end="\n\n")

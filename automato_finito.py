from validadores import (
    checa_conjunto_vazio,
    checa_conjunto_contem,
    checa_eh_subconjunto,
)
from dataclasses import dataclass
from typing import Set, TypeAlias, cast, Dict
from enum import Enum

Estado: TypeAlias = Enum


@dataclass(frozen=True, eq=True)
class Transicao:
    estado_inicial: Estado
    simbolo: str
    estado_final: Estado


@dataclass
class AutomatoFinitoDeterministico:
    estados: Set[Estado]
    alfabeto: Set[str]
    funcao_de_transicao: Dict[Estado, Dict[str, Estado]]
    estado_inicial: Estado
    estados_finais: Set[Estado]

    def __post_init__(self) -> None:
        self.estado_atual = self.estado_inicial
        self.__checa_eh_valido()

    def valida_cadeia(self, cadeia: str, verbose: bool = False) -> bool:
        if cadeia is None:
            raise Exception("Defina uma cadeia (vazia ou não) para validar")

        estado_atual: Estado = self.estado_inicial
        cursor: int = 0
        while True:
            prox_char: str = cadeia[cursor] if len(cadeia) > 0 else ""

            if estado_atual not in self.funcao_de_transicao:
                
            prox_estado: Estado = self.funcao_de_transicao[estado_atual][prox_char]


            if len(cadeia) == 0:
                return estado_atual in self.estados_finais

        return False

    def __checa_eh_valido(self) -> None:
        checa_conjunto_vazio(self.alfabeto, "Alfabeto")
        checa_eh_subconjunto(
            self.estados, "Estados", self.estados_finais, "Estados finais"
        )
        checa_conjunto_contem(
            self.estados, "Estados", self.estado_inicial, "Estado inicial"
        )
        checa_eh_subconjunto(
            self.alfabeto,
            "Alfabeto",
            set(map(lambda t: cast(Transicao, t).simbolo, self.funcao_de_transicao)),
            "transições",
        )

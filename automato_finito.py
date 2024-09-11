from validadores import (
    checa_conjunto_vazio,
    checa_conjunto_contem,
    checa_eh_subconjunto,
)
from dataclasses import dataclass
from typing import Set, TypeAlias
from enum import Enum

Estado: TypeAlias = Enum


@dataclass(frozen=True, eq=True)
class Transicao:
    estado_inicial: Estado
    simbolo: str
    estado_final: Estado


@dataclass
class AutomatoFinito:
    estados: Set[Estado]
    alfabeto: Set[str]
    funcao_de_transicao: Set[Transicao]
    estado_inicial: Estado
    estados_finais: Set[Estado]

    def __post_init__(self) -> None:
        self.__checa_eh_valido()

    def valida_cadeia(self, cadeia: str, verbose: bool = False) -> bool:
        # def consumir() -> str:
        #     nonlocal cadeia
        #     cadeia = cadeia[1:]
        #     return cadeia[0]
        

        return False
    

    def __checa_eh_valido(self) -> None:
        checa_conjunto_vazio(self.alfabeto, "Alfabeto")
        checa_eh_subconjunto(
            self.estados, "Estados", self.estados_finais, "Estados finais"
        )
        checa_conjunto_contem(
            self.estados, "Estados", self.estado_inicial, "Estado inicial"
        )

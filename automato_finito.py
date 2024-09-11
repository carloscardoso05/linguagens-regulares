from validadores import (
    checa_conjunto_vazio,
    checa_conjunto_contem,
    checa_eh_subconjunto,
)
from dataclasses import dataclass, field
from typing import Set, TypeAlias, List, Optional, cast
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

    estado_atual: Estado = field(init=False)
    cadeia: Optional[str] = field(init=False, default=None)

    def __post_init__(self) -> None:
        self.estado_atual = self.estado_inicial
        self.__checa_eh_valido()

    # def consumir(self) -> None:
    #     self.__checa_cadeia_nao_definida()
    #     cadeia: str = cast(str, self.cadeia)
    #     prox

    def valida_cadeia(self, verbose: bool = False) -> bool:
        if self.cadeia is None:
            raise Exception("Defina uma cadeia (vazia ou não) para validar")

        return False

    def __checa_eh_valido(self) -> None:
        checa_conjunto_vazio(self.alfabeto, "Alfabeto")
        checa_eh_subconjunto(
            self.estados, "Estados", self.estados_finais, "Estados finais"
        )
        checa_conjunto_contem(
            self.estados, "Estados", self.estado_inicial, "Estado inicial"
        )

    def __checa_cadeia_nao_definida(self) -> None:
        if self.cadeia is None:
            raise Exception("Defina uma cadeia (vazia ou não) para validar")

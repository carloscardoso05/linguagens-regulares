from validadores import (
    checa_conjunto_vazio,
    checa_conjunto_contem,
    checa_eh_subconjunto,
)
from dataclasses import dataclass
from typing import Set, TypeAlias, List, Deque, Tuple, cast
from enum import Enum
from collections import deque

Estado: TypeAlias = Enum


@dataclass(frozen=True, eq=True)
class Transicao:
    estado_inicial: Estado
    simbolo: str
    estado_final: Estado


@dataclass(frozen=True, eq=True)
class AutomatoSnapshot:
    estado_atual: Estado
    cadeia: Tuple[str, ...]
    cursor: int

    def simbolo_atual(self) -> str:
        return self.cadeia[self.cursor] if self.cursor < len(self.cadeia) else ""


@dataclass
class AutomatoFinito:
    estados: Set[Estado]
    alfabeto: Set[str]
    funcao_de_transicao: Set[Transicao]
    estado_inicial: Estado
    estados_finais: Set[Estado]

    def __post_init__(self) -> None:
        self.estado_atual = self.estado_inicial
        self.__checa_eh_valido()

    def aplicar_transicoes(
        self, snapshot: AutomatoSnapshot, verbose: bool = False
    ) -> Set[AutomatoSnapshot]:
        snapshots: Set[AutomatoSnapshot] = set()
        for transicao in self.funcao_de_transicao:
            if (
                snapshot.estado_atual == transicao.estado_inicial
                and transicao.simbolo
                in [
                    "",
                    snapshot.simbolo_atual(),
                ]
            ):
                if verbose:
                    print(
                        f"Consome: '{transicao.simbolo}' e vai para {transicao.estado_final.name}"
                    )
                cursor_desloc: int = 1 if transicao.simbolo else 0
                snapshots.add(
                    AutomatoSnapshot(
                        transicao.estado_final,
                        snapshot.cadeia,
                        snapshot.cursor + cursor_desloc,
                    )
                )
        return snapshots

    def valida_cadeia(self, cadeia: List[str], verbose: bool = False) -> bool:
        if cadeia is None:
            raise Exception("Defina uma cadeia (vazia ou não) para validar")

        pilha_snapshots: Deque[AutomatoSnapshot] = deque()
        pilha_snapshots.append(AutomatoSnapshot(self.estado_inicial, tuple(cadeia), 0))

        while pilha_snapshots:
            snapshot: AutomatoSnapshot = pilha_snapshots.pop()
            if verbose:
                print(
                    f"Estado atual: {snapshot.estado_atual.name}. Cadeia: {snapshot.cadeia[snapshot.cursor:]}"
                )
            if (
                snapshot.estado_atual in self.estados_finais
                and snapshot.simbolo_atual() == ""
            ):
                return True
            prox_snapshots = self.aplicar_transicoes(snapshot, verbose=verbose)
            for snapshot in prox_snapshots:
                pilha_snapshots.append(snapshot)

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

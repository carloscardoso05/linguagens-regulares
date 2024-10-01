from validadores import (
    checa_conjunto_vazio,
    checa_conjunto_contem,
    checa_eh_subconjunto,
)
from dataclasses import dataclass
from typing import Set, TypeAlias, Dict
from enum import Enum
import sys

Estado: TypeAlias = Enum


@dataclass
class AutomatoFinitoDeterministico:
    estados: Set[Estado]
    alfabeto: Set[str]
    funcao_de_transicao: Dict[Estado, Dict[str, Estado]]
    estado_inicial: Estado
    estados_finais: Set[Estado]
    verbose: bool = False
    interactive: bool = False

    def __post_init__(self) -> None:
        self.estado_atual = self.estado_inicial
        self.__checa_eh_valido()

    def valida_cadeia(self, cadeia: str) -> bool:
        if cadeia is None:
            raise Exception("Defina uma cadeia (vazia ou não) para validar")

        estado_atual: Estado = self.estado_inicial
        cursor: int = 0
        while cursor < len(cadeia):
            self.__print_config(cadeia, cursor, estado_atual)

            char: str = cadeia[cursor]

            if estado_atual not in self.funcao_de_transicao:
                self.__print_config(
                    cadeia,
                    cursor,
                    estado_atual,
                    f"Cadeia rejeitada. Sem transições disponíveis no estado {estado_atual}",
                )
                return False

            if char not in self.funcao_de_transicao[estado_atual]:
                self.__print_config(
                    cadeia,
                    cursor,
                    estado_atual,
                    f"Cadeia rejeitada. Sem transições disponíveis no estado {estado_atual}",
                )
                return False

            estado_atual = self.funcao_de_transicao[estado_atual][char]
            cursor += 1

        aceita = estado_atual in self.estados_finais
        self.__print_config(
            cadeia, cursor, estado_atual, "Aceita" if aceita else "Rejeitada"
        )
        return aceita

    def __print_config(self, cadeia: str, cursor: int, estado: Estado, msg: str = ""):
        if not self.verbose:
            return

        # Clear the previous output

        output_lines = [
            f"Cadeia:   {cadeia}",
            f"{'|'.rjust(cursor + 12)}",
            f"Caractere: {(cadeia[cursor] if cursor < len(cadeia) else '').rjust(cursor + 1)}",
            f"Estado: {estado}",
            f"Inicial: {'Sim' if estado == self.estado_inicial else 'Não'}",
            f"Final: {'Sim' if estado in self.estados_finais else 'Não'}",
            msg,
        ]

        # Print the new output
        for line in output_lines:
            print(line)

        if self.interactive:
            input()
            sys.stdout.write("\033[F" * 8)  # Move the cursor up 6 lines
            sys.stdout.write("\033[K" * 8)  # Clear the line

    def __checa_eh_valido(self) -> None:
        pass
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
            set(map(lambda t: list(t.keys())[0], self.funcao_de_transicao.values())),
            "transições",
        )

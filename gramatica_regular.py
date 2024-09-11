from typing import Set, Optional, cast, List
from dataclasses import dataclass, field
from queue import Queue
from validadores import (
    checa_conjunto_vazio,
    checa_conjunto_contem,
    checa_eh_subconjunto,
)


@dataclass(eq=True, frozen=True)
class Producao:
    inicio: str
    fim: str

    def aplicar(self, cadeia: str) -> str:
        return cadeia.replace(self.inicio, self.fim, 1)


@dataclass
class GramaticaRegular:
    "Classe para representar uma gramática regular"

    vocabulario: Set[str]
    terminais: Set[str]
    nao_terminais: Set[str] = field(init=False)
    producoes: Set[Producao]
    raiz: str

    def __post_init__(self) -> None:
        """Método chamado após a instanciação"""
        self.__checa_eh_valida()

    def gerar_cadeias(self, limite: int) -> List[str]:
        """Gera cadeias a partir das produções até o limite definido

        Args:
            limite (int): quantidade de cadeias para serem geradas

        Returns:
            List[str]: lista de cadeias geradas
        """
        cadeias: List[str] = []
        cadeias_hist: Set[str] = set()
        fila: Queue = Queue()
        fila.put(self.raiz)
        while cadeia := cast(Optional[str], fila.get()):
            if cadeia in cadeias_hist:
                continue
            cadeias_hist.add(cadeia)
            for producao in self.producoes:
                if producao.inicio not in cadeia:
                    continue
                nova_cadeia = producao.aplicar(cadeia)
                fila.put(nova_cadeia)
                cadeias.append(nova_cadeia)
                if len(cadeias) == limite:
                    return cadeias
        return cadeias

    def gerar_sentencas(self, limite: int) -> Set[str]:
        """Gera sentenças a partir das produções até o limite definido

        Args:
            limite (int): quantidade de sentenças para serem geradas

        Returns:
            Set[str]: lista de sentenças geradas
        """
        sentencas: Set[str] = set()
        cadeias_hist: Set[str] = set()
        fila: Queue = Queue()
        fila.put(self.raiz)
        while cadeia := cast(Optional[str], fila.get()):
            if cadeia in cadeias_hist:
                continue
            cadeias_hist.add(cadeia)
            for producao in self.producoes:
                nova_cadeia = producao.aplicar(cadeia)
                fila.put(nova_cadeia)
                if self.cadeia_eh_final(nova_cadeia):
                    sentencas.add(nova_cadeia)
                if len(sentencas) == limite:
                    return sentencas
        return sentencas

    def cadeia_eh_final(self, cadeia: str) -> bool:
        """Checa se a cadeia é final

        Args:
            cadeia (str): cadeia para ser checada

        Returns:
            bool: se é final
        """
        return all(simbolo in self.terminais for simbolo in cadeia)

    def __checa_eh_valida(self) -> None:
        """Checa se a gramática é válida"""
        checa_conjunto_vazio(self.vocabulario, "Vocabulário")
        checa_conjunto_vazio(self.terminais, "Terminais")
        checa_conjunto_vazio(self.producoes, "Produções")
        checa_eh_subconjunto(
            self.vocabulario, "Vocabulário", self.terminais, "Terminais"
        )
        checa_conjunto_contem(self.vocabulario, "Vocabulário", self.raiz, "raiz")

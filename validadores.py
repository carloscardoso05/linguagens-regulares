from typing import Set, TypeVar

T = TypeVar("T")


def checa_conjunto_vazio(conjunto: Set[T], nome: str = "") -> None:
    """Checa se um conjunto é vazio

    Args:
        conjunto (Set): conjunto para ser checado
        nome (Optional[str]): nome do conjunto para melhor descrição da exceção. Defaults to "".

    Raises:
        Exception: se o conjunto for vazio
    """
    if len(conjunto) == 0:
        raise Exception(f"Conjunto {nome} está vazio: {conjunto}")


def checa_eh_subconjunto(
    conjunto: Set[T], nome_conjunto: str, subconjunto: Set[T], nome_subconjunto: str
) -> None:
    if not subconjunto.issubset(conjunto):
        restantes: Set = subconjunto - conjunto
        raise Exception(f"O conjunto {nome_subconjunto} deve ser subconjunto de {nome_conjunto}:\n\
                            {nome_subconjunto}: {subconjunto}\n\
                            {nome_conjunto}: {conjunto}\n\
                            Elementos fora de {nome_conjunto}: {restantes}")


def checa_conjunto_contem(
    conjunto: Set[T], nome_conjunto: str, elemento: T, nome_elemento: str
) -> None:
    if elemento not in conjunto:
        raise Exception(f"O conjunto {nome_conjunto} conter {nome_elemento} '{elemento}':\n\
                            {nome_conjunto}: {conjunto}\n\
                            {nome_elemento}: {elemento}")

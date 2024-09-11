from gramatica_regular import GramaticaRegular, Producao

gramatica = GramaticaRegular(
    {"a", "b", "A", "S"},
    {"a", "c"},
    {Producao("S", "A"), Producao("A", "aA"), Producao("A", "b")},
    "S",
)

c = gramatica.gerar_cadeias(15)
print(c)
s = gramatica.gerar_sentencas(15)
print("\n", s)
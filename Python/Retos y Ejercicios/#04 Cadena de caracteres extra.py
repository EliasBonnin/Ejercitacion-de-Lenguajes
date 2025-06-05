# Ejercicio 04* Extra
# En el siguiente URL https:/python.org Tenemos la documentacion de phyton.
# Los retos se encuentran en https://retosdeprogramacion.com

# Funcion


def Check(Palabra1, Palabra2: str):

    # Palindromo

    print(f"{Palabra1} es un palindromo? {Palabra1 == Palabra1[::-1]}")  # Con el slider el inverso de la palabra
    print(f"{Palabra2} es un palindromo? {Palabra2 == Palabra2[::-1]}")

    # Anagrama

    print(f"{Palabra1} es un anagrama? {sorted(Palabra1) == sorted(Palabra2)}")

    # Isograma

    def isograma(Palabra: str) -> bool:

        dic_palabras = dict()
        for Palabra in Palabra2:
            dic_palabras[Palabra] = dic_palabras.get(Palabra, 0) + 1

        isograma = True
        Valores_dic = list(dic_palabras.values())
        len_isograma = Valores_dic[0]
        for Palabra_count in Valores_dic:
            if Palabra_count != len_isograma:
                isograma = False
                break

        return isograma

    print(f"{Palabra1} es un isograma? {isograma(Palabra1)}")
    print(f"{Palabra2} es un isograma? {isograma(Palabra2)}")


Check("radar", "phytonphytonphytonphyton")
# Check("amor", "roma")

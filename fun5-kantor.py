def kantor(waluta):
    print("Uruchomienie katoru")

    def usd(kwota):
        print(f"Wymieniam {kwota} usd, mam {kwota * 4.06:.2f} PLN")

    def eur(kwota):
        print(f"Wymieniam {kwota} eur, mam {kwota * 4.14:.2f} PLN")

    if waluta.lower().replace(" ", "") == 'eur':
        return eur
    else:
        return usd


kantor_eur = kantor('eur')
print(kantor_eur)  # <function kantor.<locals>.eur at 0x100ef4e00>
kantor_eur(1000)  # Wymieniam 1000 eur, mam 4140.00 PLN

# dodać możliwośc przekazywania kwoty do wymiany
# ładnie wypisywac:
# Wymieniam 100 eur, mam 414 pln
kantor_usd = kantor('usd')
kantor_usd(1000)  # Wymieniam 1000 usd, mam 4060.00 PLN
# 13:20

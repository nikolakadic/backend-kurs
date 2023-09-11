"""
Zbir cifara broja
"""


def zbir_cifara_broja(broj):
    """
    Sabira cifre broja
    """
    zbir = 0
    while broj != 0:
        zbir += broj % 10
        broj = broj // 10
    return zbir


print(zbir_cifara_broja(112))

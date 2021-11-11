#!/usr/bin/env python3
"""
Script principal

Par: Genevieve Trudel
"""
import time


def bonjour(name):
    """
    Pour saluer.
    :param name: Nom de la personne à saluer.
    """
    print(f'Bonjour, {name}')


def compter(maxi, secs=0.25):
    """
    Fonction pour compter
    :param maxi: nombre a compter
    :param secs: nombre de seconde
    """
    print(f"Je sais compter jusqu'à {maxi}:",
          end=' ', flush=True)
    for i in range(1, maxi + 1):
        time.sleep(secs)  # un quart de seconde
        print(i, end=' ', flush=True)
    print()


def main():
    """
    Fonction principale du script
    """
    bonjour('Genevieve T.')
    compter(5)
    compter(10)


if __name__ == '__main__':
    main()

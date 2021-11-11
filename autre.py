#!/usr/bin/env python3
"""
Autre script pour appeler les fonctions
du script principal.

Par: Genevieve Trudel
"""
# Importer le module main (fichiewr main.py).
# On le renomme bonjour pour éviter le conflit
# de nom avec la fonction main plus bas.
import main as bonjour


def main():
    """
    Fonction principale du script
    """
    bonjour.bonjour('Genevieve T. alias GT')
    bonjour.compter(8, 0.5)


if __name__ == '__main__':
    main()

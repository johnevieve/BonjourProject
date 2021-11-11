#!/usr/bin/env python3
"""
Autre script pour appeler les fonctions
du script principal 2.

Par: Genevieve Trudel
"""
# Importer directement les fonctions.
from main import bonjour, compter


def main():
    """
    Fonction principale du script
    """
    bonjour('Genevieve T.')
    compter(3)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

# Importer le module main (fichiewr main.py).
# On le renomme bonjour pour éviter le conflit
# de nom avec la fonction main plus bas.
import main as bonjour


def main():
    bonjour.print_hi('Genevieve T.')
    bonjour.compter(8)


if __name__ == '__main__':
    main()

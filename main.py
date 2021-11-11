#!/usr/bin/env python3

import time


def bonjour(name):
    print(f'Bonjour, {name}')


def compter(maxi, secs=0.25):
    print(f"Je sais compter jusqu'à {maxi}:",
          end=' ', flush=True)
    for i in range(1, maxi + 1):
        time.sleep(secs)  # un quart de seconde
        print(i, end=' ', flush=True)
    print()


def main():
    bonjour('Genevieve T.')
    compter(5)
    compter(10)


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:08:09 2024

@author: nik-f
"""

import random

def main():
    matriz1 = [[random.randint(0, 1) for _ in range(10)] for _ in range(8)]
    
    gen=int(input("Numero de generaciones: "))
    for a in range(gen):
        print("Generación ", a+1)
        print("--------------Población Inicial--------------")
        for i in range(8):
            # Fórmula: -30x^2 - 23x + 5
            temp1 = int(''.join(map(str, matriz1[i])), 2)
            temp2 = -30 * (temp1**2) - (temp1 * 23) + 5
            print(f"{i+1}) {''.join(map(str, matriz1[i]))} = {temp2}")
        
        corte = calcular_punto_cruce()
        matriz2 = generar_pares_poblacion()
        matriz1 = generar_nueva_poblacion(matriz1, matriz2, corte)
        print("--------------Nueva Población--------------")
        for i in range(8):
            temp1 = int(''.join(map(str, matriz1[i])), 2)
            temp2 = -30 * (temp1**2) - (temp1 * 23) + 5
            print(f"{i + 1}) {''.join(map(str, matriz1[i]))} = {temp2}")

        matriz1 = aplicar_mutacion(matriz1)
        
        for i in range(8):
            temp1 = int(''.join(map(str, matriz1[i])), 2)
            temp2 = -30 * (temp1**2) - (temp1 * 23) + 5
            print(f"{i + 1}) {''.join(map(str, matriz1[i]))} = {temp2}")

def calcular_punto_cruce():
    while True:
        num = int(random.randint(1, 9))
        if 1 <= num <= 9:
            corte = 10 - num
            print("Punto de Cruce:", num)
            return corte
        else:
            print("El número no está dentro del rango...")

def generar_pares_poblacion():
    matriz2 = [[0, 0] for _ in range(4)]
    print("--------------Pares de Población--------------")
    for i in range(4):
        for j in range(2):
            while True:
                num = int(random.randint(1, 8))
                if 1 <= num <= 8 and num not in [x for sublist in matriz2 for x in sublist]:
                    matriz2[i][j] = num
                    break
            print(f"Par {i+1}): {matriz2[i]}")
    return matriz2

def generar_nueva_poblacion(matriz1, matriz2, corte):
    nueva_poblacion = []
    for parejay in range(4):
        pareja1, pareja2 = matriz2[parejay]
        for x in range(corte, 6):
            matriz1[pareja1-1][x], matriz1[pareja2-1][x] = matriz1[pareja2-1][x], matriz1[pareja1-1][x]
    return matriz1

def aplicar_mutacion(matriz1):
    print("--------------Mutación--------------")
    xr = random.randint(0, 7)
    yr = random.randint(0, 7)
    print(f"---Se realizó una mutación en la posición [{yr}][{xr}]")
    matriz1[yr][xr] = 1 if matriz1[yr][xr] == 0 else 0
    return matriz1

main()

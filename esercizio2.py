import numpy as np

# crea la matrice 5x5
matrice = np.arange(1, 26).reshape((5, 5))
print("Matrice 5x5:")
print(matrice)

# estrae la seconda colonna (indice 1)
seconda_colonna = matrice[:, 1]
print("\nSeconda colonna:")
print(seconda_colonna)

# estrae la terza riga (indice 2)
terza_riga = matrice[2, :]
print("\nTerza riga:")
print(terza_riga)

# calcola la somma degli elementi della diagonale principale
somma_diagonale = np.trace(matrice)
print("\nSomma della diagonale principale:")
print(somma_diagonale)

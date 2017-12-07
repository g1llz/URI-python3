def imprime_matriz():
  if c < tam_mat-1:
    print('{:>{}d} '.format(matriz[l][c], espacos), end = "")
  else:
    print('{:>{}d} '.format(matriz[l][c], espacos).rstrip(" "), end = "")
while True:
  tam_mat = int(input())
  if tam_mat > 0:
    matriz = [[0] * tam_mat for q in range(tam_mat)]
    espacos = len(str((2 ** (tam_mat-1)) ** 2))
    for x in range(tam_mat):
        for y in range(tam_mat):
            matriz[y][x] = (2 ** x) * (2 ** y)
    for l in range(tam_mat):
        for c in range(tam_mat):
           imprime_matriz()
        print("")
    print("")
  else:
    break
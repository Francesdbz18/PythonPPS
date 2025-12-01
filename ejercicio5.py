cantidad = 5
for n in range(cantidad):
    print("La cantidad es: ", n)

def contar(n):
    for i in range(n):
        print("Contando: ", i)

contar(3)
contar(5)

def raiz_cuadrada(m):
    raiz = m/2
    for _ in range(20):
        raiz = (1/2)*(raiz + (m / raiz))
    return raiz

print(raiz_cuadrada(9))
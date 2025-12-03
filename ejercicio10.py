class Estudiante:
    def __init__(self, nombre, dni) -> None:
        self.lista_notas = []
        self.nombre = nombre
        self.dni = dni
    def cambiar_nombre(self, nuevo_nombre: str):
        self.nombre = nuevo_nombre
    def anadir_nota(self, nota):
        valor = float(nota)
        if not (0.0 <= valor <= 10.0):
            raise ValueError("La nota debe estar entre 0 y 10")
        self.lista_notas.append(valor)
    def nota_media(self):
        if not self.lista_notas:
            return None
        return sum(self.lista_notas) / len(self.lista_notas)
from ejercicio10 import Estudiante

juan = Estudiante("Juan Perez", "12345678A")
print (juan.nombre)
juan.cambiar_nombre("PEPE")
print(juan.nombre)
juan.anadir_nota(5.0)
juan.anadir_nota(7.5)
juan.anadir_nota(9.0)
print(f"La nota media de {juan.nombre} es {juan.nota_media():.2f}")

from conexion import Conexion

class Productos:

    def __init__(self):
        self.conexion=Conexion()
    
    def listarProductos(self):
        query="select * from productos"
        result=self.conexion.ejecutar_query(query)
        filas=result.fetchall()
        print()
        for fila in filas:
            print(fila[1])
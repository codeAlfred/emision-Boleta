from conexion import Conexion

class Boleta:

    def __init__(self):
        self.conexion=Conexion()

# listara las boletas que sean de la fecha ingresada
    def listarVentas(self,fechaBoleta):
        query=f'select * from mydb.boleta where fechaBoleta="{fechaBoleta}"'
       
        resultado=self.conexion.ejecutar_query(query)
        filas = resultado.fetchall()
        print(filas)

# imprimira los productos de una boleta ingresando el id de la boleta
    def listarBoleta(self,idBoleta):
        query=f'select productos.nombreProducto from productos inner join detalle on productos.idProducto=detalle.PRODUCTOS_idProductos where detalle.BOLETA_idBoleta={idBoleta}'
        resultado=self.conexion.ejecutar_query(query)
        filas = resultado.fetchall()
        print("---------------------------")
        for fila in filas:
            print(fila[0])
# listar las boletas
from boleta import Boleta
from productos import Productos

obj=Boleta()
# fecha para buscar boletas
listarBoleta='2020-01-13'
obj.listarVentas(listarBoleta)

# llamar al metodo para listar los productos
product=Productos()
product.listarProductos()
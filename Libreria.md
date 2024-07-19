# Libreria uan
Se quiere crear un programa que permita administrar una tienda de libros. La tienda tiene un catálogo de libros, que son los libros que desea poner a la venta. La aplicación permite abastecer la tienda con ejemplares de los libros del catálogo y venderlos. Adicionalmente permite saber cuánto dinero se tiene en caja, empezando con una inversión inicial de $1.000.000.
De cada libro se conoce:
- ISBN. Identificador del libro. No pueden existir dos libros en la tienda con el mismo ISBN.
- Título. El nombre del libro.
- Precio de compra: Valor pagado por la compra de cada ejemplar en la tienda.
- Precio de venta: Valor por el cual se vende cada ejemplar del libro.
- Cantidad actual. Cantidad actual de ejemplares que tiene la tienda. Solo puede ser modificada mediante la venta o abastecimiento.
Adicionalmente, de cada libro se conoce todas las transacciones que se han realizado sobre él. De cada transacción se conoce:
- El tipo de transacción. Puede ser venta o abastecimiento.
- La fecha de realización.
- La cantidad de ejemplares incluidos en la transacción.

El abastecimiento de libros permite aumentar la cantidad actual de ejemplares del libro y registrar una transacción de tipo abastecimiento.
La venta de libros permite disminuir la cantidad actual de ejemplares del libro y registrar una transacción de venta. Esta transacción solo se podrá realizar si la cantidad actual de ejemplares es mayor a la cantidad que se quiere vender.
> El programa debe permitir al usuario:

1. Registrar un libro en el catálogo.
2. Eliminar un libro del catálogo.
3. Buscar un libro por título.
4. Buscar un libro por ISBN.
5. Abastecer ejemplares de un libro.
6. Vender ejemplares de un libro.
7. Calcular la cantidad de transacciones de abastecimiento de un libro particular.
8. Buscar el libro más costoso.
9. Buscar el libro menos costoso.
10. Buscar el libro más vendido.
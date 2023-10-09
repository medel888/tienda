from django.db import models
from django.contrib.auth.models import User
from store.models import Product

# La clase Cart representa un carrito de compras para un usuario, con métodos para agregar y eliminar
# artículos, calcular el precio total y recuperar los artículos del carrito.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def get_cart_total(self):
        """
        La función calcula el coste total de todos los artículos de un carrito de compras.
        :return: El valor total de todos los artículos del carrito.
        """
        cart_items = CartItem.objects.filter(cart=self)
        total = sum(item.product.price * item.quantity for item in cart_items)
        return total
    
    def get_cart_items(self):
        """
        La función `get_cart_items` devuelve todos los artículos del carrito asociados con un carrito
        determinado.
        :return: un conjunto de consultas de objetos CartItem que pertenecen al carrito actual.
        """
        cart_items = CartItem.objects.filter(cart=self)
        return cart_items

    def add_to_cart(self, product, quantity):
        """
        La función agrega un producto al carrito con la cantidad especificada.
        
        :param product: El parámetro de producto es el producto que el usuario quiere añadir a su
        carrito. Podría ser una instancia de un modelo de Producto o cualquier otro objeto que
        represente un producto
        :param quantity: El parámetro cantidad representa la cantidad de unidades del producto que el
        usuario desea agregar a su carrito
        """
        cart_item, created = CartItem.objects.get_or_create(cart=self, product=product)
        cart_item.quantity += quantity
        cart_item.save()

    def remove_from_cart(self, product):
        """
        La función elimina un producto específico del carrito.
        
        :param product: El parámetro "producto" es el producto específico que desea eliminar del carrito
        """
        CartItem.objects.filter(cart=self, product=product).delete()

    def __str__(self):
        """
        La función devuelve una representación de cadena de un objeto Cart.
        :return: La representación de cadena del objeto, que es "Carrito" seguido de la identificación
        del objeto.
        """
        return f"Cart {self.id}"


# La clase `CartItem` representa un artículo en un carrito de compras, con una referencia al carrito,
# el producto y la cantidad del producto en el carrito.
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"CartItem {self.id} - Product: {self.product.name}, Quantity: {self.quantity}"

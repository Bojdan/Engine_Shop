from decimal import Decimal
from django.conf import settings
from main.models import Engine


class Cart(object):

    def __init__(self, request):
        """
        Иницаплизируем карзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Создаём карту сессии(если юзер первый раз зашёл на сайт)
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=True):
        """
        Добавляем продукты в карзину
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        Объяввление сессии cart
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        """
        Отменить севнс как 'изменённый', чтоб убедится, что он создан.
        """
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товаров из карзины
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в карзине из БД
        """
        product_ids = self.cart.keys()
        """
        Получение объектов product и добавления их в карзину
        """
        products = Engine.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчёт всех товарор в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подчёт стоимости товаров
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """
        Удаление объектов
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

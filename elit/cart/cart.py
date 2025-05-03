from decimal import Decimal
from django.conf import settings
from main.models import Product

# бекенд корзины
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем пустую корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if override_quantity:   # товара больше чем 1
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # Обновляем сессию
        self.session.modified = True

# Удаляем продукт из корзины
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # Получаем продукты из базы данных и добавляем их в корзину
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        # Подсчитываем количество товаров в корзине
        return sum(item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # Удаляем корзину из сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()

# Просчитываем общую стоимость товаров в корзине с учетом скидки
    def get_total_price(self):
        total = sum((Decimal(item['price']) - (Decimal(item['price']) \
            * Decimal(item['product'].discount / 100))) * item['quantity']
                for item in self.cart.values())
        return format(total, '.2f')
    # 2f - округляем до 2 знаков после запятой
    
    
from functools import reduce


class ShoppingCart:

    def __init__(self):
        self.products = []

    def __getitem__(self, i):
        return self.products[i]

    def __len__(self):
        return len(self.products)

    def add_one_product(self, product):
        self.products.append(product)

    def add_many_products(self, products):
        [self.products.append(product) for product in products]

    def sum_of_prices(self):
        return reduce(
            lambda x, y: x + y, [produtc['price'] for produtc in self]
            )

    def print(self):
        acumulator = 0
        total = self.sum_of_prices()
        product_text_template = '{}\t{}\t{}\t{}'

        print('Product\t', 'Price\t', 'SubTotal\t', 'Total')
        for product in self:
            acumulator += product['price']
            print(product_text_template.format(
                product['name'],
                product['price'],
                acumulator,
                total
            ))


shopping_cart = ShoppingCart()
shopping_cart.add_one_product({'name':'CellPhone', 'price': 300.0})
shopping_cart.add_many_products([
    {'name':'CellPhone', 'price': 300.0},
    {'name':'ICellPhone', 'price': 600.0}
])

print('Quantity:', len(shopping_cart), 'Price:', shopping_cart.sum_of_prices())
shopping_cart.print()
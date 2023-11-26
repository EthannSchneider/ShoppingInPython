from shopping.cart_item import CartItem

class Cart:
    # region private attributes
    __cart_items: list[CartItem]
    # endregion private attributes

    def add(self):
        raise NotImplementedError

    def remove(self):
        raise NotImplementedError

    @property
    def cart_items(self):
        raise NotImplementedError

    def does_exist(self):
        raise NotImplementedError

    def cheapest(self):
        raise NotImplementedError

    def most_expensive(self):
        raise NotImplementedError

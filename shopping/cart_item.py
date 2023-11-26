from shopping.article import Article
from shopping.exception.cart_item.update_quantity_excpetion import UpdateQuantityException
from shopping.exception.cart_item.wrong_quantity_exception import WrongQuantityException

class CartItem:

    # region private attributes
    __article: Article
    __quantity: int
    # endregion private attributes

    # region public methods
    def __init__(self, article, quantity) -> None:
        self.__article = article
        self.__quantity = quantity

    @property
    def article(self) -> Article:
        """the article of the cart item

        Returns:
            Article: the article of the cart item
        """
        return self.__article

    @property
    def quantity(self) -> int:
        """the quantity of the article

        Returns:
            int: the quantity of the article
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        """the quantity of the article

        Args:
            value (int): the quantity of the article

        Raises:
            UpdateQuantityException: Raised if the quantity is the same as the current quantity
            WrongQuantityException: Raised if the quantity is negative
        """
        if value == self.__quantity:
            raise UpdateQuantityException
        if value < 0.0:
            raise WrongQuantityException
        self.__quantity = value
    # endregion public methods
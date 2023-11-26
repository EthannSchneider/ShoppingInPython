from shopping.exception.article.special_char_in_description_exception import SpecialCharInDescriptionException
from shopping.exception.article.too_long_description_exception import TooLongDescriptionException
from shopping.exception.article.too_short_descritpion_exception import TooShortDescriptionException
from shopping.exception.article.wrong_price_exception import WrongPriceException

class Article:

    # region private attributes
    __id: int
    __description: str
    __price: float
    # endregion private attributes
    
    # region public methods
    def __init__(self, id: int, description: str, price: float) -> None:
        self.__id = id
        self.__description = description
        self.__price = price

    @property
    def id(self) -> int:
        """the id of the article

        Returns:
            int: the id of the article
        """
        return self.__id

    @property
    def description(self) -> str:
        """the description of the article

        Returns:
            str: the description of the article
        """
        return self.__description

    @description.setter
    def description(self, value: str) -> None:
        """the description of the article

        Args:
            value (str): the description of the article
            
        Raises:
            SpecialCharInDescriptionException: Raised if the description contains a special char
            TooShortDescriptionException: Raised if the description is too short
            TooLongDescriptionException: Raised if the description is too long
        """
        self.__check_description(value)
        self.__description = value

    @property
    def price(self) -> float:
        """the price of the article

        Returns:
            float: the price of the article
        """
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """the price of the article

        Args:
            value (float): the price of the article
            
        Raises:
            WrongPriceException: Raised if the price is negative or the same as the current price
        """
        if int(value) < 0 or value == self.__price:
            raise WrongPriceException
        self.__price = value
    # endregion public methods
    
    # region private methods
    def __check_description(self, description_to_check: str) -> None:
        special_chars = ['!', '*', '+', '/']

        for special_char in special_chars:
            if special_char in description_to_check:
                raise SpecialCharInDescriptionException

        if len(description_to_check.split(' ')) == 1:
            raise TooShortDescriptionException

        if len(description_to_check) > 50:
            raise TooLongDescriptionException
    # endregion private methods
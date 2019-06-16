class Stock:
    def __init__(self, symbol, name, preClosingPrice, curPrice):
        self.__symbol = symbol
        self.__name = name
        self.__preClosingPrice = preClosingPrice
        self.__curPrice = curPrice

    def get_symbol(self):
        return self.__symbol

    def get_name(self):
        return self.__name

    def get_preClosingPrice(self):
        return self.__preClosingPrice

    def set_preClosingPrice(self, preClosingPrice):
        self.__preClosingPrice = preClosingPrice

    def get_curPrice(self):
        return self.__curPrice

    def set_curPrice(self, curPrice):
        self.__curPrice = curPrice

    def getChangePercent(self):
        return (self.__curPrice-self.__preClosingPrice)/self.__preClosingPrice*100


def main():
    stock = Stock(10001, '平头哥芯片', 62.8, 70.32)
    print(stock.get_name())
    print(stock.get_preClosingPrice())
    print(stock.get_curPrice())
    print(stock.getChangePercent())


if __name__ == '__main__':
    main()

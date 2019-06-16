class QE:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def getD(self):
        return self.__b*self.__b-4*self.__a*self.__c

    def getRoot1(self):
        if self.getD() >= 0:
            return (-self.__b+self.getD()**0.5)/(2*self.__a)

    def getRoot2(self):
        if self.getD() > 0:
            return (-self.__b-self.getD()**0.5)/(2*self.__a)


def main():
    print('input a,b,c:')
    a, b, c = [int(x) for x in input().split()]
    qe = QE(a, b, c)
    if qe.getD() > 0:
        print(qe.getRoot1(), qe.getRoot2())
    elif qe.getD() == 0:
        print(qe.getRoot1())
    else:
        print('no root')


if __name__ == '__main__':
    main()

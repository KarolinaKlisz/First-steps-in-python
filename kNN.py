import numpy as np
import math

class Knn:

    def __init__(self, k, zbior=None):
        if zbior is None:
            zbior = []
        self.zbior = zbior
        self.k = k

    def train(self, dane_train):
        for wiersz in dane_train:
            self.zbior.append(wiersz)

    def odleglosc_euklidesowa(self, wiersz_train, wiersz_test):
        odleglosc = 0.0
        for i in range(0, len(wiersz_train) - 1):
            odleglosc = odleglosc + (wiersz_train[i] - wiersz_test[i]) ** 2
        return math.sqrt(odleglosc)

    def odleglosc_taksowkowa(self, wiersz_train, wiersz_test):
        odleglosc = 0.0
        for i in range(0, len(wiersz_train) - 1):
            odleglosc = odleglosc + abs(wiersz_train[i] - wiersz_test[i])
        return odleglosc

    def odleglosc_maksimum(self, wiersz_train, wiersz_test):
        odleglosc = 0.0
        for i in range(0, len(wiersz_train) - 1):
            odleglosc = max(abs(wiersz_train[i] - wiersz_test[i]), odleglosc)
        return odleglosc

    def odleglosc_cosinus(self, wiersz_train, wiersz_test):
        return np.dot(wiersz_train[:-1], wiersz_test) / (np.linalg.norm(wiersz_train[:-1])) + np.linalg.norm(
            wiersz_test)

    def predict(self, dane_predict, typ_odleglosci):
        if typ_odleglosci == 1:
            typ_odleglosci = self.odleglosc_euklidesowa
        elif typ_odleglosci == 2:
            typ_odleglosci = self.odleglosc_taksowkowa
        elif typ_odleglosci == 3:
            typ_odleglosci = self.odleglosc_maksimum
        elif typ_odleglosci == 4:
            typ_odleglosci = self.odleglosc_cosinus
        else:
            print("Nie ma takiego wyboru.")

        predictions = []
        for wiersz_test in dane_predict:
            odleglosci = np.array([])
            for wiersz_train in self.zbior:
                odleglosci = np.append(odleglosci, [wiersz_train[-1], typ_odleglosci(wiersz_train, wiersz_test)])
            odleglosci = odleglosci.reshape(-1, 2)
            odleglosci = odleglosci[np.argsort(odleglosci[:, -1])][:self.k, :1]
            wartosci, zliczenia = np.unique(odleglosci, return_counts=True)
            predictions.append(wartosci[np.argmax(zliczenia)])
        return predictions

przyklad = Knn(3, [[1.1234321, 3.111231, 1],
                   [3.2432, 2.36421423, 0],
                   [1.588889, 3.21111, 0],
                   [2.8909876, 5.678543, 1],
                   [1.2345432, 5.65443, 1]])

przyklad.train([[1.235664, 0.954321, 0],
                [9.5432123, 5.432345, 1],
                [2.312312, 0.321312, 0]])

print(przyklad.predict([[1.21, 2.22], [1.3, 3.4], [1.23, 2.4]], 2))
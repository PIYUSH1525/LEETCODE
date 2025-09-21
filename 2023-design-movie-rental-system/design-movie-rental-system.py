from typing import List
from collections import defaultdict
from sortedcontainers import SortedList
class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.unrented = defaultdict(SortedList)
        self.shop_and_movie_to_price = {}
        self.rented = SortedList()
        for shop, movie, price in entries:
            self.unrented[movie].add((price, shop))
            self.shop_and_movie_to_price[(shop, movie)] = price
    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.unrented[movie][:5]]
    def rent(self, shop: int, movie: int) -> None:
        price = self.shop_and_movie_to_price[(shop, movie)]
        self.unrented[movie].remove((price, shop))
        self.rented.add((price, shop, movie))
    def drop(self, shop: int, movie: int) -> None:
        price = self.shop_and_movie_to_price[(shop, movie)]
        self.unrented[movie].add((price, shop))
        self.rented.remove((price, shop, movie))
    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]
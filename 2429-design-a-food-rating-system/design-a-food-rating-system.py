from collections import defaultdict
from sortedcontainers import SortedList
from typing import List

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_to_foods = defaultdict(SortedList)
        self.food_info = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.cuisine_to_foods[cuisine].add((-rating, food))
            self.food_info[food] = (rating, cuisine)

    def changeRating(self, food: str, newRating: int) -> None:
        old_rating, cuisine = self.food_info[food]
        self.food_info[food] = (newRating, cuisine)
        self.cuisine_to_foods[cuisine].remove((-old_rating, food))
        self.cuisine_to_foods[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_to_foods[cuisine][0][1]


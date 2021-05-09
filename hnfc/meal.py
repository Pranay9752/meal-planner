import pandas as pd
import operator



meal_items = pd.read_pickle('meal_items_2.pickle')
df = pd.read_csv('fooddata5.csv')

class MealPlanner:
    def __init__(self, calories):
        self.b_cal = int(calories*0.32)
        self.l_cal = int(calories*0.23)
        self.d_cal = int(calories*0.30)
        self.s_cal = int(calories*0.14)
    
    def get_meal_items(self,calories):
        self.meal = {}

        for i in meal_items:
            if meal_items[i][0] in range(calories-1,calories+1):
                self.meal[meal_items[i]] = i
        sorted_tuples = sorted(self.meal.keys(), key=operator.itemgetter(1), reverse=True)[0] 
        return self.meal[sorted_tuples]

    def meals(self):
        self.b_items = self.get_meal_items(self.b_cal)
        self.l_items = self.get_meal_items(self.l_cal)
        self.d_items = self.get_meal_items(self.d_cal)
        self.s_items = self.get_meal_items(self.s_cal)
        return self.get_meals()
    
    def get_meals(self):
        d = {
            'breakfast' : [
                dict(df.iloc[self.b_items[0],1:3]),
                dict(df.iloc[self.b_items[1],1:3])
            ],
            'lunch' : [
                dict(df.iloc[self.l_items[0],1:3]),
                dict(df.iloc[self.l_items[1],1:3])
            ],
            'dinner' : [
                dict(df.iloc[self.d_items[0],1:3]),
                dict(df.iloc[self.d_items[1],1:3])
            ],
            'snacks' : [
                dict(df.iloc[self.s_items[0],1:3]),
                dict(df.iloc[self.s_items[1],1:3])
            ],
        }
        return d
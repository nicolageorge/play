# food = {
#   "chicken": [20, 5, 10], # per 100g chicken has 20g of protein, 5 grams of carbohydrates and 10 grams of fat.
#   "eggs": [10, 5, 15],    # protein:10g , carbs:5g , fats: 15g
#   "salmon": [27, 0, 10],
#   "beans": [8, 25, 0],
#   "bananas": [1, 23, 0],
# }
# a = ["175g pork, 100g eggs, 25g chocolate", "175g goose, 200g cheddar, 250g milk, 300g kiwi", "100g catfish, 125g parmesan, 75g chocolate, 125g watermelon", "125g chicken, 25g beans, 50g lemons"]
# b = ["150g elk, 325g tofu, 150g watermelon", "75g pork, 50g mushrooms, 75g kiwi", "275g rabbit, 325g broccoli, 100g cherries", "225g duck, 200g potatoes, 175g parmesan, 25g wine", "225g rabbit, 125g broccoli"]
# c = ["350g goose, 75g mozzarella", "325g beef, 175g tofu, 75g juice", "125g goose, 350g rice", "175g beef, 50g mushrooms", "325g pork, 50g mushrooms", "325g rabbit, 175g cheddar"]
# d = ["325g duck, 175g potatoes, 325g bananas", "75g elk, 225g rice", "100g chicken, 50g broccoli", "300g turkey, 325g corn, 175g milk, 50g wine", "150g bass, 75g tomatoes, 275g wine", "200g buffalo, 150g potatoes"]


def rounder(numb):
    if numb == 0:
        return 0
    if numb % int(numb) == 0:
        return int(numb)
    else:
        return round(numb, ndigits=2)

def get_calories(protein=0, carbs=0, fat=0):
    return rounder(protein*4 + carbs*4 + fat*9)


def get_nutrients(item, quantity):
    p = quantity*food[item][0]/100
    c = quantity*food[item][1]/100
    f = quantity*food[item][2]/100
    return p, c, f


def bulk(arr):
    protein = 0
    carbs = 0
    fat = 0
    for i in arr:
        meal = i.split(", ")
        for f in meal:
            i = f.split("g ")
            quantity = int(i[0])
            item = i[1]
            p, c, f = get_nutrients(item, quantity)
            protein += p
            carbs += c
            fat += f
    return "Total proteins: {} grams, Total calories: {}".format(rounder(protein), get_calories(protein=protein, carbs=carbs, fat=fat))





print bulk(a)

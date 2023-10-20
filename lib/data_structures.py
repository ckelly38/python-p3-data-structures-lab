spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    if (spicy_foods == None): return None;
    elif (len(spicy_foods) < 1): return [];
    else: return [myvalobj["name"] for myvalobj in spicy_foods];

def get_spiciest_foods(spicy_foods):
    #heat level > 5
    if (spicy_foods == None): return None;
    elif (len(spicy_foods) < 1): return [];
    else: return [myvalobj for myvalobj in spicy_foods if myvalobj["heat_level"] > 5];

def spicyfoodToString(foodobj):
    myhtlvstr = "🌶" * foodobj['heat_level'];
    return f"{foodobj['name']} ({foodobj['cuisine']}) | Heat Level: {myhtlvstr}";

def print_spicy_foods(spicy_foods):
    if (spicy_foods == None): return None;
    elif (len(spicy_foods) < 1): print("");
    else:
        for i in range(len(spicy_foods)):
            print(spicyfoodToString(spicy_foods[i]));
    return None;

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    if (spicy_foods == None): return None;
    elif (len(spicy_foods) < 1): return None;
    else:
        myspfdswithcuisine = [myvalobj for myvalobj in spicy_foods if myvalobj["cuisine"] == cuisine];
        if (myspfdswithcuisine == None): return None;
        elif (len(myspfdswithcuisine) < 1): return None;
        else: return myspfdswithcuisine[0];

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods));
    return None;

def get_average_heat_level(spicy_foods):
    if (spicy_foods == None): return 0;
    elif (len(spicy_foods) < 1): return 0;
    else:
        theat = 0;
        for i in range(len(spicy_foods)):
            theat += spicy_foods[i]["heat_level"];
        return (theat / len(spicy_foods));

def create_spicy_food(spicy_foods, spicy_food):
    if (spicy_food == None): return spicy_foods;
    elif (spicy_foods == None): return [spicy_food];
    else:
        spicy_foods.append(spicy_food);
        return spicy_foods;

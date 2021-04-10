import psycopg2

class PostgreSQL():
    def __init__(self, *args, **kwargs):
        return(None)

    def openConnection(self):
        try:
            self.conn = psycopg2.connect(host = "localhost",
                                    user="josephsmith",
                                    port="5432",
                                    database="josephsmith")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def closeConnection(self):
        self.conn.close()

    def addRecipe(self, info):

        def apostrophe_check(string):
            new_string = ''
            for char in string:
                if char != '\'':
                    new_string+=char
                else:
                    new_string+='\'\''
            return(new_string)

        title, feeds, calories, prep, cook, img_path, instructions = info
        instructions = apostrophe_check(instructions)
        img = open(img_path, 'rb')
        binary = psycopg2.Binary(img.read())
        img.close()
        cursor = self.conn.cursor()
        cursor.execute('''SELECT id FROM recipes;''')

        # May be slow with large database
        rows = len(cursor.fetchall())
        id_num = rows+1
        print(id_num)

        recipe_query = '''INSERT INTO recipes(id, title, feeds, calories, prep_time, cook_time, instructions, image)
                            VALUES (%i, '%s', %i, %i, %i, %i, '%s', %s);''' %(id_num, title, feeds, calories, prep, cook, instructions, binary)
        cursor.execute(recipe_query)
        self.conn.commit()

    def deleteRecipe(self, id_num):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM recipes WHERE id = %i;' %(id_num)) 
        cursor.execute('''SELECT * FROM recipes;''')
        print(len(cursor.fetchall()))
        self.conn.commit()

    def listRecipes(self):
        cursor=self.conn.cursor()
        cursor.execute('SELECT title FROM recipes')
        print(cursor.fetchall())
        self.conn.commit()

    def addIngredient(self, ingred_info):
        recipe_id, ingredient, amount, prep = ingred_info
        cursor=self.conn.cursor()
        cursor.execute('''SELECT * FROM ingredients;''')
        rows = cursor.fetchall()
        print(rows)
        id_num = len(rows)+1

        present = False
        for i in rows:
            if i[1] == ingredient:
                id_num = i[0]
                present = True
        if present == False:
            ingredient_query = '''INSERT INTO ingredients(id, ingredient)
                                VALUES (%i, '%s');''' %(id_num, ingredient)
            cursor.execute(ingredient_query)

        recipe_ingredient_query = '''INSERT INTO recipes_ingredients(recipe_id, ingredient_id, amount, preparation)
                                        VALUES (%i, %i, '%s', '%s')''' %(recipe_id, id_num, amount, prep)
        cursor.execute(recipe_ingredient_query)
        self.conn.commit()

    def deleteIngredient(self, id_num):
        cursor = self.conn.cursor()
        cursor.execute('''DELETE FROM ingredients WHERE id = %i;''' %(id_num)) 
        cursor.execute('''SELECT * FROM ingredients;''')
        print(len(cursor.fetchall()))
        cursor.execute('''DELETE FROM recipes_ingredients WHERE ingredient_id = %i;''' %(id_num))
        self.conn.commit()

    def extractRecipe(self, id_num):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM recipes WHERE id = %i;''' %(id_num))
        recipe = cursor.fetchall()
        title, feeds, calories, prep, cook, instructions, image = recipe[0][1:]
        return(title, feeds, calories, prep, cook, instructions, image)
        


    

psql = PostgreSQL()
psql.openConnection()

info = ['''Mediterranean-style fried rice with anchovy lemon dressing''', 
2, 
350, 
20, 
25,
'''/Users/josephsmith/Documents/recipe-manager/recipe_images/mediterranean-style_fried_rice_with_anchovy_lemon_dressing.webp''', 
'''First, make the dressing. Put the anchovies, garlic, cumin, oil and a good grind of pepper in a small saucepan on a medium heat. 
As soon as it starts to bubble, turn off the heat, add the lemon juice, leave to cool, then stir in the parsley.

Put a tablespoon of oil in a large frying pan for which you have a lid, and put on a medium-high heat. 
Add the diced pepper and saute for four minutes, stirring occasionally, until nicely coloured and softened. 
Add two more tablespoons of oil, the garlic, red chilli and spring onion whites, and cook for two minutes more, until they’ve also taken on some colour. 
Now add the spring onion greens, thyme and strips of lemon peel, and cook for another minute.

Add the rice, a quarter-teaspoon of salt and a good grind of pepper, and cook for three minutes, stirring to breakup any clumps, until the rice is heated through and starting to take on a little colour.

Use a spoon to make two wells in the rice mixture, exposing the bottom of the pan. 
Pour a teaspoon and a half of oil into each well, then crack an egg into each one and turn down the heat to medium. 
Sprinkle lightly with salt and pepper, cover the pan with a lid and leave to cook for four to five minutes, until the egg whites are set and the yolks still runny, and the bottom of the rice is nice and crisp. 
Drizzle the dressing all over the top and serve right away straight from the pan.''']

ingred_info = [1, 'chilli flakes', '2 tsp', '']

#psql.deleteRecipe(12)
#psql.addRecipe(info)
#psql.listRecipes()
#psql.addIngredient(ingred_info)
#psql.deleteIngredient(19)
psql.extractRecipe(1)
psql.closeConnection()
import sqlite3

conn = sqlite3.connect('module1-introduction-to-sql/rpg_db.sqlite3')
cur = conn.cursor()


# 1 How many total Characters are there?
Q1 = """
     SELECT COUNT (DISTINCT character_id)
     FROM charactercreator_character;
     """
print(cur.execute(Q1).fetchall())

# 2 How many of each specific subclass?
Q2 = """
     SELECT COUNT (DISTINCT character_id)
     FROM
     """
print(cur.execute(Q2).fetchall())

# Question 2 - How many of each specific subclass?
query = 'SELECT * FROM charactercreator_mage;'
characters = len(cur.execute(query).fetchall())
print('Total Mage: ', characters)

query = 'SELECT * FROM charactercreator_thief;'
characters = len(cur.execute(query).fetchall())
print('Total Thief: ', characters)

query = 'SELECT * FROM charactercreator_cleric;'
characters = len(cur.execute(query).fetchall())
print('Total Cleric: ', characters)

query = 'SELECT * FROM charactercreator_fighter;'
characters = len(cur.execute(query).fetchall())
print('Total Fighter: ', characters)

# Question 3 - How many total items?
query = 'SELECT * FROM armory_item'
total_items = len(cur.execute(query).fetchall())
print('Total Items: ', total_items)

# Question 4 - How many of the Items are weapons? How many are not?
query = 'SELECT * FROM armory_weapon'
is_weapon = len(cur.execute(query).fetchall())
print('Are weapons: ', is_weapon)
query = 'SELECT * FROM armory_item'
is_not_weapon = (len(cur.execute(query).fetchall())) - is_weapon
print('Are not weapons: ', is_not_weapon)

# Question 5 - How many Items does each character have? (Return first 20 rows)
query = '''
        SELECT cc.character_id cid, COUNT(charactercreator_character_inventory.item_id) AS NumOfItems
        FROM charactercreator_character as cc LEFT JOIN charactercreator_character_inventory ON cid = 
        charactercreator_character_inventory.character_id GROUP BY cid LIMIT 20;
        '''
items_per_char = cur.execute(query).fetchall()
print('Total items per character: ', items_per_char)


# - How many of the Items are weapons? How many are not?
# - How many Items does each character have? (Return first 20 rows)
# - How many Weapons does each character have? (Return first 20 rows)
# - On average, how many Items does each Character have?
# - On average, how many Weapons does each character have?
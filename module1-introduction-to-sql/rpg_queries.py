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

# - How many total Items?
# - How many of the Items are weapons? How many are not?
# - How many Items does each character have? (Return first 20 rows)
# - How many Weapons does each character have? (Return first 20 rows)
# - On average, how many Items does each Character have?
# - On average, how many Weapons does each character have?
import sqlite3

class ProblemsPipeline:
    def __init__(self):
        self.con = sqlite3.connect('problems.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
        name TEXT PRIMARY KEY,
        brand TEXT,
        price REAL
        )""")

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES(?,?,?)""",
                         (item['name'], item['brand'], item['price']))
        self.con.commit()
        return item

import sqlite3
from sqlite3 import Error
import os


class DataBase():
    def __init__(self, database):
        self.a = self.get_path(database)
        self.b = self.create_conection()

    def get_path(self, database):
        self.dirname = os.path.dirname(__file__)
        self.filename = os.path.join(self.dirname, database)
        return self.filename

    def create_conection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.a)
            print('success')
        except Error as e:
            print(f'Error {e}')
        return connection

    def execute_query(self, query):  # рефакторнути
        cursor = self.b.cursor()
        try:
            cursor.execute(query)
            self.b.commit()
        except Error as e:
            print(f'Error {e}')

    def execute_read_query(self, query):
        cursor = self.b.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")


t = DataBase('test.db')


create_users_table = """
CREATE TABLE IF NOT EXISTS users(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name TEXT NOT NULL,
 age INTEGER,
 gender TEXT,
 nationality TEXT
);
"""

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 text TEXT NOT NULL,
 user_id INTEGER NOT NULL,
 post_id INTEGER NOT NULL,
 FOREIGN KEY(user_id) REFERENCES users(id) FOREIGN KEY(post_id) REFERENCES posts(id)
);
"""

create_likes_table = """
CREATE TABLE IF NOT EXISTS likes(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 user_id INTEGER NOT NULL,
 post_id integer NOT NULL,
 FOREIGN KEY(user_id) REFERENCES users(id) FOREIGN KEY(post_id) REFERENCES posts(id)
);
"""

create_post_table = """CREATE TABLE IF NOT EXISTS posts(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL,
 description TEXT NOT NULL,
 user_id INTEGER NOT NULL,
 FOREIGN KEY(user_id) REFERENCES users(id)
);
"""
# t.execute_query(create_post_table)

# t.execute_query(create_users_table)
# t.execute_query(create_comments_table)
# t.execute_query(create_likes_table)


reate_comments = """
INSERT INTO
 comments(text, user_id, post_id)
VALUES
('Count me in', 1, 6),
('What sort of help?', 5, 3),
('Congrats buddy', 2, 4),
('I was rooting for Nadal though', 4, 5),
('Help with your thesis?', 2, 3),
('Many congratulations', 5, 4);
"""
# t.execute_query(reate_comments)

create_posts = """
INSERT INTO
 posts(title, description, user_id)
VALUES
("Happy", "I am feeling very happy today", 1),
("Hot Weather", "The weather is very hot today", 2),
("Help", "I need some help with my work", 2),
("Great News", "I am getting married", 1),
("Interesting Game", "It was a fantastic game of tennis", 5),
("Party", "Anyone up for a late-night party today?", 3);
"""
# t.execute_query(create_posts)


create_likes = """
INSERT INTO
 likes(user_id, post_id)
VALUES
(1, 6),
(2, 3),
(1, 5),
(5, 4),
(2, 4),
(4, 2),
(3, 6);
"""

# t.execute_query(create_likes)

create_users = """
INSERT INTO
 users(name, age, gender, nationality)
VALUES
('James', 25, 'male', 'USA'),
('Leila', 32, 'female', 'France'),
('Brigitte', 35, 'female', 'England'),
('Mike', 40, 'male', 'Denmark'),
('Elizabeth', 21, 'female', 'Canada');
"""

# t.execute_query(create_users)


# select_users = "SELECT * from users"
# users = t.execute_read_query(select_users)

# for user in users:
#     print(user)


select_users_posts = """
SELECT
 users.id,
 users.name,
 posts.description
FROM
 posts
 INNER JOIN users ON users.id = posts.user_id
"""
# розібратись з INNER JOIN

users_posts = t.execute_read_query(select_users_posts)
for users_post in users_posts:
    print(users_post)

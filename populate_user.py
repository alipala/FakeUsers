from faker import Faker
import sqlite3 as sqlite

# ===========================================================
# Step 3: Create 2000 users
# Step 4: The users should have the same areas as facebook register
#
# This is a demo application in order to show how to creating
# fake user data, based on facebook.com register template
# mailto:ali.pala@ymail.com
# ===========================================================


class PopulateUser:

    """Populate 2000 users and store their data in the db"""
    def fake_user_populate(self):
        try:
            # location provider
            fake = Faker('en_US')
            # Create a connection
            # Data will be stored in fake.db
            con = sqlite.connect('fake.db')

            cur = con.cursor()
            # Remove the table in the database,
            cur.execute("DROP TABLE IF EXISTS users")

            # Create users table
            cur.execute("CREATE TABLE users(id INT, first_name TEXT, last_name TEXT, sex TEXT, mail TEXT, "
                        "password TEXT, birth_date date, tel TEXT, image TEXT)")
            with con:
                for _ in range(1000):
                    # Creating a dictionary to store the data as key value pair
                    user_profile_dict = fake.simple_profile()

                    # Keys are used as a column names
                    columns = ', '.join(user_profile_dict.keys())
                    placeholders = ', '.join('?' * len(user_profile_dict))
                    sql = 'INSERT INTO users ({}) VALUES ({})'.format(columns, placeholders)

                    # Insert data
                    cur.execute(sql, tuple(user_profile_dict.values()))

                    # Save (commit) the changes
                    con.commit()
        except Exception as e:
            raise
            print("There is something wrong", e)


if __name__ == '__main__':
    p = PopulateUser()
    p.fake_user_populate()

'''
Created on Mar 10, 2020

@author: surya
'''

import pymysql


class Database:
    def connect(self):
        return pymysql.connect("book-mysql", "dev", "dev", "tennis_db")

        # return pymysql.connect("localhost", "root", "1234567", "tennis_db")

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM tennis_book order by Date asc")
            else:
                cursor.execute("SELECT * FROM tennis_book where id = %s order by Date asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):

        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO tennis_book(ATP,Location,Tournament,Date,Series,Court,Surface,Round,Winner,"
                           "Loser) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)", (
                               data['ATP'], data['Location'], data['Tournament'], data['Date'], data['Series'],
                               data['Court'], data['Surface'], data['Round'], data['Winner'], data['Loser']))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()
        print(data)
        print(data['ATP'], data['Location'], data['Tournament'], data['Date'], data['Series'], data['Court'],
              data['Surface'], data['Round'], data['Winner'], data['Loser'], id)
        try:

            cursor.execute("UPDATE tennis_book set ATP = %s, Location = %s, Tournament = %s, Date = %s, Series = %s, "
                           "Court = %s ,Surface = %s, Round = %s, Winner = %s, Loser = %s  where id = %s",
                           (data['ATP'], data['Location'], data['Tournament'], data['Date'], data['Series'],
                            data['Court'], data['Surface'], data['Round'], data['Winner'], data['Loser'], id,))

            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM tennis_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

import sqlite3
link=sqlite3.connect("MOVIECOLLECTION.db")
c=link.cursor()
query="""CREATE TABLE MOVIE_DETAILS1(Name VARCHAR(20),Actor VARCHAR(20),
Actress VARCHAR(20), Director VARCHAR(20),Year_of_rlse INTEGER);"""
c.execute(query);
query="""INSERT INTO  MOVIE_DETAILS1(Name,Actor,Actress,Director,Year_of_rlse)VALUES("MERSAL","JOSEPH VIJAY","SAMANTHA","ATLEE",2017);"""
c.execute(query)
query="""INSERT INTO MOVIE_DETAILS1(Name,Actor,Actress,Director,Year_of_rlse)VALUES("MASTER","JOSEPH VIJAY","MALAVIKA","LOKESH",2021);"""
c.execute(query)
query="""INSERT INTO  MOVIE_DETAILS1(Name,Actor,Actress,Director,Year_of_rlse)VALUES("DEAR COMRADE","VIJAY DEVARKONDA","RASHMIKA","BHARAT KAMMA",2017);"""
c.execute(query)
query="""INSERT INTO  MOVIE_DETAILS1(Name,Actor,Actress,Director,Year_of_rlse)VALUES("SOORAI POTRU","SURYA","ABARNA","SUDHA PRASAD",2020);"""
c.execute(query)
link.commit()
c.execute("SELECT * FROM  MOVIE_DETAILS1")
print("data:")
data=c.fetchall()
for i in data:
    print(i)
data1=c.execute("SELECT Name from  MOVIE_DETAILS1 WHERE Actor='JOSEPH VIJAY'")
for i in data1:
    print(i)

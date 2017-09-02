#!/usr/bin/python
import psycopg2
import query


def solution(q):
    # making the connection with database
    conn = psycopg2.connect("host='localhost' dbname='news' user='postgres' password= 'password'")
    # cursor from the connection
    cursor = conn.cursor()
    # executing the query
    cursor.execute(q)
    # fetching the result
    result = cursor.fetchall()
    # printing the result
    print result
    # close the connection
    conn.close()



def main():
    # sending the queries to solve importing from query.py file
    solution(query.query_one)
    solution(query.query_two)
    solution(query.query_three)




if '__name__' == '__main__':
    main()

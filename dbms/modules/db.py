import psycopg2
import os


def connect_to_db():
    conn = psycopg2.connect(
        database = "dafonabp5estsj",
        user = "krpnttxzepxgmc",
        password = "36bbd13385dc3c89abdfe15879f1a0bfbc029d0ee9d89e49702d9e75f3eda437",
        host = "ec2-52-1-115-6.compute-1.amazonaws.com"
    )
    conn.autocommit = True
    return conn.cursor()
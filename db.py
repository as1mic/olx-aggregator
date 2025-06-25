import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def save_ad_to_db(title, price, link):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ads (title, price, link)
        VALUES (%s, %s, %s)
    """, (title, price, link))
    conn.commit()
    conn.close()

def get_all_ads():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, price, link FROM ads")
    results = cursor.fetchall()
    conn.close()
    return results

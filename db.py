import mysql.connector

def save_ad_to_db(title, price, link):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="auto_aggregator_db"
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
        host="localhost",
        user="root",
        password="root",
        database="auto_aggregator_db"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT title, price, link FROM ads")
    results = cursor.fetchall()
    conn.close()
    return results


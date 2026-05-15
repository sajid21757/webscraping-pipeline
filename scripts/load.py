import psycopg2

def load_data(df):
    conn = psycopg2.connect(
        host="localhost",
        database="jobs_db",
        user="postgres",
        password="Abbasi123"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS quotes (
            id SERIAL PRIMARY KEY,
            text TEXT,
            author TEXT,
            base_currency TEXT,
            pkr_rate FLOAT
        )
    """)

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO quotes (text, author, base_currency, pkr_rate)
            VALUES (%s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()
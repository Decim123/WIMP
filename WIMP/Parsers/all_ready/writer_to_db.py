import sqlite3

def writer(data):
    try:
        conn = sqlite3.connect('pars_info.db')
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS realty (
                url TEXT,
                adres TEXT,
                area INTEGER,
                price INTEGER

            )
        ''')
        cursor.execute(f'INSERT INTO realty (url, adres, area, price) VALUES (?, ?, ?, ?)', data)
        conn.commit()
        conn.close()
        print(f"данные сохранены в realty успешно.")
    except Exception as e:
        print(f"ОШИБКА: {str(e)}")



def main():
    pass


if __name__ == '__main__':
    main()
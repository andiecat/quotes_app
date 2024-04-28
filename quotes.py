import psycopg2

SQL_CONNECTION_STRING = 'postgresql://localhost:5432/radu.vasilescu'


def main():
    conn = psycopg2.connect(SQL_CONNECTION_STRING)
    cursor = conn.cursor()

    cursor.execute("""
        select * 
        from public.quotes
        full join public.people p on p.source_id = "source"
        full join public.books b on b.source_id = "source"
    """)

    quotes = cursor.fetchall()

    for quote in quotes:
        # 6 = person name
        # 7 = person comment
        # 9 = book title
        # 10 = book author

        if quote[6] is not None and quote[6] != '':
            # it is a person
            print(f'{quote[1]}\n    -- {quote[6]} ({quote[7]})')
        
        if quote[9] is not None and quote[9] != '':
            # it is a book
            print(f'{quote[1]}\n    -- {quote[9]} ({quote[10]})')

    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()


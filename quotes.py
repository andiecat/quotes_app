import psycopg2
from flask import Flask, jsonify

def get_all_quotes():
    conn = psycopg2.connect(SQL_CONNECTION_STRING)
    cursor = conn.cursor()

    cursor.execute("""
        select * 
        from public.quotes
        full join public.people p on p.source_id = "source"
        full join public.books b on b.source_id = "source"
    """)

    quotes = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return [
        {
            "id": q[0],
            "text": q[1],
            "source": q[2],
            "date_added": q[3],
            "tags": q[4],
            "source_id": q[5],
            "name": q[6],
            "notes": q[7],
            "title": q[9],
            "author": q[10],
            "publication_year": q[11],
            "isbn": q[12]
        }
        for q in quotes
    ]

app = Flask(__name__)

@app.route("/quotes")
def quotes_endpoint():
    # return jsonify(get_all_quotes())
    webpage = ""
    webpage += "<h1>Quotes</h1>"
    webpage += "<ol>"

    for quote in get_all_quotes():
        webpage += f"<li>{quote['text']} <br/> by <span style=\"color: olivedrab\">{quote['name']}</span> <br/><br/></li>"

    webpage += "</ol>"

    return webpage


SQL_CONNECTION_STRING = 'postgresql://localhost:5432/andiecat'


def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

    # quotes = get_all_quotes()

    # for quote in quotes:
    #     print(quote)
        # 6 = person name
        # 7 = person comment
        # 9 = book title
        # 10 = book author

        # if quote[6] is not None and quote[6] != '':
        #     # it is a person
        #     print(f'{quote[1]}\n    -- {quote[6]} ({quote[7]})')
        
        # if quote[9] is not None and quote[9] != '':
        #     # it is a book
        #     print(f'{quote[1]}\n    -- {quote[9]} ({quote[10]})')




if __name__ == "__main__":
    main()
    

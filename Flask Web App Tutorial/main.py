from website import create_app

app = create_app()

if __name__ == '__main__':
    from waitress import serve
    app.run(debug=True)

    

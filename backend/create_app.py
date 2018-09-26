from app.factory import create_app
app = create_app()

if __name__ == "__main__":
    app = create_app(config="Development")
    app.run(debug=True, use_reloader=True, port=8080)

from flask import Flask

app = Flask(__name__)
print("Registered routes:", app.url_map) # Adding this line for better view of the routes


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
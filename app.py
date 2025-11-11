from flask import Flask, render_template
import json

app = Flask(__name__)
print("Registered routes:", app.url_map) # Adding this line for better view of the routes

# Load posts from Json file.
def load_posts():
    try:
        with open('posts.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("The file does not exist")
        return []

# Load the posts when the app starts
posts = load_posts()

@app.route('/')
def index():
    """ Pass posts to the template """
    return render_template('index.html', posts = posts)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
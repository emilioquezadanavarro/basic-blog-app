from flask import Flask, render_template, request, redirect, url_for
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

# Save post function
def save_posts(posts_to_save):
    with open('posts.json', 'w') as f:
        json.dump(posts_to_save, f, indent=4)

# 1 - Index route
@app.route('/')
def index():
    """ Pass posts to the template """
    return render_template('index.html', posts = posts)

# 2 - Add post route
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        # Get form data from add.html
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        # Validation all fields are filled
        if author and title and content:

            # Generate new ID for storage
            if posts:
                max_id = max(post['id'] for post in posts)
                new_id = max_id + 1
            else:
                new_id = 1

            # Create a new post directory

            new_post = {
                'id': new_id,
                'author': author,
                'title': title,
                'content': content
            }

            # Add the new post to post list

            posts.append(new_post)

            # Save to Json file

            save_posts(posts)

            # Return to index page to see the updated
            # list of posts

            return redirect(url_for('index'))

        else:
            return "Error: All fields are required", 400

    # GET response
    return render_template('add.html')

# 3 - Delete post route
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    # Find the post with matching ID
    post_to_delete = None
    for post in posts:
        if post['id'] == post_id:
            post_to_delete = post
            break

    if post_to_delete:

        # Remove from list

        posts.remove(post_to_delete)

        # Save to Json file

        save_posts(posts)

        # Return to index page to see updated version
        return redirect(url_for('index'))

    else:
        # Post not found
        return "Post not found", 404

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)

# GitHub Repository renamed to masterblog - connection verified
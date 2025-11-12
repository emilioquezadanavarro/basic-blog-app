## Masterblog

A fully functional Flask-based blog application with complete CRUD operations, built for learning web development fundamentals.

## 📋 Features

- View All Posts: Homepage displays all blog posts with formatting preserved
- Add New Posts: Web form to create blog posts with author, title, and content
- Edit Posts: Update existing posts with pre-filled form data
- Delete Posts: Remove posts with confirmation dialog (POST-based for security)
- Persistent Storage: All posts saved to JSON file (posts.json)
- Responsive UI: Clean, styled interface with centered layout

## 🛠 Technologies Used

- Backend: Python 3 with Flask framework
- Frontend: HTML5, CSS3, Jinja2 templating
- Data Storage: JSON file (no database needed)
- Version Control: Git with GitHub integration

## 📁 Project Structure

**Root Files:**
- `app.py` - Main Flask application
- `posts.json` - Blog posts data storage
- `.gitignore` - Git ignore rules
- `README.md` - This file

**Folders:**
- `static/` - Static assets
  - `style.css` - Custom styling
- `templates/` - HTML templates
  - `index.html` - Homepage
  - `add.html` - Add post form
  - `update.html` - Edit post form

## 🚀 Installation & Setup

1. Clone the Repository

git clone https://github.com/emilioquezadanavarro/masterblog.git
cd masterblog

2. Create Virtual Environment (Recommended)

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install Dependencies

pip install flask

4. Run the Application

python3 app.py

5. Open in Browser

Visit: http://127.0.0.1:5000/

## 💡 Usage Guide

- Viewing Posts

The homepage displays all blog posts with preserved formatting
Each post shows title, author, and content

- Adding a Post

Click "➕ Add New Post" on the homepage
Fill in author, title, and content fields
Click "Add Post" to save

- Editing a Post

Click the "✏️ Update" button next to any post
Modify the pre-filled form fields
Click "Update Post" to save changes

- Deleting a Post

Click the "🗑️ Delete" button next to any post
Confirm deletion in the popup dialog
Post is permanently removed

## 🎯 Key Learning Concepts

This project demonstrates:

- Flask Routing: Dynamic URLs with parameters
- Jinja2 Templates: Conditional rendering and loops
- Static Files: CSS styling and file organization
- Form Handling: GET vs POST requests
- Data Persistence: Reading/writing JSON files
- HTTP Status Codes: 200, 302, 404, 405
- PRG Pattern: Post-Redirect-Get for form submissions
- Git Workflow: Commit, push, pull, and remote management

## 🚀 Future Enhancements

Potential improvements for advanced learners:

- Migrate from JSON to SQL database
- Add user authentication (Flask-Login)
- Implement pagination for many posts
- Add Markdown support for rich text
- Deploy to PythonAnywhere or Heroku
- Add search and filter functionality
- Include image upload capability

## 📄 License

This project is open-source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!

HAPPY BLOGGING!📝
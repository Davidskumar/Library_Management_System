from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for books and members
books = []
members = []
users = {'admin': 'password'}  # Hardcoded user for authentication (username: admin, password: password)
sessions = {}

# Helper Functions
def generate_id(data_list):
    """Generates a unique ID based on the list size."""
    return len(data_list) + 1

def is_authenticated(token):
    return token in sessions.values()

# Routes for Books
@app.route('/books', methods=['GET'])
def get_books():
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    filtered_books = books
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    start = (page - 1) * per_page
    end = start + per_page
    return jsonify(filtered_books[start:end])

@app.route('/books', methods=['POST'])
def add_book():
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    data = request.json
    if not data.get('title') or not data.get('author'):
        abort(400, 'Title and Author are required')

    book = {
        'id': generate_id(books),
        'title': data['title'],
        'author': data['author']
    }
    books.append(book)
    return jsonify(book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    data = request.json
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        abort(404, 'Book not found')

    book.update({
        'title': data.get('title', book['title']),
        'author': data.get('author', book['author'])
    })
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        abort(404, 'Book not found')

    books.remove(book)
    return '', 204

# Routes for Members
@app.route('/members', methods=['GET'])
def get_members():
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    return jsonify(members)

@app.route('/members', methods=['POST'])
def add_member():
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    data = request.json
    if not data.get('name'):
        abort(400, 'Name is required')

    member = {
        'id': generate_id(members),
        'name': data['name']
    }
    members.append(member)
    return jsonify(member), 201

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    data = request.json
    member = next((member for member in members if member['id'] == member_id), None)
    if not member:
        abort(404, 'Member not found')

    member['name'] = data.get('name', member['name'])
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    token = request.headers.get('Authorization')
    if not is_authenticated(token):
        abort(401, 'Unauthorized')

    member = next((member for member in members if member['id'] == member_id), None)
    if not member:
        abort(404, 'Member not found')

    members.remove(member)
    return '', 204

# Authentication
@app.route('/login', methods=['POST'])
def login():
    credentials = request.json
    username = credentials.get('username')
    password = credentials.get('password')

    if users.get(username) == password:
        token = f"token-{username}"
        sessions[username] = token
        return jsonify({'token': token})
    abort(401, 'Invalid credentials')

@app.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization')
    username = next((user for user, t in sessions.items() if t == token), None)
    if username:
        del sessions[username]
        return '', 204
    abort(401, 'Unauthorized')

    
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Library Management System API!", 200

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
import json

app = Flask(__name__)
books = [
    {"id": 1, 'title': 'Book 1'},
    {"id": 2, 'title': 'Book 2'}]


# GET all books


@app.route('/books', methods=['GET'])
def get_books():
    response = jsonify(books)
    return response

# GET book by ID


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        response = jsonify(book)
    else:
        response = jsonify({'message': 'Book not found'})
    return response

# POST a new book


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or not 'title' in data:
        response = jsonify({'message': 'Invalid book data'})
        return response, 400
    book = {'id': len(books) + 1, 'title': data['title']}
    books.append(book)
    response = jsonify(book)
    return response, 201

# PUT update a book


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        response = jsonify({'message': 'Book not found'})
        return response, 404
    data = request.get_json()
    if not data or not 'title' in data:
        response = jsonify({'message': 'Invalid book data'})
        return response, 400
    book['title'] = data['title']
    response = jsonify(book)
    return response

# DELETE a book


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if not book:
        response = jsonify({'message': 'Book not found'})
        return response, 404
    books.remove(book)
    response = jsonify({'message': 'Book deleted'})
    return response


if __name__ == '__main__':
    app.run(debug=True)

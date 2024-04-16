from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route('/knihy/', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/knihy/', methods=['POST'])
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/knihy/<int:id>', methods=['GET'])
def search(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book)
    return jsonify({'Kniha': 'nenajdena'}), 404

@app.route('/knihy/<int:id>', methods=['DELETE'])
def delete(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)
            return jsonify({'message': 'Book deleted successfully'}),
        return jsonify({'message': 'nenajdena'}), 404

@app.route('/knihy/<int:id>', methods=['PATCH'])
def update_book(id):
    for book in books:
        if book['id'] == id:
            data = request.json
            if 'title' in data:
                book['title'] = data['title']
            if 'author' in data:
                book['author'] = data['author']
            return jsonify({'message': 'Book updated successfully'}),
    return jsonify({'message': 'nenajdena'}), 404





if __name__ == "__main__":
    app.run()
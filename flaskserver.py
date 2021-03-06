from flask import Flask, jsonify, request, abort
from DAO import DAO

app= Flask(__name__, static_url_path='', static_folder='.')


@app.route('/Books')
def getAll():
    results = DAO.getAll()
    return jsonify(results)

@app.route('/Books/<int:id>')
def findById(id):
    foundBooks = DAO.findByID(id)

    return jsonify(foundBooks)


@app.route('/Books', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    Books = {
        "Author": request.json['Author'],
        "Title": request.json['Title'],
        "Genre": request.json['Genre'],
        "Owned by": request.json['Owned by'],
        "Format": request.json['Format'],
    }
    values =(Books['Author'], Books['Title'], Books['Genre'], Books['Owned by'], Books['Format'])
    newId = DAO.create(values)
    Books['id'] = newId
    return jsonify(Books)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = DAO.findByID(id)
    if not foundBooks:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Author' in reqJson is int:
        abort(400)

    if 'Author' in reqJson:
        foundBook['Autor'] = reqJson['Author']
    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Genre' in reqJson:
        foundBook['Genre'] = reqJson['Genre']
    values = (foundBooks['Author'],foundBooks['Title'],foundBooks['Genre'],foundBooks['id'])
    DAO.update(values)
    return jsonify(foundBooks)
        

    

@app.route('/books/<int:id>' , methods=['DELETE'])
def delete(id):
    DAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)
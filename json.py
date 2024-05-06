import json

book = {}
book['tom'] = {
    'name': 'Siva',
    'address':'Kerala',
    'Phone': 9087072668
}

book['Hari'] ={
    'name': 'Hari',
    'address': 'Pondy',
    'Phone': 9677561918
}

s= json.loads(book)
print(s)
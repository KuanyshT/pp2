movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def checkrate():
    name = str(input("Name of the movie: "))
    
    for movie in movies:
        if movie["name"] == name:
            if movie["imdb"] > 5.5:
                return True
            else:
                return False
            
    return "moovie name is not found"

print(checkrate())
print()

def sblist():
    lst = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            lst.append(movie["name"])
    return lst


print(sblist())
print()

def ctgrylist():
    lst = []
    ctgry = str(input("enter category: "))
    for movie in movies:
        if movie["category"] == ctgry:
            lst.append(movie["name"])
    return lst

print(ctgrylist())
print()




            

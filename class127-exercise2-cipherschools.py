name=input("Enter Your Name: ")
age=input("Enter your age: ")
fav_movies=input("Enter your favorite movies (comma separated values): ").split(",")
fav_songs=input("Enter your favorite songs (comma separated values): ").split(",")
dic={}
dic["name"]=name
dic["age"]=age
dic["fav_movies"]=fav_movies
dic["fav_songs"]=fav_songs
print(dic)
for key,value in dic.items():
    print(f"{key}:{value}")
import requests
import json

def movie_data():
    random_joke = False
    movie_title = input("Enter Any Movie Title: ")
    if movie_title == "":
        print("You didn't Enter any Movie\n")
        random_joke = True
    movie_api_key = "637c5bd8"
    movie_base_url = "http://www.omdbapi.com/"
    movie_param = {"apikey":movie_api_key,"t":movie_title}
    movie_data = requests.get(movie_base_url,params=movie_param)
    json_movie_data = movie_data.json()
    plot_choosewordforjoke(movie_title,json_movie_data,random_joke)


def plot_choosewordforjoke(movie_title,json_movie_data,random_joke):
    header = {"accept":"text/plain"}
    if random_joke==True:
        get_joke = requests.get("https://icanhazdadjoke.com/",headers=header)
        print("Provided a Joke For You Too: {}".format(get_joke.text))
        return
    try:
        plot = json_movie_data['Plot']
    except:
        print("No Movies Found, Maybe Try Other Movies")
        return
    split_plot = plot.split()
    for word in range (len(split_plot)):
        for character in [',','.','(',')']:
            if character in split_plot[word]:
                split_plot[word] = split_plot[word].replace(character,"")
    dadjoke(movie_title,plot,split_plot,header)


def dadjoke(movie_title,plot,split_plot,header):
    base_url = "https://icanhazdadjoke.com/search"
    for num in range (len(split_plot)):
        if len(split_plot[num])>4:
            param = {"term":split_plot[num],"limit":1}
            get_joke = requests.get(base_url,params=param,headers=header)
            if get_joke.text == "":
                pass
            else:
                break
    if get_joke.text == "":
        print("I've got no jokes about this movie. It's too serious!")
        return
    split_joke = get_joke.text.split()
    for each_word in range (len(split_joke)):
        if split_joke[each_word] == split_plot[num]:
            split_joke[each_word] = "***"+split_plot[num]+"***"
    joke = " ".join(split_joke)
    split_plot[num]="***"+split_plot[num]+"***"
    plot = " ".join(split_plot)
    print("Plot of {}: {}\n".format(movie_title,plot))
    print("Joke About Your Movie: {}".format(joke))
movie_data()
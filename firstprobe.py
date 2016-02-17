import imdb 
from pandas import DataFrame as df
import pandas
import random
import pdb
from fish import ProgressFish


im = imdb.IMDb()
df1 = df()

movie_ids = []

for y in range(0, 5000):
    rand = random.randint(10000, 5300000)
    if rand not in movie_ids:
        movie_ids.append(rand)

print "Finished randomising, start now.."

def handle_lists(in_list, same_in_dict, in_key):
    count = 0
    for obj in in_list:
        if type(obj) == unicode:
            same_in_dict[0].update({in_key+str(count): obj})
        if type(obj) == int:
            same_in_dict[0].update({in_key+str(count): obj})
        if type(obj) == imdb.Person.Person:
            same_in_dict[0].update({in_key+str(count): obj['name']})
        count += 1

def makerows(in_map, in_dict):
    keys = ['director', 'rating', 'genres',
            'kind', 'runtimes', 'year', 'title']
    # if in_map.has_key('kind') == True:
    #     print in_map['kind'], type(in_map['kind'])
    for k in keys:
        if in_map.has_key(k):
            if type(in_map[k]) == int or type(in_map[k]) == float:
                in_dict[0].update({k: in_map[k]})
            if type(in_map[k]) == unicode:
                in_dict[0].update({k: in_map[k].encode('utf-8')})
            # if in_map.has_key('kind'):
            #     pdb.set_trace()
            if type(in_map[k]) == list:
                handle_lists(in_map[k], in_dict, k)

result = []
fish = ProgressFish(total=len(movie_ids))

for index, i in enumerate(movie_ids):
    # if index%100 == 0:
    #     print "On movie number: ", index
    fish.animate(amount=index)
    m = im.get_movie(i)
    maps = {}
    for keys in m.iterkeys():
      #  print keys, m[keys]
        maps.update({keys:m[keys]})
        dicts = [{}]

    # if maps.has_key('language codes'):
    #     if maps['language codes'][0].encode() != "en":
    #         continue
    # elif maps.has_key('language codes') == False:
    #     continue
    # if maps.has_key("title"):
    #     dicts[0].update({"title":maps['title'].encode()})
    # if maps.has_key("director"):
    #     #            dicts[0].update({"director":maps['director']})
    #     if len(maps['director']) == 1:
    #         try:
    #             dicts[0].update({'director': maps['director'][0]['name'].encode()})
    #         except:
    #             continue
    #     if len(maps['director']) > 1:
    #         for index, name in enumerate(maps['director']):
    #             try:
    #                 dicts[0].update({'director'+str(index): name['name'].encode()})
    #             except:
    #                 continue
                    
    # if maps.has_key("rating"):
    #     dicts[0].update({"rating":maps['rating']})
    # if maps.has_key("genres"):
    #     if len(maps['genres']) == 1:
    #         dicts[0].update({"genre":maps['genres'][0].encode()})
    #     if len(maps['genres']) > 1:
    #         for index, genre in enumerate(maps['genres']):
    #             dicts[0].update({'genres'+str(index): maps['genres'][index].encode()})
    # if maps.has_key("runtimes"):
    #     dicts[0].update({"runtimes":maps['runtimes'][0].encode()})
    # if maps.has_key("year"):
    #     dicts[0].update({"year":maps['year']})
    # if maps.has_key("kind"):
    #     dicts[0].update({"kind":maps['kind'].encode()})

    if maps != {} : ## To ensure that maps are filled, otherwise dicts is not defined! 
        makerows(maps, dicts)
#        print dicts
        result.append(df1.append(dicts))
#        print result

x = pandas.concat(result)
x.to_csv("results_5k.csv", encoding="utf-8")

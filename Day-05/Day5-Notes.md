#Dictionary:-
'''
dict is a key : value pair seperated by : and keys are unique
in the place of keys we have use immutaable data type..
dict is mutable
details= {"name" : "sankar",
          2:"number",
          (6,7):[7,8]}
print(details)
methods:-
Keys():-
used to get all the keys from the dict
syntax:- varible.keys()
details={"name" : "sankar",
         "age":21,
         "gender":"male"
         }
print(details.keys())

#value():-
details={"name" : "sankar",
         "age":21,
         "gender":"male"
         }
print(details.values())
#items():-
used to get both key and value in a pair
synatax varible.items()
details={"name" : "sankar",
         "age":21,
         "gender":"male"
         }
print(details.items())

s=[10,20,40,50,60]
print(s[0])
s={"name":"sankar",
   }
print(s["age"])
clear():-
if we use clear method the dict becomes empty
details={"name" : "sankar",
         "age":21,
         "gender":"male"
         }
details.clear()
print(detail)
update:-

details={"name" : "sankar",
         "age":21,
         "gender":"male"
         }
details.update({"age":90})
print(details)

details={"name" : "sankar",
         "age":21,
         "gender":"male"
         }
details.update({"mob":90})
print(details)

Sets:-
set is a collection of unordered elements that are seperated by ,
set is muttable
can remove duplicate value by itself...
go= {1,2,3,4,5)
print(go)


methods
union()():- combine the elements from both set
syntax:-set_1.union(set_2)
'''
g={1,2,3,4,5}
s={3,3,3,3,4}
print(g|s)
print(g.union(s))
#intersection()():-
common elements from both sets
syntax:-
set_1.intersection(set_2)
g={1,2,3,3,4}
s={2,3,3,5,5}
print(g.intersection(s))
symmetric difference() :-
all different elements from both sets
syntax:- set_1.symmentric_difference(set_2)
g={1,2,3,3,4}
s={2,3,3,5,5}
print(g^s)
print(g.symmentric_difference(s))
add():-
g={1,2,3,4}
g.add(46)
print(g)
remove():-
to delete the elements from set based on element  
g={1,2,3,4}
g.remove(4)
print(g)




         


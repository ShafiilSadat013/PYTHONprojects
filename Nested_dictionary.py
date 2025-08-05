capitals ={
    "France" : "Paris",
    "Germany":"Berlin"
}

#nested list in dictionary

#travel_log = {
 #   "France" : ["Paris","Lille","Dijon"],
  #  "Germany" : ["Munich","Stutgart","Leipzig"],

#}
#print(travel_log["France"][1])

travel_no = {
    "x"  : [1,2,3]
}
#print(travel_no["x"][1])
nested_list  = ["A","B",["C","D"]]

#print(nested_list[2][0])
travel_log = {
    "France" : {
        "num_times_visited" : 8,
        "cities visited" : ["Paris","Lille","Dijon"]
    },
    "Germany" :
        {
            "cities_visited"  : ["Munich","Stutgart","Leipzig"],
            "total visits" : 5
        }

}
print(travel_log["Germany"]["cities_visited"][1])

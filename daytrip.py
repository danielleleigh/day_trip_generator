import random

#place everything into functions!

list_of_destinations = ['Milwaukee' , 'Madison' , 'Racine' , 'Kenosha']
list_of_restaurants = ['Chick-fil-A' , 'Subway' , 'Dominos' , 'Qdoba']
list_of_transportation = ['Car' , 'Bus' , 'Airplane' , 'Train']
list_of_entertainment = ['Movies' , 'Concert' , 'Bar' , 'Skating']

#randomly select a value from each list & print. Remember to provide index 0, -1 in parenthesis.

def random_destination():
    print(random.choice(list_of_destinations))
    
def random_restaurant():
    print(random.choice(list_of_restaurants))

def random_transportation():
    print(random.choice(list_of_transportation))

def random_entertainment():
    print(random.choice(list_of_entertainment))

random_destination() , random_restaurant() , random_transportation() , random_entertainment()


#PLACE INTO FUNCTIONS!
# random_index = random.randint(0,len(list_of_destinations)-1)
# random_index2 = random.randint(0,len(list_of_restaurants)-1)
# random_index3 = random.randint(0,len(list_of_transportation)-1)
# random_index4 = random.randint(0,len(list_of_entertainment)-1)

# #list random itineraries
# spacing_for_list = ' , '
# trip_itinerary = list_of_destinations[random_index] + spacing_for_list + list_of_restaurants[random_index2] + spacing_for_list +  list_of_transportation[random_index3] + spacing_for_list + list_of_entertainment[random_index4]
# print('Here is your trip intinerary: ' + trip_itinerary)


def does_user_disapprove():
    user_disapproves = True
    while user_disapproves == True:
        user_trip_approval = input("Do you approve of this itinerary? ")
        if user_trip_approval == "No":
            random_destination() , random_restaurant() , random_transportation() , random_entertainment()
            # does_user_disapprove()
        elif user_trip_approval == "Yes":
             print("Your itinerary is confirmed!")
             user_disapproves = False

does_user_disapprove()


    



#old attempts--updated by placing in functions.
    # while user_trip_approval is True:
     
    # if user_trip_approval == 'Yes':
    #     print("Congrats! Your itinerary is confirmed!")
    # else:
    #     random_destination() , random_restaurant() , random_transportation() , random_entertainment()
    # does_user_approve()
    
    
    #  def does_user_disapprove():
    #  if input("No"):
    #  print(random_destination() , random_restaurant() , random_transportation() , random_entertainment())
    #  does_user_disapprove()


    # if trip_approval == 'No':
    #         print(random.choice(list_of_destinations))
    #         print(random.choice(list_of_restaurants))
    #         print(random.choice(list_of_transportation))
    #         print(random.choice(list_of_entertainment))
        

# # call functions in logical order to run app






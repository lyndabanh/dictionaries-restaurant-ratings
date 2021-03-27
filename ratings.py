def list_and_sort_restaurant_ratings(filename):
    """Restaurant rating lister."""

    #open file
    my_file = open(filename)

    #initialize empty dictionary of restaurants
    restaurant_ratings = {}

    #iterate through the file
    #for each line in file, make a list of items (rstrip, split)
    #add restaurant as key with value of its rating to the dictionary
    for line in my_file:
        restaurant_name_rating = line.rstrip().split(':')
        restaurant_ratings[restaurant_name_rating[0]] = int(restaurant_name_rating[1])
    
    return restaurant_ratings

print(list_and_sort_restaurant_ratings('scores.txt'))
    
    



# Reads the ratings in from the file

# Stores them in a dictionary

# And finally, spits out the ratings in alphabetical order by restaurant
# put your code here

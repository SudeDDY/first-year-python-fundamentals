"""320201049 - 320201097"""

def linear_search_iterative(city_ids, target_id):
    """Performs an iterative linear search on a list of city IDs. Returns the index of target_id if found, otherwise -1."""
    for i in range(len(city_ids)):
        if city_ids[i] == target_id: # search item by item until finding it
            return i
    return -1   # item is not in the list
        
def linear_search_recursive(city_ids, target_id, index=0): 
    """Performs a recursive linear search on a list of city IDs. Returns the index of target_id if found, otherwise -1."""
    if index == len(city_ids):
        return -1   # item is not in the list / Base case
    elif city_ids[index] == target_id:
        return index   # if you find, return index
    else:   # until finding, search item by item by using the same function and increasing index 1
        index += 1
        return linear_search_recursive(city_ids, target_id, index)
    
def binary_search_iterative(city_ids, target_id):
    """Performs an iterative binary search on a list of city IDs. Returns the index of target_id if found, otherwise -1."""
    left = 0
    right = len(city_ids) - 1

    while left <= right:  
        mid = (left + right) // 2 # for binary search we need to find mid point bc it checks half of the list each time 
        if city_ids[mid] == target_id:
            return mid  # Found it
        elif city_ids[mid] < target_id:
            left = mid + 1  # Target is on the right side, shift mid point to right
        else:
            right = mid - 1 # Target is on the left side, shift mid point to left
            
    return -1  # item is not in the list

def binary_search_recursive(city_ids, target_id, left, right):
    """Performs a recursive binary search on a list of city IDs. Returns the index of target_id if found, otherwise -1."""
    mid = (left + right) // 2 # for binary search we need to find mid point bc it checks half of the list each time 
    if left > right:
        return -1    # item is not in the list / Base case
    if city_ids[mid] == target_id:
            return mid
    elif city_ids[mid] > target_id:
        return binary_search_recursive(city_ids, target_id, left, mid-1) # Target is smaller than mid, move right to mid - 1
    elif city_ids[mid] < target_id:
        return binary_search_recursive(city_ids, target_id, mid+1, right) # Target is bigger than mid, move mid+1 to right

def load_cities_from_file(filename):
    """This function reads the data from the file named cities.txt and returns
    the cities dicitonary."""
    #Create an empty dicitonary.
    cities = {}
    
    #Open the file named cities.txt.
    infile = open(filename, 'r')
    for line in infile:
        city_id, name, country, population, tags = line.strip().split(",")
        cities[int(city_id)] = {"name" : name,
                      "country": country, 
                      "population": float(population), 
                      "tags" : set(tags.split(";"))
        }
    infile.close()
    return cities

def add_city(cities, city_id, name, country, population):
    """This functions add a new city to the dictionary named cities
    and prints a warning if the id already exists."""
   
    if city_id in cities:
        print("This id is already exists, enter a different one!")
    else:
        cities[city_id] = {"name" : name, #If the city id exists, the new city is added to the dicitonary.
                      "country": country, 
                      "population": population, 
                      "tags" : set()
                    }
        
def remove_city(cities, city_id):
    """This function removes the city with the given id from the dictionary and prints
    prints the current cities data.It prints a warning if city id does not exists."""

    if city_id not in cities:#Search for city id in cities dictionary. 
        print("There is no such a city id, please enter an existing one!")
    else:
        del cities[city_id]

def add_tag(cities, city_id, tag):
    """This function adds a tag to the given id from the dicitonary.
    If there is no such a id, it prints a warning."""

    if city_id not in cities:#Search for city id in cities dictionary.
        print("There is no such an id, please enter an existing one!")
    else:
        cities[city_id]["tags"].add(tag)

def remove_tag(cities, city_id, tag):
    """This funtions removes the given tag from the identified city's tag set.
    If there is no such an id and the tag is not found, it prints a warning."""

    if city_id not in cities:
        print("There is no such an id, please enter an existing one!")
    elif tag not in cities[city_id]["tags"] :
        print("There is no such a tag in the tags set, please enter an exisiting one!")
    else:
        cities[city_id]["tags"].remove(tag)

def print_cities(cities):
    """This function print the current data of the cities ficitonary in the 
    required format."""

    print("CityID | Name        | Country        | Population | Tags")
    print("-"*90)
    for city_id in sorted(cities):
        city = cities[city_id]

        tags_str = ""
        for tag in city["tags"]:
            tags_str += tag + ","
        if tags_str != "":
            tags_str = tags_str[:-1]


        print(f"{city_id}  |", 
              f"{city['name']:<11} |", 
              f"{city['country']:<14} |", 
              f"{city['population']:<10} |"
              f"{tags_str}")
        

def main():
    filename = "cities.txt"

    cities = load_cities_from_file(filename) # Load the data from cities.txt
    print_cities(cities)   # Print the initial cities data

    add_city(cities, 1011, "Madrid", "Spain", 3.4) # Add and remove at least one city
    add_city(cities, 1012, "Seoul", "South Korea", 9.6)
    remove_city(cities, 1001)
    print_cities(cities)  # Print the current cities data.

    add_tag(cities, 1002, "sunny") # Add and remove tags for at least one city
    remove_tag(cities, 1004, "historical")
    print_cities(cities) # Print the current cities data

    city_ids = sorted(list(cities.keys())) # For binary search, sortion of the list is mandatory
    target_id = 1005 # Need a targer to search

    """Call each search function one by one and print the results of each function."""
    linear_iterative = linear_search_iterative(city_ids, target_id) # returns index
    print(f"Target id: {target_id}, Index: {linear_iterative}")     # prints the result
    linear_recursive = linear_search_recursive(city_ids, target_id) # returns index
    print(f"Target id: {target_id}, Index: {linear_recursive}")     # prints the result
    binary_iterative = binary_search_iterative(city_ids, target_id) # returns index
    print(f"Target id: {target_id}, Index: {binary_iterative}")     # prints the result
    binary_recursive = binary_search_recursive(city_ids, target_id, 0, len(city_ids)-1) # returns index
    print(f"Target id: {target_id}, Index: {binary_recursive}")     # prints the result

if __name__ == "__main__":
    main()
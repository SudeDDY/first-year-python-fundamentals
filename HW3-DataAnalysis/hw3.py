"""320201049 - 320201097"""

def load_raw_lines(filename):      
    try:
        with open(filename, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        return [] 

#EXPLANATION:
"""I explained most of my codes step by step, but the main logic behind the finding top student is comparison by using 'for' loop. 
I defined a variable for max score and for each iteration, value was checked if the new score is bigger than the previous ones. 
If it was bigger, it saved this student's infos into the top student variable.""" #320201049

def clean_student_record(line):
    line = line.strip() # Clean and standardize whitespace / with strip method, cleaned spaces from both sides
    if not line:
        return None # Return None for malformed lines / if there is not line breaks the code
    parts = line.split(";") # sliced each part to execute different function on each of them and to convert tuple later
    if len(parts) != 3:
        return None # Return None for malformed lines / if parts are not 3, breaks the code
    clean_name = parts[0].strip().title() # Convert names to capitalized form / used "title" instead of "capitalize" because wanted to upper both name and surnames first letter 
    house_name = parts[1].strip()
    if house_name.lower().startswith("house "):
        house_name = house_name[6:].strip() # Extract the house name / if it is starting with "house" word, new version starts from other word
    try:
        score_info = parts[2].strip()
        score_info = score_info.split("=")
        score = int(score_info[1]) # Parse "score=NN" into an integer / sliced and converted score to an integer
        if score < 0 or score > 100: # Validate score is in [0, 100] / checks score's interval
            return None 
    except (IndexError, ValueError):
        return None # Return None for malformed lines / prevents errors and crushes
    return (clean_name, house_name, score) # creates tuple

def build_student_list(raw_lines):
    cleaned_list = [] # created a list to collect all cleaned tuples
    for line in raw_lines: # for each line
        result = clean_student_record(line) # cleans the lines
        if result is not None: 
            cleaned_list.append(result) # and adds them to the list as an item
    return cleaned_list

def compute_student_stats(students):
    total_students = len(students) # Total number of students
    passing_count = 0
    total_score_sum = 0
    max_score = -1
    top_student = None
    house_count = [] # empty list
    for clean_name, house_name, score in students: # for each students it will iterate
        total_score_sum += score # sums all scores
        if score >= 60: # Number of passing students (score ≥ 60) / counts passed students 
            passing_count += 1
        if score > max_score: # Top student / finds the student which has highest score
            max_score = score 
            top_student = clean_name , house_name , score
        # House distribution
        found = False  # to control the loop
        for i in range(len(house_count)): # loop for searching each house in the list
            if house_count[i][0] == house_name: # checks the house name
                current_count = house_count[i][1] #  count students per house
                new_tuple = (house_name, current_count + 1) # creates a new tuple 
                house_count[i] = new_tuple # adds tuple to the list's given index
                found = True  # house is in the list
                break
        if not found:  # if house doesnt exist, prevents the error and add house to the list with a student
            house_count.append((house_name, 1)) 
    if total_students > 0:
        average_score = total_score_sum / total_students # Average score / calculates the average of all students score
    else: # if no students exist
        average_score = "N/A"
        top_student = "N/A"
    house_count.sort() # sort alphabetically by house name
    return (total_students, passing_count, average_score, top_student, house_count)
    
def print_report(my_tuple):
    if len(my_tuple) == 5: 
        total_students, passing_count, average_score, top_student, house_count = my_tuple # unpacking the tuple
        print( "="*50 + "\n")
        print("-"*8," Student Performance ","-"*8)
        print(f"Number of students: {total_students}") # number of students
        print(f"Passing count: {passing_count}") # passing count
        if average_score == "N/A":   # “N/A” where appropriate
            print("Average Score: N/A")
        else:
            print(f"Average Score: {average_score:.1f}") # average score (1 decimal)
        if top_student == "N/A":   # “N/A” where appropriate
            print("Top Student: N/A")
        else:
            name, house, score = top_student # instead of printing as tuple, unpacking it
            print(f"Top Student: {name} ({house}, {score})")
        print("\n"+"-"*8," House Distribution ","-"*8)
        for house_name, count in house_count:
            print(f"{house_name}: {count}") # lists houses with their counts

    elif len(my_tuple) == 3:
        total_items, total_weight, heaviest_item = my_tuple
        print("\n"+"-"*8,"  Inventory Summary ","-"*8)
        print(f"Number of items: {total_items}") # number of items
        print(f"Total weight: {total_weight:.1f}")  # total weight (rounded to one decimal)
        if heaviest_item == "N/A":  # “N/A” where appropriate
            print("Heaviest item: N/A")
        else:
            print(f"Heaviest item: {heaviest_item}") # heaviest item
        print("\n" + "="*50 + "\n")

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

#EXPLANATION:
"""From this part of the program, the program processes the inventory list. Mainly, inventory lists contains tuples which are name-weight pairs. 
The whitespaces are stripped and unnwanted characters are removed. As for malformed lines, the program returns None.
At the end, total number of items/total weight/heaviest item are returned.""" #320201097

def clean_inventory_item(line):

    if line is None:
        return None
    line = line.strip() #Leading and trailing whitespaces are deleted.

    if line is "": 
        return None
    line = line.replace("*", "") #Unwanted characters are deleted.
    line = line.replace("-", " ") 

    if '|' not in line:
        return None
    parts = line.split("|")
    
    if len(parts) < 2:
        return None
    
    name_part = parts[0].strip()
    weight_part = parts[1].strip()

    if name_part =="" or weight_part =="":
        return None
    
    name = name_part.title()

   
    #This part cleans if wieght_part contains unnecessary items.
    weight_part = weight_part.lower()
    if 'kg' in weight_part:
        weight_part = weight_part.replace("kg", "") #
    if 'weight' in weight_part:
        weight_part = weight_part.replace("weight", "")
    if ':' in weight_part:
        weight_part = weight_part.replace(":", "")
    weight_part = weight_part.strip()
    
    #This part returns none if there is no weight part.
    try: 
        weight = float(weight_part)
    except ValueError:
        return None
    
    return(name, weight)

def build_inventory(raw_lines):
    #This function creates a list from raw lines/ skips malformed lines.
    
    list_inventory = [] #empty list

    for line in raw_lines:
        purified_item = clean_inventory_item(line) #The item was cleand by 'clean inventory item' function.
        if purified_item is not None:
            list_inventory.append(purified_item) #Cleaned items is added to the list_inventory.
    
    return list_inventory

def compute_inventory_stats(inventory):
    #This function carries out computing the statistics of total item/total weight/heaviest weigh.
    
    count = 0
    total_weight = 0.0
    heaviest_weight = 0.0
    heaviest_name = None # name, weight tuple is holded.

    for item in inventory:
        count = count + 1
        total_weight = total_weight + item[1]
        if heaviest_weight is None or item[1] > heaviest_weight:
            heaviest_name = item[0]
            heaviest_weight = item[1]


    if count == 0:
        heaviest_item = 'N/A'
    else:
        heaviest_item = (heaviest_name, heaviest_weight)

    return (count, total_weight, heaviest_item)

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------

def main():
    STUDENT_FILENAME = "student_data.txt" 
    INVENTORY_FILENAME = "inventory_data.txt"

    # calling student data part
    raw_lines = load_raw_lines(STUDENT_FILENAME)
    if raw_lines is None or not raw_lines:
        print("ERROR: Empty file!")
        return
    students = build_student_list(raw_lines)
    if not students:
        print("ERROR: Empty list!")
        return
    stats_tuple = compute_student_stats(students)
    print_report(stats_tuple)

    # calling inventory data part
    inventory_lines = load_raw_lines(INVENTORY_FILENAME)
    if inventory_lines is None or not inventory_lines:
        print("ERROR: Empty file!")
        return
    inventory = build_inventory(inventory_lines)
    if not inventory:
        print("ERROR: Empty list!")
        return
    inv_stats_tuple = compute_inventory_stats(inventory)
    print_report(inv_stats_tuple)

if __name__ == "__main__":
    main()

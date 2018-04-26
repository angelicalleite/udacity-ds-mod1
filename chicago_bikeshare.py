# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for i in range(20):
    print(data_list[i])

# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# Print the `gender` of the first 20 rows
for i in range(20):
    print(data_list[i][6])

print("\nTASK 2: Printing the genders of the first 20 samples")

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")


# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """
    Add the columns(index) of a list in another list in the same order
    Args:
        :data list for map
        :index index represent columns for map
    Returns:
        List of respective index of column informed
    """
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for item in data:
        column_list.append(item[index])
    return column_list


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[
    1] == "Male", "TASK 3: The list doesn't match."


# -----------------------------------------------------

def countElements(data, x):
    """
    Function count element in the list
    Args:
        :data list for count elements
        :x element for count ins the data
    Returns:
        Count elements find in the data
    """
    count = 0
    for ele in data:
        if ele == x:
            count += 1
    return count


def sumElements(data):
    """
    Function sum element in the list
    Args:
        :data list for sum elements
        :x element for sum ins the data
    Returns:
        sum elements find in the data
    """
    sum = 0
    for ele in data:
        sum += ele
    return sum


input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
gender = column_to_list(data_list, 6)
male = countElements(gender, "Male")
female = countElements(gender, "Female")

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")


# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """
        Count the genders in the list informed
        Args:
            :data_list list of gender
        Returns:
            List with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
    """
    gender = column_to_list(data_list, 6)
    male = countElements(gender, "Male")
    female = countElements(gender, "Female")
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")


# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """
    Get the most popular gender and print the gender as string
    Args:
        data_list: list of gender
    Returns:
        Print to "Male", "Female" or "Equal" as answer
    """
    male = count_gender(data_list)[0];
    female = count_gender(data_list)[1];

    return "Equal" if male == female else ("Male" if male > female else "Female")


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")


# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
def count_user_types(data_list):
    """
       Get types user of list by print in legend of map
       Args:
           data_list: list of user types
       Returns:
           Array with types user
    """
    user_types = column_to_list(data_list, 5)
    customer = countElements(user_types, "Customer")
    subscriber = countElements(user_types, "Subscriber")
    return [customer, subscriber]


print("\nTASK 7: Check the chart!")
user_types_list = column_to_list(data_list, 5)
types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantity by User Types')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = False
print("Answer:", answer)
print("List also contains empty elements, then the sum of masculine and feminine, does not equal total list elements")

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")


# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().

def median(list):
    """
       Get number median of list
       Args:
           list: list of number for calc
       Returns:
           Number result calc median of list
    """
    n = len(list)
    if n < 1:
        return None
    if n % 2 == 1:
        return sorted(list)[n // 2]
    else:
        return sumElements(sorted(list)[n // 2 - 1:n // 2 + 1]) / 2.0


def minmax(list):
    """
       Get number min and max of list
       Args:
           list: list of number for calc
       Returns:
           Array number result calc min and max of list
    """
    minimum = maximum = list[0]
    for i in list[1:]:
        if i < minimum:
            minimum = i
        else:
            if i > maximum: maximum = i
    return (minimum, maximum)


def mean(list):
    """
       Get number mean of list
       Args:
           list: list of number for calc
       Returns:
           Number result calc mean of list
    """
    return sumElements(map(int, list)) / len(list);


trip_duration_list = column_to_list(data_list, 2)
numbers = list(map(int, trip_duration_list));

min_trip = minmax(numbers)[0]
max_trip = minmax(numbers)[1]
mean_trip = mean(trip_duration_list)
median_trip = median(numbers)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set(column_to_list(data_list, 3))

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")


# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
def new_function(param1: int, param2: str) -> list:
    """
    Example function with annotations.
    Args:
        param1: The first parameter.
        param2: The second parameter.
    Returns:
        List of X values

    """


input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"


def count_items(column_list):
    """
    Analyze item and its respective count according to the reported column
    Args:
        column_list: list of respective column for analysis
    Returns:
        Set of available items and list respective count elements types
    """
    item_types = set(column_list)
    count_items = []

    for item in item_types:
        count_items.append(countElements(column_list, item))

    return item_types, count_items


if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------

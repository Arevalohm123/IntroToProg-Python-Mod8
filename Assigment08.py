# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# AArevalo, 2.19.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = "products.txt"
lstOfProductObjects = []
strStatus = ""  # Captures the status of an processing functions


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AArevalo, 2.19.2021, Modified code to complete assignment 8
    """
    # -- Constructor --
    def __init__(self, product_name, product_price):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

    # -- Properties
    # ProductName
    @property
    def product_name(self):
        return str(self.__product_name).title()

    # ProductPrice
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric():
            raise Exception("Product name cannot be a number!")
        else:
            self.__product_name = value

    @product_price.setter
    def product_price(self, value):
        if not value.isnumeric():
            raise Exception("Product price must be a string!")
        else:
            self.__product_price = value

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #


class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects): -> (list_of_product_objects)

        add_data_to_list(new_object, new_value, list_of_product_objects): -> (list_of_product_objects)

        read_data_from_file(file_name, list_of_product_objects): -> (list_of_product_objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        AArevalo, 2.19.2021, Modified code
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data to file

        :param file_name: file location of the to-do list
        :param list_of_product_objects: (list) of existing objects and values
        :return: list_of_product_objects: (list) of objects and values
        """
        obj_file = open(file_name, "w")
        for row in list_of_product_objects:
            obj_file.write(row[0] + "," + row[1] + "\n")
        obj_file.close()
        return list_of_product_objects

    @staticmethod
    def add_data_to_list(new_object, new_value, list_of_product_objects):
        """ Adds a new task and priority to the list of dictionary rows

        :param new_value: (str) new task you want to add
        :param new_object: (str) new priority you want to add
        :param list_of_product_objects: (list) of rows you want to display
        :return: list_of_product_objects: (list) of dictionary rows
        """
        new_row = (new_object, new_value)
        list_of_product_objects.append(new_row)
        print("\nObject has been successfully added!")
        return list_of_product_objects, 'Success'

    @staticmethod
    def read_data_from_file(file_name, list_of_product_objects):
        """ Reads data from a file into a list

        :param file_name: file location of the objects
        :param list_of_product_objects: (list) you want filled with file data:
        :return: list_of_product_objects: (list) of data
        """
        list_of_product_objects.clear()
        obj_file = open(file_name, "r")
        for line in obj_file:
            read_object, read_value = line.split(",")
            row = (read_object.strip(), read_value.strip())
            list_of_product_objects.append(row)
        obj_file.close()
        return list_of_product_objects, 'Success'


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks

    methods:
        print_menu_tasks():

        input_menu_choice():

        print_current_objects(list_of_product_objects)

        input_yes_no_choice(message):

        input_object_and_value():

        input_press_to_continue(optional_message=''):

    changelog: (When,Who,What)
        AArevalo, 3.6.2021, Modified code
    """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show the current data
        2) Add data to the list
        3) Save current data to file and exit    
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_objects(list_of_product_objects):
        """ Shows the current list objects and their values

        :param list_of_product_objects: (list) of rows you want to display
        :return: nothing
        """
        print("\n******* The current list of items are: *******")
        for row in list_of_product_objects:
            print(row)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_object_and_value():
        """ Gets the input from user on the new object and value

        :return: new_object: (string) input from user on new object
        :return: new_value: (string) input from user on new value
        """
        new_object = str(input("\nWhat object would you like to add? :")).strip()
        new_value = str(input("What is the value in dollars?")).strip()
        return new_object, new_value

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from products.txt.


FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)  # read file data

while True:
    # Step 2 - Display a menu of choices to the user
    IO.print_current_objects(lstOfProductObjects)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 3 Show current data
    if strChoice.strip() == '1':  # Show Current List
        IO.print_current_objects(lstOfProductObjects)  # Show current data in the list/table
        continue   # to show the menu

    # Step 4 - Adding a new object to the list
    elif strChoice.strip() == '2':  # Add a new object
        obj = Product
        Product.product_name, Product.product_price = IO.input_object_and_value()
        FileProcessor.add_data_to_list(Product.product_name, Product.product_price, lstOfProductObjects)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    # Step 5 - Saving the data and exiting
    elif strChoice == '3':  # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            IO.input_press_to_continue("File Saved!")
        else:
            IO.input_press_to_continue("Save Cancelled!")
        break  # Exit program

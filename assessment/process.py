"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv


def load_data(filepath):
    """
    Load data from a CSV file and return it as a list of dictionaries.
    Each row in the CSV becomes a dictionary with column names as keys.
    
    What: Reads the CSV file and converts it to a list of dictionaries
    Why: We need the data in memory to analyze it. Dictionaries make it easy
         to access data by column name (e.g., row['Rating'])
    
    Args:
        filepath (str): The path to the CSV file to load
        
    Returns:
        list: A list of dictionaries, where each dictionary represents a row
              from the CSV file. Each dictionary has keys matching the CSV
              column headers.
    
    Example:
        data = load_data('data/disneyland_reviews.csv')
        # data[0] might be: {'Review_ID': '670772142', 'Rating': '4', ...}
    """
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            # csv.DictReader automatically uses the first row as keys
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

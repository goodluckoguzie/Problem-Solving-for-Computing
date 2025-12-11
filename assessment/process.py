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


def filter_reviews_by_park(data, park_name):
    """
    Filter reviews to get only those for a specific park.
    
    What: Goes through all reviews and selects ones matching the park name
    Why: User wants to see reviews for a specific park (Task 7)
    
    Args:
        data (list): The list of all reviews
        park_name (str): The name of the park to filter by
        
    Returns:
        list: A list of reviews (dictionaries) for the specified park
    """
    filtered_reviews = []
    # Convert input to lowercase for case-insensitive comparison
    target_park = park_name.lower()
    
    for review in data:
        # Get the branch (park name) from the review
        # Use .get() to safely access the dictionary key, returning empty string if missing
        branch = review.get('Branch', '').lower()
        
        # Check if the target park name is in the branch name
        if target_park in branch:
            filtered_reviews.append(review)
            
    return filtered_reviews


def count_reviews_by_park_and_location(data, park_name, location):
    """
    Count how many reviews a park received from a specific location.
    
    What: Filters by park and location, then counts the results
    Why: User wants to know review volume from specific locations (Task 8)
    
    Args:
        data (list): The list of all reviews
        park_name (str): The name of the park
        location (str): The reviewer's location
        
    Returns:
        int: The number of matching reviews
    """
    count = 0
    target_park = park_name.lower()
    target_location = location.lower()
    
    for review in data:
        branch = review.get('Branch', '').lower()
        reviewer_location = review.get('Reviewer_Location', '').lower()
        
        if target_park in branch and target_location in reviewer_location:
            count += 1
            
    return count


def calculate_average_rating_by_year(data, park_name, year):
    """
    Calculate the average rating for a park in a specific year.
    
    What: Finds reviews for park/year, sums ratings, divides by count
    Why: Track park performance over time (Task 9)
    
    Args:
        data (list): The list of all reviews
        park_name (str): The name of the park
        year (str): The year to filter by
        
    Returns:
        float: The average rating, or 0 if no reviews found
    """
    total_rating = 0
    count = 0
    target_park = park_name.lower()
    target_year = str(year)
    
    for review in data:
        branch = review.get('Branch', '').lower()
        # Year_Month is in format "YYYY-M" or "YYYY-MM"
        review_date = review.get('Year_Month', '')
        
        # Check if park matches and date starts with the year
        if target_park in branch and review_date.startswith(target_year):
            try:
                rating = int(review.get('Rating', 0))
                total_rating += rating
                count += 1
            except ValueError:
                # Skip if rating is not a valid number
                continue
                
    if count == 0:
        return 0
        
    return total_rating / count



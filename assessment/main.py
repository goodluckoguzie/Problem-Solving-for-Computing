"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""
import tui
import process


def main():
    """
    Main function that controls the program flow.
    This function:
    1. Displays welcome message
    2. Loads the data from CSV file
    3. Runs a continuous loop showing menus and handling user choices
    4. Exits when user chooses to exit
    """
    # Task 1: Display welcome message
    tui.display_welcome()
    
    # Task 2: Load data from CSV file
    # The filepath is relative to where main.py is located
    filepath = "data/disneyland_reviews.csv"
    data = process.load_data(filepath)
    
    # Display confirmation message with row count
    if data:
        row_count = len(data)
        tui.display_message(f"✓ Data loaded successfully!")
        tui.display_message(f"✓ Total number of reviews: {row_count:,}")
    else:
        tui.display_error("Failed to load data. Please check the file path.")
        return
    
    # Task 5: Continuous program loop
    # This loop keeps the program running until user chooses to exit
    # Definition: A while loop repeats code as long as a condition is True
    running = True
    while running:
        # Task 3: Display main menu
        tui.display_main_menu()
        
        # Get user's menu choice
        choice = tui.get_menu_choice()
        
        # Task 4: Validate user input and confirm choice
        if choice == 'A':
            tui.display_message("You selected: [A] View Data")
            handle_view_data_menu(data)
        elif choice == 'B':
            tui.display_message("You selected: [B] Visualise Data")
            handle_visualise_menu(data)
        elif choice == 'C':
            tui.display_message("You selected: [C] Export Data")
            handle_export_menu(data)
        elif choice == 'X':
            tui.display_message("Thank you for using the Disneyland Reviews Analysis System!")
            tui.display_message("Goodbye!")
            running = False  # Exit the loop
        else:
            # Invalid input - show error message
            tui.display_error(f"Invalid choice '{choice}'. Please enter A, B, C, or X.")


def handle_view_data_menu(data):
    """
    Handle the View Data sub-menu (Task 6).
    This function displays the sub-menu and processes user choices for Section A features.
    
    Args:
        data (list): The loaded dataset
    """
    while True:
        tui.display_view_data_menu()
        sub_choice = tui.get_submenu_choice()
        
        if sub_choice == '1':
            # Task 7: Display all reviews for a park (will be implemented in Phase 2)
            tui.display_message("Feature coming soon: Display all reviews for a park")
        elif sub_choice == '2':
            # Task 8: Count reviews by park and location (will be implemented in Phase 2)
            tui.display_message("Feature coming soon: Count reviews by park and location")
        elif sub_choice == '3':
            # Task 9: Average rating by park and year (will be implemented in Phase 2)
            tui.display_message("Feature coming soon: Average rating by park and year")
        elif sub_choice == '4':
            # Task 13: Average score per park by location (will be implemented in Phase 4)
            tui.display_message("Feature coming soon: Average score per park by location")
        elif sub_choice == 'X':
            break  # Return to main menu
        else:
            tui.display_error(f"Invalid choice '{sub_choice}'. Please enter 1-4 or X.")


def handle_visualise_menu(data):
    """
    Handle the Visualise Data sub-menu (Task 6).
    This function displays the sub-menu and processes user choices for Section B features.
    
    Args:
        data (list): The loaded dataset
    """
    while True:
        tui.display_visualise_menu()
        sub_choice = tui.get_submenu_choice()
        
        if sub_choice == '1':
            # Task 10: Pie chart - Reviews per park (will be implemented in Phase 3)
            tui.display_message("Feature coming soon: Pie chart - Reviews per park")
        elif sub_choice == '2':
            # Task 11: Bar chart - Top 10 locations (will be implemented in Phase 3)
            tui.display_message("Feature coming soon: Bar chart - Top 10 locations by rating")
        elif sub_choice == '3':
            # Task 12: Bar chart - Average rating by month (will be implemented in Phase 3)
            tui.display_message("Feature coming soon: Bar chart - Average rating by month")
        elif sub_choice == 'X':
            break  # Return to main menu
        else:
            tui.display_error(f"Invalid choice '{sub_choice}'. Please enter 1-3 or X.")


def handle_export_menu(data):
    """
    Handle the Export Data sub-menu (Task 14).
    This function displays the sub-menu and processes user choices for Section D export feature.
    
    Args:
        data (list): The loaded dataset
    """
    while True:
        tui.display_export_menu()
        sub_choice = tui.get_submenu_choice()
        
        if sub_choice == '1':
            # Task 14: Export as TXT (will be implemented in Phase 4)
            tui.display_message("Feature coming soon: Export as TXT")
        elif sub_choice == '2':
            # Task 14: Export as CSV (will be implemented in Phase 4)
            tui.display_message("Feature coming soon: Export as CSV")
        elif sub_choice == '3':
            # Task 14: Export as JSON (will be implemented in Phase 4)
            tui.display_message("Feature coming soon: Export as JSON")
        elif sub_choice == 'X':
            break  # Return to main menu
        else:
            tui.display_error(f"Invalid choice '{sub_choice}'. Please enter 1-3 or X.")


# This is the entry point of the program
# When you run main.py, Python will execute the code below
if __name__ == "__main__":
    main()


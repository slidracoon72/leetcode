from database_manager import DatabaseManager
from json_reader import read_json
from html_generator import generate_html


def main():
    """
    Main function to execute the program.

    Returns:
        None
    """
    # Read data from JSON file.
    courses_data = read_json('courses.json')

    # Create DatabaseManager instance (Singleton).
    db_manager = DatabaseManager()

    # Create the 'courses' table.
    db_manager.create_table()
    print("Table 'courses' created!")

    # Prepare data for insertion into the 'courses' table.
    row_data = [(course['semester'], course['course'], course['instructor'], course['location']) for course in
                courses_data]
    # Insert data into the 'courses' table.
    db_manager.insert_data(row_data)
    print("Data inserted into 'courses' table!")

    # Fetch data from the 'courses' table.
    fetched_data = db_manager.fetch_data()
    print("Fetched Data:", fetched_data)

    # Generate HTML content using the fetched data.
    html_content = generate_html(fetched_data)

    # Write HTML content to 'courses.html'.
    with open('courses.html', 'w') as html_file:
        html_file.write(html_content)
    print("HTML file 'courses.html' created!")


if __name__ == '__main__':
    main()

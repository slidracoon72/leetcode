from jinja2 import Template


def generate_html(data):
    """
    Generate HTML content using a Jinja2 template.

    Args:
        data (list): List of tuples containing course information.

    Returns:
        str: HTML content as a string.
    """
    # HTML template for rendering the data in a table format.
    html = '''
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                table {
                    border-collapse: collapse;
                    width: 50%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 8px;
                    text-align: left;
                }
                th {
                    background-color: #000;
                    color: #FFF;
                }
            </style>
        </head>
        <body>
            <h1>Software Engineering - Final Exam</h1>
            <h2>Courses Information</h2>
            <table>
                <tr>
                    <th>Semester</th>
                    <th>Course</th>
                    <th>Instructor</th>
                    <th>Location</th>
                </tr>
                {% for row in data %}
                    <tr>
                        <td>{{ row[1] }}</td>
                        <td>{{ row[2] }}</td>
                        <td>{{ row[3] }}</td>
                        <td>{{ row[4] }}</td>
                    </tr>
                {% endfor %}
            </table>
        </body>
        </html>
    '''
    template = Template(html)
    return template.render(data=data)

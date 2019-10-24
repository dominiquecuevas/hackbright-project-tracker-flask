"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    # github = "jhacks"

    github =  request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)
    list_of_tuples = hackbright.get_grades_by_github(github)

    # return "{} is the GitHub account for {} {}".format(github, first, last)
    return render_template('student_info.html', first=first, last=last, 
                            github=github, rows=list_of_tuples)

@app.route("/student-search")
def search_student():
    return render_template('student_search.html')


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    github = request.form.get('git')
    hackbright.make_new_student(first_name, last_name, github)
    return render_template('add_results.html', github=github)


@app.route("/add")
def to_add():
    return render_template('new_student.html')

@app.route("/project")
def get_project():

    ptitle = request.args.get('project_title')
    title, description, max_grade = hackbright.get_project_by_title(ptitle)

    return render_template('project.html',
                            title=title,
                            description=description,
                            max_grade=max_grade)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)

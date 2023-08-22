from flask import Flask, render_template, jsonify
from database import load_data

app = Flask(__name__)
# get data from database
data = load_data()

about_spa = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
                anim id est laborum.'''
tabs = ["Home", "Vacancies", "About Us", "Contact Us"]

@app.route("/")
def index():
    return render_template("home.html", Jobs=data, about=about_spa, company_name="JOBSPa", tabs=tabs)

@app.route("/api/jobs")
def get_jobs():
    return jsonify({
        'data': data,
        'totalCount': len(data),
        'success': True
    })

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
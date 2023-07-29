from flask import Flask, render_template

app = Flask(__name__)

# Dummy data
data = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Texas US",
        "salary": '120,500 usd'
    },
    {
        "id": 2,
        "title": "System Analyst",
        "location": "Washington DC US",
    },
    {
        "id": 3,
        "title": "Backend Engineer",
        "location": "Remote",
        "salary": '140,500 usd'
    },
    {
        "id": 4,
        "title": "Frontend Engineer",
        "location": "Toronto",
        "salary": '130,500 usd'
    },
]
about_spa = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
                incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
                exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
                dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
                anim id est laborum.'''

@app.route("/")
def index():
    return render_template("home.html", Jobs=data, about=about_spa)

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
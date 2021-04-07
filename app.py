#Import flask from library
from flask import Flask
from flask import render_template
from markupsafe import escape
#init the flask app server
app = Flask(__name__,static_url_path='',static_folder='static')
app.config.from_object(__name__)

#When user access root URL: example.com/
@app.route('/')
def index():
    title="Hung's cave"
    name="Hello"
    content="Welcome the app"
    #passing title, name and content variable to index.html {{title}}, {{name}}, {{content}}
    return render_template('index.html', title=title, name=name, content=content)

#add another route function name must be different
@app.route('/whois/<name>')
#take the data from <name>
def showinfo(name):
    #pass <name> data to name variable by escape(name)
    if escape(name)=="hung":
        return render_template('index.html', title="Whois Information", name="Duong Dang Hung", content="He is a SIMP, horny, toxic guy")
    if escape(name)=="minh":
        return render_template('index.html', title="Who is Minh", name="Nguyen Hoang Minh aka Mom Long 2", content="Donkey, idiot sandwich, sleep overnoon, always late")
    else:
        return render_template('index.html',title="Not found",name="Not found",content="Sorry we don't know him")

#still taking the variable height but double the value. define height as integer
@app.route('/doublemyheight/<int:height>')
def show_height(height):
    doubleh = height * 2
    return "Your doubled height is: " + str(doubleh)

#main function will exec first (run directly without flask run)
if __name__ == "__main__":
    app.run(debug=True)
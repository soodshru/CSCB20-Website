from flask import Flask
app = Flask (__name__)

@app.route('/<name>')
def  generateResponse(name):
        if name.isupper() == 0 :
            WelcomeName = name.upper();
        elif name.islower() == 0 :
            WelcomeName = name.lower();
        return "Welcome, "+WelcomeName+", to my CSCB20 website!";

# run the app when app.py is run
if __name__ == '__main__':
    app.run(debug = True)
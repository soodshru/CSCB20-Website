from flask import Flask
app = Flask (__name__)

@app.route('/<name>')
@app.route('/')
def  generateResponse(name = ''):
        #case where no name is passed
        if (name == ''):
            WelcomeName = "Unknown";
        #cases where some name is passed
        elif (name.isupper() and name.isalpha()):
            WelcomeName = name.lower();
        elif (name.islower() and name.isalpha()) :
            WelcomeName = name.upper();
        elif (name.isalpha()):
            WelcomeName = name;
        else :
            newName = ""
            for a in name :
                if a.isalpha() :
                    newName += a
            WelcomeName = newName;
        return "Welcome, "+WelcomeName+", to my CSCB20 website!";


# run the app when question1.py is run
if __name__ == '__main__':
    app.run()
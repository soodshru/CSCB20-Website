from flask import Flask
app = Flask (__name__)

@app.route('/')
def login():
    return render_template('')

# run the app when app.py is run
if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template
import json 

data = {}
with open('data.txt') as json_file:  
    data = json.load(json_file)

print(data['1793'])

app = Flask(__name__)

@app.route('/')
def render():
    return render_template('myfile.html',data=data)

if __name__=='__main__':
    app.run()
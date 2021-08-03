from flask import Flask, jsonify, request
import datetime
# creating a Flask app
app = Flask(__name__)
ct = datetime.datetime.now()
ct = ct.timestamp()  
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/')
def home():
    data = ct
    return jsonify({'value': data})
    
  
        

if __name__ == '__main__':
      
    app.run(debug = False)        

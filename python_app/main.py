from flask import Flask # importing the flask class
app = Flask(__name__) # creating an instance of the Flask class
 
@app.route('/') #
def hello_world(): 
    return 'Hello Wiley'
 
if __name__ == '__main__':
    app.run(host= '0.0.0.0', debug=True) 

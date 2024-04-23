from flask import Flask
app=Flask(__name__)
@app.route("/") #when the URL slash (root URL) is accessed, show Hello World
def hello():
    return "<p> Hello!World</p>"
if __name__=="__main__":
    app.run(debug=True)


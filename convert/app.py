from flask import Flask, render_template, request
import  json

app = Flask(__name__)

def binr(test_str): 
  res = ''.join(format(ord(i), '08b') for i in test_str)
  return res

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/convert")
def convert():
  userText = request.args.get('user-text')
  result = {}
 
  result["value"] = binr(userText)

  return json.dumps(result) # dict to 


if __name__ == "__main__":
  app.run(port=10000, debug=True)
  #app.run(port =10319,debug=True)
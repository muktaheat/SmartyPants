from flask import Flask, render_template
#from src.common.database import Database
#request, session

app = Flask(__name__)


values = []
f = open('data.txt', 'r+')
for line in f:
    values.append(float(line))
f.close()
a = values[-1]


@app.route('/')
def driver():
    if(a<23):
        name = 'Full'
        return render_template("driver.html", name=name)
    else:
        name = 'Empty'
        return render_template("driver.html", name=name)



if __name__ == "__main__":
    app.run(port=4995)
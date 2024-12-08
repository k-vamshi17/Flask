from flask import Flask
app=Flask(__name__)
@app.route('/hello')
def hello_world():
    return "Hello World"

@app.route("/hello1")
def hello_world1():
    output='''<body bgcolor=cyan>
    <h2>Hello This is first Flask Application</h2>
    </body>'''
    return output

def hello_world2():
    output='''<body bgcolor=aqua>
    <h2>Hello This is First Flask Application</h2>
    </body>'''
    return output
app.add_url_rule('/hello2','hello_world2',hello_world2)
app.run()
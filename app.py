from flask import Flask
app=Flask('_MANI_')
@app.route('/')
def hello_world():
    return 'hello from flask'
if __name__=='__main__':
    app.run (debug = True,host='0.0.0.0')
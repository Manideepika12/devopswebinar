from flask import Flask#hello world
app=Flask('_MANI_')
@app.route('/')
def hello_world():
    strr="Checkout new branch"
    return 'hello from flask'+strr
if __name__=='__main__':
    app.run (debug = True,host='0.0.0.0')

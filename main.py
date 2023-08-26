from flask import Flask,render_template

app= Flask(__name__,template_folder='templates')

@app.route('/')
def fun():
    return render_template('tt.html')

if __name__=='__main__':
    app.run()
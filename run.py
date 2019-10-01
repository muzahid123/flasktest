import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')
def content():
    errors = []
    content = []
    try:
        file = request.args.get('file')
        start = int(request.args.get('start'))
        end = int(request.args.get('end'))
        with open(file, encoding="utf8", errors='ignore') as fp:
           line = fp.readline()
           cnt = 1
           while line:
               if start <= cnt and end >= cnt:
                   content.append(line.strip())
               line = fp.readline()
               cnt += 1
    except Exception as e:
        errors.append(e)
        content.append("error occurs")
    return render_template('index.html', errors=errors, text=content)
    
    
 
if __name__ == '__main__':
	app.run(debug=True)

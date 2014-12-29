from flask import Flask, jsonify, render_template

app = Flask(__name__)
app.config.from_object('conf')


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/data')
def names():
    data = {
	"first_names": ["John", "Jacob", "Julie", "Jennifer"],
	"last_names": ["Connor", "Johnson", "Cloud", "Ray"]
	}
    return jsonify(data)

if __name__ == '__main__':
    app.run()

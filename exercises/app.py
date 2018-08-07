from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
fav_players = ["messi", "mohammad salah", "michael phelps"]
def home_page():
	return render_template("index.html")
for i in range (3):
	


if __name__ == '__main__':
	app.run(debug = True)

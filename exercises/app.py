from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def home_page():
	fav_players = ["messi", "mohammad salah", "michael phelps"]
	likes_same_sport = False
	return render_template(
		"index.html",
		fav_players=fav_players,
		likes_same_sport=likes_same_sport)



if __name__ == '__main__':
	app.run(debug = True)

from flask import Flask, render_template, request
from cat_data import cats

app = Flask(__name__)

def score_cat(cat, preferences):
    score = 0
    for trait, value in preferences.items():
        if trait == "hair_length":
            score += 1 if cat["traits"]["hair_length"] == value else 0
        else:
            score += cat["traits"].get(trait, 0) * value
    return score

@app.route('/')
def index():
    return render_template('quiz.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        preferences = {
            "good_with_kids": 1.0 if request.form.get("kids") == "yes" else 0.0,
            "good_with_other_animals": 1.0 if request.form.get("animals") == "yes" else 0.0,
            "affectionate": 1.0 if request.form.get("cuddle") == "cuddly" else 0.0,
            "independent": 1.0 if request.form.get("cuddle") == "independent" else 0.0,
            "hair_length": request.form.get("hair_length")
        }

        scored = [(cat, score_cat(cat, preferences)) for cat in cats]
        scored.sort(key=lambda x: x[1], reverse=True)
        recommendations = [c[0] for c in scored[:3]]

        return render_template('results.html', recommendations=recommendations)

    return render_template('quiz.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

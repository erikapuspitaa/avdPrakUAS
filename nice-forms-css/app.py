from flask import Flask, render_template, request

app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve form data
    bermain_game = int(request.form['bermain_game'])
    durasi_bermain = int(request.form['durasi_bermain'])
    durasi_waktu_bermain = int(request.form['durasi_waktu_bermain'])
    pilihan_pertama_stress = int(request.form['pilihan_pertama_stress'])
    membantu_mengalihkan_stress = int(request.form['membantu_mengalihkan_stress'])

    # Perform your prediction logic here
    # For simplicity, let's assume a basic prediction based on the sum of selected options
    prediction_score = bermain_game + durasi_bermain + durasi_waktu_bermain + pilihan_pertama_stress + membantu_mengalihkan_stress

    # Map the prediction score to a classification
    if prediction_score >= 12:
        prediction_text = "Sangat Setuju"
    elif prediction_score >= 8:
        prediction_text = "Setuju"
    elif prediction_score >= 4:
        prediction_text = "Netral"
    else:
        prediction_text = "Tidak Setuju"

    # Render the result in the template
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == '_main_':
    app.run(debug=True)
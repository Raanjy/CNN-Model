app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Preprocess the input data
    input_data = np.array(data['input']).reshape((1, -1))  # Adjust shape as needed
    prediction = model.predict(input_data)
    response = {
        'prediction': prediction.tolist()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

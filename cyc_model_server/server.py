from flask import Flask, jsonify, request, abort
from utils import load_pkl_model, check_payload, get_precition

app = Flask(__name__)
MODEL_NAME = './models/model1.pkl'


@app.route('/')
def home():
    """This function just responds to the browser URL.
    """
    return "Home page"


@app.route('/api', methods=['POST', 'GET'])
def api():
    """This is the endpoint of api calls.
    """

    if request.method == 'POST':
        try:  # we want json
            payload = request.get_json(force=True)  # convert it to dict
            data = payload['data']  # `data` is a dict
        except Exception as e:
            print(e)
            abort(400)

        # let's load the model first
        model = load_pkl_model(MODEL_NAME)

        # payload received, let's turn it to proper format
        # e.g., check for whether we have all the features needed
        inputs = check_payload(model, data)

        # combine the input and model
        pred = get_precition(model, inputs)  # `pred` is a dict

        return jsonify(pred)

    else:  # GET, print some info about the model
        return jsonify({
            'model_name': MODEL_NAME,
            'feature_names': ['feature_1', 'feature_2']
        })


if __name__ == '__main__':
    app.run(debug=True, port=5050)

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
@app.route('/home')
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
            message = payload['message']  # `data` is a dict
        except Exception as e:
            print(e)
            abort(400)

        return jsonify({
          'message': message
        })

    else:  # GET, print some info about the model
        return jsonify({
            'message': 'what a wonderful world!'
        })

if __name__ == '__main__':
    app.run(debug=True, port=5050)

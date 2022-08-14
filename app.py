from flask import Flask, jsonify, render_template

app = Flask(__name__, template_folder='')

from services import calculate_fibonacci, get_valid_numbers, upload_valid_numbers

""" Swagger """
@app.route('/', methods=['GET'])
def get_swagger():
    return render_template('index.html', base_url='/')


""" GET serie of fibonacci with limit parameter """
@app.route('/fibonacci/<int:item_end>', methods=['GET'])
def get_fibonacci(item_end):
    return jsonify({"fibonacci_serie": calculate_fibonacci(item_end)})


""" GET valid_numbers of file_fibonnacci.json that were save"""
@app.route('/valid_numbers', methods=['GET'])
def valid_numbers():
    return get_valid_numbers()


""" DELETE valid_numbers of file_fibonnacci.json that were save"""
@app.route('/fibonacci/<int:item_end>', methods=['DELETE'])
def delete_product(item_end):
    return jsonify({"message": upload_valid_numbers(item_end, False)})


""" VALIDATE that the service is running"""
@app.route('/healcheck')
def healcheck():
    return jsonify({"message": "service is running"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)

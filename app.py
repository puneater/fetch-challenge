from flask import Flask, jsonify, request
import uuid
from points_calculator import calculate_points

app = Flask(__name__)

receipt_data = dict()   # local datastore for receipts


@app.route("/receipts/process", methods=['POST'])
def process_receipts():
    global receipt_data
    generated_id = str(uuid.uuid4())
    receipt_data[generated_id] = request.get_json()

    return jsonify({
        'id': generated_id
    })


@app.route("/receipts/<receipt_id>/points", methods=['GET'])
def get_points(receipt_id):
    global receipt_data
    return jsonify({
        'points': calculate_points(receipt_data[str(receipt_id)])
    })


if __name__ == '__main__':
    app.run()

from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

receipt_data = dict()   # local datastore


@app.route("/receipts/process", methods=['POST'])
def process_receipts():
    generated_id = str(uuid.uuid4())
    receipt_data[generated_id] = request.get_json()
    return jsonify({'id': generated_id})


if __name__ == '__main__':
    app.run()

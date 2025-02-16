from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated contract store
contracts = {
    "customer_profile": {
        "version": "1.0.0",
        "schema": {
            "fields": [
                {"name": "customer_id", "type": "string"},
                {"name": "email", "type": "string"}
            ]
        }
    }
}

@app.route('/contracts/<contract_id>', methods=['GET'])
def get_contract(contract_id):
    contract = contracts.get(contract_id)
    if contract:
        return jsonify(contract)
    else:
        return jsonify({"error": "Contract not found"}), 404

@app.route('/contracts', methods=['POST'])
def add_contract():
    new_contract = request.json
    contract_id = new_contract.get("id")
    if contract_id in contracts:
        return jsonify({"error": "Contract already exists"}), 400
    contracts[contract_id] = new_contract
    return jsonify(new_contract), 201

if __name__ == '__main__':
    app.run(debug=True, port=8000) 
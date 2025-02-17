from flask import Flask, jsonify, request
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Simulated stores
contracts = {
    "customer_profile": {
        "version": "1.0.0",
        "schema": {
            "fields": [
                {"name": "customer_id", "type": "string"},
                {"name": "email", "type": "string"}
            ]
        },
        "producer": "retail-data-team",
        "status": "active"
    }
}

# Store for subscriptions
subscriptions = {
    "customer_profile": {
        "consumers": [
            {
                "team": "data-science-team",
                "contact": "ds-team@company.com",
                "notification_url": "http://ds-team-webhook/notifications"
            }
        ]
    }
}

# Store for notifications history
notifications_history = []

def notify_consumers(contract_id, event_type, details):
    """Simulate async notification to consumers"""
    if contract_id in subscriptions:
        notification = {
            "timestamp": datetime.utcnow().isoformat(),
            "contract_id": contract_id,
            "event_type": event_type,
            "details": details
        }
        notifications_history.append(notification)
        # In real implementation, would make HTTP calls to notification_urls
        print(f"Notifying consumers of {contract_id}: {event_type}")

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
    notify_consumers(contract_id, "contract_created", new_contract)
    return jsonify(new_contract), 201

@app.route('/contracts/<contract_id>/subscribe', methods=['POST'])
def subscribe_to_contract(contract_id):
    if contract_id not in contracts:
        return jsonify({"error": "Contract not found"}), 404
    
    subscription = request.json
    if contract_id not in subscriptions:
        subscriptions[contract_id] = {"consumers": []}
    
    subscriptions[contract_id]["consumers"].append(subscription)
    return jsonify({"message": "Subscription successful"}), 201

@app.route('/contracts/<contract_id>/subscribers', methods=['GET'])
def get_subscribers(contract_id):
    if contract_id not in subscriptions:
        return jsonify({"consumers": []}), 200
    return jsonify(subscriptions[contract_id])

@app.route('/contracts/<contract_id>/deprecate', methods=['POST'])
def deprecate_contract(contract_id):
    if contract_id not in contracts:
        return jsonify({"error": "Contract not found"}), 404
    
    deprecation_info = request.json
    contracts[contract_id]["status"] = "deprecated"
    contracts[contract_id]["deprecation_info"] = deprecation_info
    
    notify_consumers(contract_id, "contract_deprecated", deprecation_info)
    return jsonify({"message": "Contract deprecated successfully"})

@app.route('/notifications/history', methods=['GET'])
def get_notifications_history():
    return jsonify(notifications_history)

# Simulation d'un cache simple
cache = {}

def cache_cleanup():
    """Simulate cache cleanup every 5 minutes"""
    while True:
        time.sleep(300)
        cache.clear()
        print("Cache cleaned")

# Start cache cleanup in background
cleanup_thread = threading.Thread(target=cache_cleanup, daemon=True)
cleanup_thread.start()

if __name__ == '__main__':
    app.run(debug=True, port=8000) 
from flask import Flask, request, jsonify

app = Flask(__name__)

subscriptions = {}

@app.route("/subscription/<user_id>", methods=["GET"])
def get_subscription(user_id):
    if user_id not in subscriptions:
        return jsonify({"error": "Subscription not found"}), 404

    return jsonify({
        "user_id": user_id,
        "subscription": subscriptions[user_id]
    }), 200


@app.route("/subscription", methods=["POST"])
def create_or_update_subscription():
    data = request.get_json()

    user_id = data.get("user_id")
    plan = data.get("plan")

    if not user_id or not plan:
        return jsonify({"error": "user_id and plan are required"}), 400

    subscriptions[user_id] = {
        "plan": plan
    }

    print("Received subscription request:", data)

    return jsonify({
        "message": "Subscription saved successfully",
        "user_id": user_id,
        "subscription": subscriptions[user_id]
    }), 200


if __name__ == "__main__":
    app.run(port=8009, debug=True)

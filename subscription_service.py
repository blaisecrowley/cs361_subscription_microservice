from flask import Flask, request, jsonify

app = Flask(__name__)

subscriptions = {}

@app.route("/subscription/<username>", methods=["GET"])
def get_subscription(username):
    if username not in subscriptions:
        return jsonify({"error": "Subscription not found"}), 404

    return jsonify({
        "username": username,
        "subscription": subscriptions[username]
    }), 200


@app.route("/subscription", methods=["POST"])
def create_or_update_subscription():
    data = request.get_json()

    username = data.get("username")
    plan = data.get("plan")

    if not username or not plan:
        return jsonify({"error": "username and plan are required"}), 400

    subscriptions[username] = {
        "plan": plan
    }

    return jsonify({
        "message": "Subscription saved successfully",
        "username": username,
        "subscription": subscriptions[username]
    }), 200


if __name__ == "__main__":
    app.run(port=5003, debug=True)

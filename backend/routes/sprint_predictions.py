from flask import Blueprint, request, jsonify
from controllers.sprint_predictions_controller import create_sprint_prediction, get_all_sprint_predictions, get_sprint_prediction_by_id, update_sprint_prediction, delete_sprint_prediction
from controllers.sprints_controller import check_if_sprint_exists
from controllers.auth_controller import check_if_user_exists

sprint_predictions_bp = Blueprint("sprint_predictions", __name__)


@sprint_predictions_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    if not check_if_sprint_exists(data["sprint_id"]):
        return jsonify({"message": "Sprint not found"}), 404
    if not check_if_user_exists(data["user_id"]):
        return jsonify({"message": "User not found"}), 404
    result = create_sprint_prediction(data)
    if "error" not in result:
        return jsonify({"message": "Sprint Prediction Created Successfully", "sprint_prediction": result}), 201
    print(result["error"])
    return jsonify({"message": f"Error Creating Sprint Prediction - Problem with field {result['error']}"}), 400

@sprint_predictions_bp.route("/", methods=["GET"])
def get_all():
    sprint_predictions = get_all_sprint_predictions()
    return jsonify({"message":"Successfully retrieved sprint predictions", "sprint_predictions": sprint_predictions}), 200

@sprint_predictions_bp.route("/<int:sprint_prediction_id>", methods=["GET"])
def get_one(sprint_prediction_id):
    sprint_prediction = get_sprint_prediction_by_id(sprint_prediction_id)
    if sprint_prediction:
        return jsonify({"message": f"Successfully retrieved sprint prediction", "sprint_prediction": sprint_prediction}), 200
    return jsonify({"message": "Sprint Prediction not found"}), 404

@sprint_predictions_bp.route("/<int:sprint_prediction_id>", methods=["PUT"])
def update(sprint_prediction_id):
    data = request.get_json()
    sprint_prediction = update_sprint_prediction(sprint_prediction_id, data)
    if sprint_prediction:
        return jsonify({"message": "Sprint Prediction Updated Successfully", "sprint_prediction": sprint_prediction}), 200
    return jsonify({"message": "Sprint Prediction not found"}), 404

@sprint_predictions_bp.route("/<int:sprint_prediction_id>", methods=["DELETE"])
def delete(sprint_prediction_id):
    sprint_prediction = get_sprint_prediction_by_id(sprint_prediction_id)
    if not sprint_prediction:
        return jsonify({"message": "Sprint Prediction not found"}), 404

    status = delete_sprint_prediction(sprint_prediction_id)
    if status:
        return jsonify({"message": "Sprint Prediction deleted successfully", "sprint_prediction": sprint_prediction}), 200
    return jsonify({"message": "Error deleting sprint prediction"}), 400    


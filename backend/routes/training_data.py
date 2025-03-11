from flask import Blueprint, request, jsonify
from controllers.training_data_controller import create_training_data, get_all_training_data, get_training_data_by_id, update_training_data, delete_training_data


training_data_bp = Blueprint("training_data", __name__)


@training_data_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    result = create_training_data(data)
    if "error" not in result:
        return jsonify({"message": "Training Data Created Successfully", "training_data": result}), 201
    print(result["error"])
    return jsonify({"message": f"Error Creating Training Data - Problem with field {result['error']}"}), 400

@training_data_bp.route("/", methods=["GET"])
def get_all():
    training_data = get_all_training_data()
    return jsonify({"message":"Successfully retrieved training data", "training_data": training_data}), 200

@training_data_bp.route("/<int:training_data_id>", methods=["GET"])
def get_one(training_data_id):
    training_data = get_training_data_by_id(training_data_id)
    if training_data:
        return jsonify({"message": f"Successfully retrieved training data", "training_data": training_data}), 200
    return jsonify({"message": "Training Data not found"}), 404

@training_data_bp.route("/<int:training_data_id>", methods=["PUT"])
def update(training_data_id):
    data = request.get_json()
    training_data = update_training_data(training_data_id, data)
    if training_data:
        return jsonify({"message": "Training Data Updated Successfully", "training_data": training_data}), 200
    return jsonify({"message": "Training Data not found"}), 404

@training_data_bp.route("/<int:training_data_id>", methods=["DELETE"])
def delete(training_data_id):
    training_data = get_training_data_by_id(training_data_id)
    if not training_data:
        return jsonify({"message": "Training Data not found"}), 404

    status = delete_training_data(training_data_id)
    if status:
        return jsonify({"message": "Training Data deleted successfully", "training_data": training_data}), 200
    return jsonify({"message": "Error deleting training data"}), 400

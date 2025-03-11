from flask import Blueprint, request, jsonify
from controllers.sprint_metrics_controller import create_sprint_metrics, get_all_sprint_metrics, get_sprint_metrics_by_id, update_sprint_metrics, delete_sprint_metrics
from controllers.sprints_controller import check_if_sprint_exists

sprint_metrics_bp = Blueprint("sprint_metrics", __name__)


@sprint_metrics_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    if not check_if_sprint_exists(data["sprint_id"]):
        return jsonify({"message": "Sprint not found"}), 404
    result = create_sprint_metrics(data)
    if "error" not in result:
        return jsonify({"message": "Sprint Metrics Created Successfully", "sprint_metrics": result}), 201
    print(result["error"])
    return jsonify({"message": f"Error Creating Sprint Metrics - Problem with field {result['error']}"}), 400

@sprint_metrics_bp.route("/", methods=["GET"])
def get_all():
    sprint_metrics = get_all_sprint_metrics()
    return jsonify({"message":"Successfully retrieved sprint metrics", "sprint_metrics": sprint_metrics}), 200

@sprint_metrics_bp.route("/<int:sprint_metrics_id>", methods=["GET"])
def get_one(sprint_metrics_id):
    sprint_metrics = get_sprint_metrics_by_id(sprint_metrics_id)
    if sprint_metrics:
        return jsonify({"message": f"Successfully retrieved sprint metrics", "sprint_metrics": sprint_metrics}), 200
    return jsonify({"message": "Sprint Metrics not found"}), 404

@sprint_metrics_bp.route("/<int:sprint_metrics_id>", methods=["PUT"])
def update(sprint_metrics_id):
    data = request.get_json()
    sprint_metrics = update_sprint_metrics(sprint_metrics_id, data)
    if sprint_metrics:
        return jsonify({"message": "Sprint Metrics Updated Successfully", "sprint_metrics": sprint_metrics}), 200
    return jsonify({"message": "Sprint Metrics not found"}), 404

@sprint_metrics_bp.route("/<int:sprint_metrics_id>", methods=["DELETE"])
def delete(sprint_metrics_id):
    sprint_metrics = get_sprint_metrics_by_id(sprint_metrics_id)
    if not sprint_metrics:
        return jsonify({"message": "Sprint Metrics not found"}), 404

    status = delete_sprint_metrics(sprint_metrics_id)
    if status:
        return jsonify({"message": "Sprint Metrics deleted successfully", "sprint_metrics": sprint_metrics}), 200
    return jsonify({"message": "Error deleting sprint metrics"}), 400
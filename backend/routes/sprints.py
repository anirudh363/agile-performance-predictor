from flask import Blueprint, request, jsonify
from controllers.sprints_controller import create_sprint, get_all_sprints, get_sprint_by_id, update_sprint, delete_sprint
from controllers.teams_controller import check_if_team_exists

sprints_bp = Blueprint("sprints", __name__)


@sprints_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    if not check_if_team_exists(data["team_id"]):
        return jsonify({"message": "Team not found"}), 404
    result = create_sprint(data)
    if "error" not in result:
        return jsonify({"message": "Sprint Created Successfully", "sprint": result}), 201
    print(result["error"])
    return jsonify({"message": f"Error Creating Sprint - Problem with field {result['error']}"}), 400

@sprints_bp.route("/", methods=["GET"])
def get_all():
    sprints = get_all_sprints()
    return jsonify({"message":"Successfully retrieved sprints", "sprints": sprints}), 200

@sprints_bp.route("/<int:sprint_id>", methods=["GET"])
def get_one(sprint_id):
    sprint = get_sprint_by_id(sprint_id)
    if sprint:
        return jsonify({"message": f"Successfully retrieved sprint", "sprint": sprint}), 200
    return jsonify({"message": "Sprint not found"}), 404

@sprints_bp.route("/<int:sprint_id>", methods=["PUT"])
def update(sprint_id):
    data = request.get_json()
    sprint = update_sprint(sprint_id, data)
    if sprint:
        return jsonify({"message": "Sprint Updated Successfully", "sprint": sprint}), 200
    return jsonify({"message": "Sprint not found"}), 404

@sprints_bp.route("/<int:sprint_id>", methods=["DELETE"])
def delete(sprint_id):
    sprint = get_sprint_by_id(sprint_id)
    if not sprint:
        return jsonify({"message": "Sprint not found"}), 404

    status = delete_sprint(sprint_id)
    if status:
        return jsonify({"message": "Sprint deleted successfully", "sprint": sprint}), 200
    return jsonify({"message": "Error deleting sprint"}), 400
from flask import Blueprint, request, jsonify
from controllers.teams_controller import create_team, get_all_teams, get_team_by_id, update_team, delete_team

teams_bp = Blueprint("teams", __name__)

@teams_bp.route("/", methods=["POST"])
def create():
    data = request.get_json()
    result = create_team(data)
    if "error" not in result:
        return jsonify({"message": "Team Created Successfully", "team": result}), 201
    print(result["error"])
    return jsonify({"message": f"Error Creating Team - Problem with field {result['error']}"}), 400

@teams_bp.route("/", methods=["GET"])
def get_all():
    teams = get_all_teams()
    return jsonify({"message":"Successfully retrieved teams", "teams": teams}), 200

@teams_bp.route("/<int:team_id>", methods=["GET"])
def get_one(team_id):
    team = get_team_by_id(team_id)
    if team:
        return jsonify({"message": f"Successfully retrieved team", "team": team}), 200
    return jsonify({"message": "Team not found"}), 404

@teams_bp.route("/<int:team_id>", methods=["PUT"])
def update(team_id):
    data = request.get_json()
    team = update_team(team_id, data)
    if team:
        return jsonify({"message": "Team Updated Successfully", "team": team}), 200
    return jsonify({"message": "Team not found"}), 404

@teams_bp.route("/<int:team_id>", methods=["DELETE"])
def delete(team_id):
    team = get_team_by_id(team_id)
    if not team:
        return jsonify({"message": "Team not found"}), 404

    status = delete_team(team_id)
    if status:
        return jsonify({"message": "Team deleted successfully", "team": team}), 200
    return jsonify({"message": "Error deleting team"}), 400


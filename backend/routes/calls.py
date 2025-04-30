from flask import Blueprint, jsonify
from services.supabase_service import SupabaseService

calls_bp = Blueprint("calls", __name__)

@calls_bp.route("/calls", methods=["GET"])
def get_calls():
    try:
        data = SupabaseService.get_table_data("calls")
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
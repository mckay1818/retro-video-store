from app import db
from app.models.customer import Customer
from app.models.video import Video
from flask import Blueprint, jsonify, abort, make_response, request

videos_bp = Blueprint("videos", __name__, url_prefix="/videos")
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customers_bp.route("",methods = ["GET"])
def read_all_customers():
    customers = Customer.query.all()
    customers_response = []
    for customer in customers:
        customers_response.append({
            "id": customer.id,
            "name": customer.id,
            "postal_code": customer.id,
            "phone": customer.phone
        })
    return jsonify(customers_response)
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
            "name": customer.name,
            "postal_code": customer.postal_code,
            "phone": customer.phone
        })
    return jsonify(customers_response)

@customers_bp.route("", methods = ["POST"])
def create_one_customer():
    request_body = request.get_json()
    new_customer = Customer(
        name = request_body["name"],
        registered_at = request_body["registered_at"],
        postal_code = request_body["postal_code"],
        phone = request_body["phone"]
    )

    db.session.add(new_customer)
    db.session.commit()

    return make_response({"id": f"{new_customer.id}"},201)
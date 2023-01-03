from app import db
from app.models.customer import Customer
from app.models.video import Video
from flask import Blueprint, jsonify, abort, make_response, request

videos_bp = Blueprint("videos", __name__, url_prefix="/videos")
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")
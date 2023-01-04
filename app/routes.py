from app import db
from app.models.customer import Customer
from app.models.video import Video
from flask import Blueprint, jsonify, abort, make_response, request

videos_bp = Blueprint("videos", __name__, url_prefix="/videos")
customers_bp = Blueprint("customers", __name__, url_prefix="/customers")

def validate_video_id(video_id):
    try:
        video_id = int(video_id)
    except:
        abort(make_response(jsonify({"message": f"Video {video_id} is invalid"}), 400))

    video = Video.query.get(video_id)

    if not video:
        abort(make_response(jsonify({"message": f"Video {video_id} was not found"}), 404))

@videos_bp.route("", methods=["POST"])
def create_video():
    request_body = request.get_json()
    new_video = Video.from_dict(request_body)

    db.session.add(new_video)
    db.session.commit()

    return make_response(jsonify(f"Video {new_video.title} successfully created."), 201)

@videos_bp.route("", methods=["GET"])
def get_all_videos():
    #add logic for filtering by query params
    videos = Video.query.all()
    videos_response = []
    for video in videos:
        videos_response.append(video.to_dict())
    return jsonify(videos_response)

@videos_bp.route("/<video_id>", methods=["GET"])
def get_one_video(video_id):
    video = validate_video_id(video_id)
    return video.to_dict()

@videos_bp.route("/<video_id>", methods=["PUT"]) 
def update_one_video(video_id):
    video = validate_video_id(video_id)
    request_body = request.get_json()

    try:
        video.title = request_body["title"]
        video.release_date = request_body["release_date"]
        video.total_inventory = request_body["total_inventory"]
    ###########
    ###########
    ##########
    #TODO: refactor this out of Video model, into sep fn in routes
    except KeyError as e:
        key = str(e).strip("\'")
        abort(make_response(jsonify({"details": f"Request body must include {key}."}), 400))

    db.session.commit()
    return make_response(jsonify({"message": "Video ID #{video_id} successfully updated"}), 200)
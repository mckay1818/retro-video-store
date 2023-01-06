from app import db
from sqlalchemy.orm import relationship
from datetime import timedelta

class Rental(db.Model):
    __tablename__ = "customer_video"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    customer = relationship("Customer", back_populates="rentals")
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"), nullable=False)
    video = relationship("Video", back_populates="rentals")
    due_date = db.Column(db.DateTime(timezone=True), default=db.func.now() + timedelta(days=7), nullable=False)


    # @classmethod
    # def from_dict(cls, rental_data):
    #     new_rental = Rental(name=customer_data["name"],
    #     postal_code = customer_data["postal_code"],
    #     phone = customer_data["phone"])
    #     return new_rental
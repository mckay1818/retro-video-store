from app import db
from sqlalchemy.orm import relationship

class Rental(db.Model):
    __tablename__ = "customer_video"
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    customer = relationship("Customer", back_populates="rentals")
    video_id = db.Column(db.Integer, db.ForeignKey("video.id"), nullable=False)
    video = relationship("Video", back_populates="rentals")
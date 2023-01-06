from app import db
from sqlalchemy.orm import relationship

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    registered_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), nullable=False)
    postal_code = db.Column(db.String)
    phone = db.Column(db.String)
    rentals = db.relationship("Rental", back_populates="customer")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "postal_code": self.postal_code,
            "phone": self.phone
        }

    def rental_count(self):
        count = 0
        for rental in self.rentals:
            count += 1
        return count

    @classmethod
    def from_dict(cls, customer_data):
        new_customer = Customer(name=customer_data["name"],
        postal_code = customer_data["postal_code"],
        phone = customer_data["phone"])
        return new_customer



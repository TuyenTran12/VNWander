from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey, Text, JSON, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255))
    phone = Column(String(20))
    role = Column(String(20), default='customer')
    is_active = Column(Boolean, default=True)
    created_at = Column(Date, server_default='CURRENT_DATE')

    vendor = relationship("Vendor", back_populates="user", uselist=False)
    bookings = relationship("Booking", back_populates="user")
    reviews = relationship("Review", back_populates="user")

class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    business_name = Column(String(255))
    tax_id = Column(String(50))
    address = Column(Text)
    verified = Column(Boolean, default=False)

    user = relationship("User", back_populates="vendor")
    properties = relationship("Property", back_populates="vendor")

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    address = Column(Text)
    city = Column(String(100))
    country = Column(String(100), default='Vietnam')
    latitude = Column(DECIMAL(10,8))
    longitude = Column(DECIMAL(11,8))
    star_rating = Column(Integer)
    amenities = Column(JSON)
    policies = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(Date, server_default='CURRENT_DATE')

    vendor = relationship("Vendor", back_populates="properties")
    rooms = relationship("Room", back_populates="property")
    bookings = relationship("Booking", back_populates="property")
    reviews = relationship("Review", back_populates="property")

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    property_id = Column(Integer, ForeignKey('properties.id'))
    name = Column(String(255), nullable=False)
    description = Column(Text)
    max_occupancy = Column(Integer, nullable=False)
    bed_configuration = Column(String(100))
    price_per_night = Column(DECIMAL(10,2), nullable=False)
    amenities = Column(JSON)
    is_active = Column(Boolean, default=True)

    property = relationship("Property", back_populates="rooms")
    inventory = relationship("Inventory", back_populates="room")
    bookings = relationship("Booking", back_populates="room")

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    date = Column(Date, nullable=False)
    available_rooms = Column(Integer, default=0)
    price_override = Column(DECIMAL(10,2))
    is_blocked = Column(Boolean, default=False)

    room = relationship("Room", back_populates="inventory")

class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_reference = Column(String(20), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    guest_count = Column(Integer, nullable=False)
    total_price = Column(DECIMAL(10,2), nullable=False)
    status = Column(String(20), default='pending')
    payment_status = Column(String(20), default='unpaid')
    special_requests = Column(Text)
    created_at = Column(Date, server_default='CURRENT_DATE')

    user = relationship("User", back_populates="bookings")
    property = relationship("Property", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")
    payments = relationship("Payment", back_populates="booking")
    review = relationship("Review", back_populates="booking", uselist=False)

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    amount = Column(DECIMAL(10,2), nullable=False)
    payment_method = Column(String(50))
    transaction_id = Column(String(100))
    status = Column(String(20), default='pending')
    created_at = Column(Date, server_default='CURRENT_DATE')

    booking = relationship("Booking", back_populates="payments")

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('bookings.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))
    rating = Column(Integer)
    comment = Column(Text)
    created_at = Column(Date, server_default='CURRENT_DATE')

    booking = relationship("Booking", back_populates="review")
    user = relationship("User", back_populates="reviews")
    property = relationship("Property", back_populates="reviews")
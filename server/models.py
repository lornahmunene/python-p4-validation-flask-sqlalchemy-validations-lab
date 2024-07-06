from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('phone_number')
    def validates_phone_number(self,key,digits):
        if len(digits) !=10 or not digits.isdigit() :
         raise ValueError('Phone_number should be less than 10 digits and numeric')
        return digits
    @validates ('name')
    def validates_name(self,key,name):
        if not name :
            raise ValueError("Author name is required")
        if Author.query.filter_by(name=name).first():
            raise ValueError(f"Author with name '{name}' already exists.")
        return name
    


    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators
    @validates('content')
    def validate_content(self,key,content):
        if len(content)!=250:
            raise ValueError("Content is too short")
        return content
    @validates('summary')
    def validate_summary(self,key,summary):
        if len(summary)>250:
            raise ValueError("Summary is too long")
        return summary



    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'

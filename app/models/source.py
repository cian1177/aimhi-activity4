from app import db

class source(db.Model):
    __tablename__ = 'Source'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ref = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String, nullable=False)
    type = db.Column(db.String(250), nullable=False)
    status_change = db.Column(db.String, nullable=False)
    open_actions = db.Column(db.String(250), nullable=False)
    total_actions = db.Column(db.String(250), nullable=False)
    association = db.Column(db.String(250), nullable=False)
    overdue = db.Column(db.String(250), nullable=False)
    images = db.Column(db.String(250), nullable=False)
    comments = db.Column(db.String(250), nullable=False)
    documents = db.Column(db.String(250), nullable=False)
    project = db.Column(db.String(250), nullable=False)
    report_forms_status = db.Column(db.String(250), nullable=False)
    report_forms_group = db.Column(db.String(250), nullable=False)

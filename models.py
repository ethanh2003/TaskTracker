from database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(4150))
    email = db.Column(db.String(4150), unique=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    access = db.Column(db.Boolean)  # True if admin, False otherwise
    pinnedTask = db.Column(db.String(4150))

    def __init__(self, name, email, username, password, access):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.access = access
        self.pinnedTask = ""


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(4150))
    assigned = db.Column(db.String(100))
    due = db.Column(db.Date)
    complete = db.Column(db.Integer)
    createdBy = db.Column(db.Integer)
    comments = db.relationship("Comment", backref="comment", cascade="all, delete-orphan", lazy=True)

    def __init__(self, title, description, assigned, due, complete, createdBy):
        self.title = title
        self.description = description
        self.assigned = assigned
        self.due = due
        self.complete = complete
        self.createdBy = createdBy


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.VARCHAR, nullable=False)
    todo_id = db.Column(db.Integer, db.ForeignKey("todo.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, content, todo_id, user_id):
        self.content = content
        self.todo_id = todo_id
        self.user_id = user_id

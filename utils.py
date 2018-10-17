from flaskApp.models import studentDemographics, db

def initdb():
	stud = studentDemographics('A9700074', 161, 'channa', 0)
	db.session.add(stud)
	db.session.commit()
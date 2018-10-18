from flaskApp import db
from datetime import datetime

class studentDemographics(db.Model):
    __tablename__ = 'student_demographics'
    id = db.Column(db.Integer, primary_key=True)
    ncesid = db.Column(db.String(10))
    totalstudent = db.Column(db.Integer)
    stype = db.Column(db.String(20))
    value = db.Column(db.Integer)

    def __init__(self, ncesid, totalstudent, stype, value):
        self.ncesid = ncesid
        self.totalstudent = totalstudent
        self.stype = stype
        self.value = value

    def __repr__(self):
        return '<studentDemographics {}>'.format(self.ncesid)

class freeReducedLunch(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    ncesid = db.Column(db.String(10))
    numReducedLunch = db.Column(db.Integer)
    numFreeLunch = db.Column(db.Integer)

    def __init__(self, ncesid, numReducedLunch, numFreeLunch):
        self.ncesid = ncesid
        self.numReducedLunch = numReducedLunch
        self.numFreeLunch = numFreeLunch


    def __repr__(self):
        return '<freeReducedLunch {}>'.format(self.ncesid)

# schooltype table

class acs5PopulationAgeByRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    agegroup = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, agegroup, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.agegroup = agegroup
        self.count = count


    def __repr__(self):
        return '<acs5PopulationAgeByRace {}>'.format(self.censustractid)

class acs5SchoolEnrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    schoolenrollment = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, schoolenrollment, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.schoolenrollment = schoolenrollment
        self.count = count


    def __repr__(self):
        return '<acs5SchoolEnrollment {}>'.format(self.censustractid)

class acs5HouseholdIncomeByRace(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    householdincome = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, householdincome, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.householdincome = householdincome
        self.count = count


    def __repr__(self):
        return '<acs5HouseholdIncomeByRace {}>'.format(self.censustractid)

class acs5PlaceOfBirthByCitizenship(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    placeofbirth = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, placeofbirth, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.placeofbirth = placeofbirth
        self.count = count


    def __repr__(self):
        return '<acs5PlaceOfBirthByCitizenship {}>'.format(self.censustractid)

class acs5DetailedFieldOfBachelorDegree(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    field_of_bachelor_degree = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, field_of_bachelor_degree, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.field_of_bachelor_degree = field_of_bachelor_degree
        self.count = count


    def __repr__(self):
        return '<acs5DetailedFieldOfBachelorDegree {}>'.format(self.censustractid)

class acs5EdAttainByEmployment25yrs(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    employment_status_25_64_years = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, employment_status_25_64_years, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.employment_status_25_64_years = employment_status_25_64_years
        self.count = count


    def __repr__(self):
        return '<acs5EdAttainByEmployment25yrs {}>'.format(self.censustractid)

class acs5DetailedEdAttain25yrs(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    educational_attainment = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, educational_attainment, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.educational_attainment = educational_attainment
        self.count = count


    def __repr__(self):
        return '<acs5DetailedEdAttain25yrs {}>'.format(self.censustractid)

class MedianHouseholdIncome(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    censustractid = db.Column(db.String(10))
    censustract = db.Column(db.String(10))
    household_income = db.Column(db.String(10))
    count = db.Column(db.Integer)

    def __init__(self, censustractid, censustract, household_income, count):
        self.censustractid = censustractid
        self.censustract = censustract
        self.household_income = household_income
        self.count = count


    def __repr__(self):
        return '<MedianHouseholdIncome {}>'.format(self.censustractid)
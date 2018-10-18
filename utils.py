from flaskApp.models import studentDemographics, \
							freeReducedLunch, \
							acs5PopulationAgeByRace, \
							acs5SchoolEnrollment, \
							acs5HouseholdIncomeByRace, \
							acs5PlaceOfBirthByCitizenship, \
							acs5DetailedFieldOfBachelorDegree, \
							acs5EdAttainByEmployment25yrs, \
							acs5DetailedEdAttain25yrs, \
							MedianHouseholdIncome, \
							db
import pandas as pd
import math 

# workspace = 

def initdb():
	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/studentDemographics2015.csv", converters={'ncesid': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			ncesid = row['ncesid']
			totalstudents = int(row['totalstudents']) if row['totalstudents'] != 'M' and not math.isnan(float(row['totalstudents'])) else 0
			stype = row['stype']
			value = int(row['value']) if row['value'] != 'M' and not math.isnan(float(row['value'])) else 0

			# make a ORM object
			ormObj = studentDemographics(ncesid, 
										totalstudents, 
										stype, 
										value)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except:
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/free_reduced_lunch.csv", converters={'ncesID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			ncesid = row['ncesID']
			numReducedLunch = int(row['numReducedLunch']) if row['numReducedLunch'] != 'M' and not math.isnan(float(row['numReducedLunch'])) else 0
			numFreeLunch = int(row['numFreeLunch']) if row['numFreeLunch'] != 'M' and not math.isnan(float(row['numFreeLunch'])) else 0

			# make a ORM object
			ormObj = freeReducedLunch(ncesid, 
										numReducedLunch, 
										numFreeLunch)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()


	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5PopulationAgeByRace.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			agegroup = row[r'Age Group']
			count = int(row[r'#ofPeople'])

			# make a ORM object
			ormObj = acs5PopulationAgeByRace(censustractid, 
										censustract, 
										agegroup, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()
	
	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5SchoolEnrollment.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			schoolenrollment = row[r'School Enrollment']
			count = int(row[r'#ofStudents'])

			# make a ORM object
			ormObj = acs5SchoolEnrollment(censustractid, 
										censustract, 
										schoolenrollment, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5HouseholdIncomeByRace.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			householdincome = row[r'Household Income (in Dollars)']
			count = int(row[r'#ofPeople'])

			# make a ORM object
			ormObj = acs5HouseholdIncomeByRace(censustractid, 
										censustract, 
										householdincome, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5PlaceOfBirthByCitizenship.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			placeofbirth = row[r'Place Of Birth']
			count = int(row[r'#ofPeople'])

			# make a ORM object
			ormObj = acs5PlaceOfBirthByCitizenship(censustractid, 
										censustract, 
										placeofbirth, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5DetailedFieldOfBachelorDegree.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			field_of_bachelor_degree = row[r'Field of Bachelor Degree']
			count = int(row[r'#'])

			# make a ORM object
			ormObj = acs5DetailedFieldOfBachelorDegree(censustractid, 
										censustract, 
										field_of_bachelor_degree, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5EdAttainByEmployment25yrs.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			employment_status_25_64_years = row[r'Employment Status for people 25-64 years']
			count = int(row[r'#ofPeople'])

			# make a ORM object
			ormObj = acs5EdAttainByEmployment25yrs(censustractid, 
										censustract, 
										employment_status_25_64_years, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/acs5DetailedEdAttain25yrs.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			educational_attainment = row[r'Educational Attainment']
			count = int(row[r'#ofPeople'])

			# make a ORM object
			ormObj = acs5DetailedEdAttain25yrs(censustractid, 
										censustract, 
										educational_attainment, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	df = pd.read_csv(r"/Users/channa/Projects/DecisionTheater/HELIOS/csvfiles2/MedianHouseholdIncome.csv", converters={'ID': lambda x: str(x)})
	try:
		# iterate through each row in csv
		for index, row in df.iterrows():

			# collect variables from csv
			censustractid = str(row[r'ID'])
			censustract = row[r'CensusTract,County,State']
			household_income = row[r'Household Income (in Dollars)']
			count = int(row[r'#ofPeople'])

			# make a ORM object
			ormObj = MedianHouseholdIncome(censustractid, 
										censustract, 
										household_income, 
										count)

			# add it to database (commit it later - last line)
			db.session.add(ormObj)
	except Exception, e:
		print ("Error message: ", e)
		import pdb; pdb.set_trace()

	db.session.commit()
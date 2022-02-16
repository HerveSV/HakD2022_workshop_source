from airtable import Airtable



baseKey = "appDhfVy7MEF7Sudv"
apiKey = "keycI94kSI29b60Ix"


studentsTable = Airtable(f"airtable://{baseKey}/Students", api_key=apiKey)

# this way you can display the data directly on this computer, though it won't necessarily be updated.
studentsDict = studentsTable.get_all_as_dict()

# Add money to a student's card
#   sid <integer>: student id
#   value <float>: the positive amount of money you want to add
def top_up_card(sid, value):
    if value <= 0:
        return
    # find the student record with corresponding student id
    rec = studentsTable.search("SID", sid)[0]
    # then retrieve their current balance value
    currBal = rec.get("fields").get("Balance")

    newBal = currBal + value
    studentsTable.update_by_field("SID", sid, {"Balance": newBal})
    
# Create a new student record
#   name <string>: name of the new student
def add_student(name):
    studentsTable.insert({"Name": name})

# delete a new student record
#   name <string>: name of the new student
def delete_student(sid):
    studentsTable.delete_by_field("SID", sid)




#top_up_card(1, 69)
#add_student("Joe")
delete_student(3)







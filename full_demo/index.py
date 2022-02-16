from airtable import Airtable
import datetime



baseKey = "appDhfVy7MEF7Sudv"
apiKey = "keycI94kSI29b60Ix"


studentsTable = Airtable(f"airtable://{baseKey}/Students", api_key=apiKey)
transacsTable = Airtable(f"airtable://{baseKey}/Transactions", api_key=apiKey)

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
    studentsTable.update_by_field("ID", sid, {"Balance": newBal})
    
# Create a new student record
#   name <string>: name of the new student
def add_student(name):
    studentsTable.insert({"Name": name, "Balance": 0})

# Creates a transaction and puts it under a students name
#   sid <integer>: student id
#   cost <float>: cost of the transaction, will be deducted from the student's balance
#   name <string>: name of the transaction
def make_transaction(sid, cost, name="unnamed"):
    # get the student's record
    rec = studentsTable.search("SID", sid)[0]
    # extract the internal id, this is the only way to reference Foreign Keys
    intern_id = rec.get('id')
    # get current balance
    currBal = rec.get("fields").get("Balance")
    # always remember that foreign keys, even if meant to be single record, need to be sent in a list structure
    transacsTable.insert({"Name": name, "Cost": cost, "Student": [intern_id], "Date": f"{datetime.datetime.today().year}-{datetime.datetime.today().month}-{datetime.datetime.today().day}"})

    # calculated deducted balance, and update the student's balance
    newBal = currBal - cost
    studentsTable.update_by_field("SID", sid, {"Balance": newBal})




make_transaction(3, 15, "Bits and things")







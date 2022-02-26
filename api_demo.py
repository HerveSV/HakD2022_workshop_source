from airtable import Airtable

baseKey = "appDhfVy7MEF7Sudv"
apiKey = "keycI94kSI29b60Ix"

table = Airtable(airtable_url_or_base_key=baseKey, api_key=apiKey, table_name="test")
# otherwise, table can also be initialised this way:
# table = Airtable(f"airtable://{baseKey}/Students", api_key=apiKey)

# super handy method, allows you to get the entire table in convenient dictionary format
stuff = table.get_all_as_dict()
print(stuff)


def create_record(data):
    # create a new record, set default values to those in the dictionary
    # if you are re-using these functions, make sure to adapt to the fields you are having
    table.insert({"Notes": data})

def update_record(id, newData):
    # first argument, the field you are searching by
    # second argument, the specific value you are looking for
    # third argument, dictionary containing field-value pairs to be updated.
    #   Any fields that are not included will not be changed
    table.update_by_field("ID", id, {"Notes": newData})

def read_notes_field(id):
    # returns an array
    # we know "ID" to be unique, so only need 1st element
    record = table.search("ID", id)[0]

    return record.get('fields').get('Notes')

def delete_record(id):
    table.delete_by_field("ID", id)

# this is to get autogenerated alphanumerical id
# when you set the value of a foreign key, it always needs to be an array of internal ids
def get_record_internal_id(id):
    record = table.search("ID", id)[0]
    return record.get('id')

import csv
import random

def generate_dummy_csv(filename, numEntityIds, numInvites):
    # Define column headers
    fields = ['entityId', 'firstName', 'lastName', 'contact']
    
    # Dummy data
    contact = 'bmarterella'
    entityIds = select_random_entity_ids(filename, numEntityIds)
    
    # Generate data for 1000 rows
    rows = []
    for i in range(numInvites):
        row = [random.choice(entityIds), 'DummyFirstName', 'DummyLastName', "NEWmseverance+%s" %i +"devblah@yext.com"]
        rows.append(row)
    
    # Write to CSV file
    with open('invites.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

def select_random_entity_ids(filename, numEntityIds):
    with open(filename) as csvfile:
        entityIdRows = csv.reader(csvfile)
        entityIds = [entityIdRow[0] for entityIdRow in entityIdRows]
        return random.sample(entityIds, numEntityIds)
        
if __name__ == "__main__":
    filename = 'qa_entity_ids.csv'
    generate_dummy_csv(filename, 1000, 1000)
    print("DONE!")

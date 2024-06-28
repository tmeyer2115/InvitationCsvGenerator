import csv

def generate_dummy_csv(filename):
    # Define column headers
    fields = ['entityId', 'firstName', 'lastName', 'contact']
    
    # Dummy data
    entityId = '4'
    contact = 'bmarterella'
    
    # Generate data for 1000 rows
    rows = []
    for i in range(6000):
        row = [entityId, 'DummyFirstName', 'DummyLastName', "NEWmseverance+%s" %i +"devblah@yext.com"]
        rows.append(row)
    
    # Write to CSV file
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

if __name__ == "__main__":
    filename = 'dummy_data.csv'
    generate_dummy_csv(filename)
    print("DONE!")

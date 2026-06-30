class Requisition:

    requisition_counter = 10000

    def __init__(self, date, staff_id, staff_name):

        Requisition.requisition_counter += 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.requisition_counter

        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"


    # This method adds items and calculates total cost
    def add_requisition(self, items):

        self.items = items
        self.total = 0

        for item in items:
            self.total += item["cost"]

        self.approve_requisition()


    # This method automatically approves requisition below $500
    def approve_requisition(self):

        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

        else:
            self.status = "Pending"
            self.approval_reference = "Not available"


    # This method is used for manager response
    def respond_requisition(self, response):

        if self.status == "Pending":

            if response.lower() == "approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

            elif response.lower() == "not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"


# Main program starts here

requisitions = []

number = int(input("How many requisitions do you want to enter? "))

for i in range(number):

    print()
    print("Enter details for Requisition", i + 1)

    date = input("Enter Date (DD/MM/YYYY): ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")

    req = Requisition(date, staff_id, staff_name)

    items = []

    item_number = int(input("How many items do you want to enter? "))

    for j in range(item_number):

        item_name = input("Enter Item Name: ")
        item_cost = float(input("Enter Item Cost: "))

        item = {
            "item": item_name,
            "cost": item_cost
        }

        items.append(item)

    req.add_requisition(items)
    requisitions.append(req)


print()
print("Manager Response")
print()

for req in requisitions:

    if req.status == "Pending":

        print()
        print("Requisition ID:", req.requisition_id)
        print("Staff Name:", req.staff_name)
        print("Total: $" + str(req.total))
        print("Status:", req.status)

        response = input("Enter manager response (approved/not approved): ")
        req.respond_requisition(response)


print()
print("Manager responses have been completed.")
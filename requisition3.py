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


    # This method displays one requisition
    def display_requisition(self):

        print("Date:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + str(self.total))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()


# This function displays all requisitions
def display_all_requisitions(requisitions):

    for req in requisitions:
        req.display_requisition()


# This function displays statistics
def requisition_statistics(requisitions):

    total_submitted = len(requisitions)
    approved = 0
    pending = 0
    not_approved = 0

    for req in requisitions:

        if req.status == "Approved":
            approved += 1

        elif req.status == "Pending":
            pending += 1

        elif req.status == "Not approved":
            not_approved += 1

    print("Statistics:")
    print("Displaying the Requisition statistics")
    print("The total number of requisitions submitted:", total_submitted)
    print("Total approved requisition:", approved)
    print("Total pending requisitions:", pending)
    print("Total not approved requisitions:", not_approved)
    print()


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
print("Before Manager Response")
print()
display_all_requisitions(requisitions)
requisition_statistics(requisitions)


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
print("After Manager Response")
print()
display_all_requisitions(requisitions)
requisition_statistics(requisitions)
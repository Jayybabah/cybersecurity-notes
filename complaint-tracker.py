# Customer Complaint Tracker - by Aliyu Abdulkadir Baba
# Based on my PGD research: Social Media Complaints & Brand Reputation

complaints = []

print("=== Customer Complaint Tracker ===")
for i in range(2):
    name = input(f"\nCustomer {i+1} name: ")
    platform = input("Platform (WhatsApp/Facebook/Instagram/X): ")
    issue = input("Complaint: ")
    severity = input("Severity (Low / High / Serious): ")

    complaints.append({"name": name, "platform": platform, "issue": issue, "severity": severity})
    print("Complaint saved!")

print("\n=== All Complaints ===")
for c in complaints:
    print(f"{c['name']} on {c['platform']} - {c['issue']} [{c['severity']}]")

print(f"\nTotal complaints: {len(complaints)}")
print("Tip: Respond quickly + politely to protect brand reputation!")

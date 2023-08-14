# A Program to Assist St. John's Marina & Yacht Club to calculate member fees
#  Written By: Tanner Jones
# Date Written: January 27th 2023

# Constants

COST_EVEN = 80.00
COST_ODD = 120.00
COST_EXTRA = 5.00
WEEK_CLEAN = 50.00
VIDEO_SURVEY = 35.00
STANDARD_MEMBER = 75.00
EXECUTIVE_MEMBER = 150.00
PRO_FEE = 59.99
HST_RATE = 0.15
CANCEL_RATE = 0.60

# Inputs

MemberName = input("What is members name: ")
StreetAdd = input("What is the Street Address: ")
City = input("What Is the city: ")
Province = input("What is the Province: ")
Postcode = input("What is the Postal Code: ")
PhoneNum = input("What is the phone number: ")
CellNum = input("What is the Cell number: ")
SiteNumber = int(input("What is the site number: "))
MembershipType = input("What type is the membership(S or E): ").upper()
NumAlternative = int(input("What is the number of Alternate Members: "))
WeeklyClean = input("Does Member want weekly cleaning(Y or N): ").upper()
VideoSurvey = input("Does Member want Video Surveillance(Y or N): ").upper()

# Calculations
if SiteNumber % 2 == 0:
    siteCost = COST_EVEN
else:
    siteCost = COST_ODD

altMemCharge = NumAlternative * COST_EXTRA
siteCharge = siteCost + altMemCharge

if WeeklyClean == "Y":
    cleanCharge = WEEK_CLEAN
else:
    cleanCharge = 0

if VideoSurvey == "Y":
    VideoCharge = VIDEO_SURVEY
else:
    VideoCharge = 0

#Extra calculations from if statements

ExtraCharge = cleanCharge + VideoCharge
subtotal = siteCharge + ExtraCharge
salesTax = subtotal * HST_RATE
totalmonthlycharge = subtotal + salesTax

if MembershipType == "S":
    MonthDue = STANDARD_MEMBER
elif MembershipType == "E":
    MonthDue = EXECUTIVE_MEMBER

TotalMonthlyFees = totalmonthlycharge + MonthDue
totalyearlyfee = TotalMonthlyFees * 12
monthlypay = (totalmonthlycharge + PRO_FEE)/12

yearlysitecharge = 12 * siteCharge

cancelfee = yearlysitecharge * CANCEL_RATE

# Determining What statements to print in output

if MembershipType == "S":
    MembershipPrint = "Standard"
elif MembershipType == "E":
    MembershipPrint = "Executive"

if WeeklyClean == "Y":
    CleanPrint = "Yes"
elif WeeklyClean == "N":
    CleanPrint = "No"

if VideoSurvey == "Y":
    VideoPrint = "Yes"
elif WeeklyClean == "N":
    VideoPrint = "No"

# Printing Required outputs in format


print(" "*6, "St. John’s Marina & Yacht Club")
print(" "*11, "Yearly Member Receipt")
print("-"*44)
print("Client Name and Address:")
print()
print(f"{MemberName:<24s}")
print(f"{StreetAdd:<24s}")
print(f"{City}, {Province}, {Postcode}")
print()
print("Phone:", f"{PhoneNum:<10s}", "(H)")
print(" "*6, f"{CellNum:<10s}", "(C)")
print()
print("Site #:", f"{SiteNumber:<3d}", "Member Type:", f"{MembershipPrint:<9s}")
print()
print("Alternate members:", " "*22, f"{NumAlternative:>2d}")
print("Weekly site cleaning:", " "*18, f"{CleanPrint:<3s}")
print(f"Video Surveillance:", " "*20, f"{VideoPrint:<3s}")
print()

#  Printing and formatting Calculated outputs

siteChargeDSP = "${:.2f}".format(siteCharge)
print("Site Charges:                     ", f"{siteChargeDSP:>9s}")
ExtraChargeDSP = "${:.2f}".format(ExtraCharge)
print(f"Extra Charges:                       {ExtraChargeDSP:>7s}")
print(" "*20, "_"*13)
subtotalDSP = "${:.2f}".format(subtotal)
print(f"Subtotal:                          {subtotalDSP:>9s}")
salesTaxDSP = "${:.2f}".format(salesTax)
print(f"Sales tax (HST):                     {salesTaxDSP:>7s}")
print(" "*20, "_"*13)
totalmonthlychargeDSP = "${:.2f}".format(totalmonthlycharge)
print(f"Total monthly charges:             {totalmonthlychargeDSP:>9s}")
MonthDueDSP = "${:.2f}".format(MonthDue)
print(f"Monthly dues:                        {MonthDueDSP:>7s}")
print(" "*20, "_"*13)
TotalMonthlyFeesDSP = "${:.2f}".format(TotalMonthlyFees)
print(f"Total Monthly fees:                {TotalMonthlyFeesDSP:>9s}")
totalyearlyfeeDSP = "${:.2f}".format(totalyearlyfee)
print(f"Total Yearly Fees:                {totalyearlyfeeDSP:>10s}")
print()
monthlypayDSP = "${:.2f}".format(monthlypay)
print(f"Monthly Payment:                   {monthlypayDSP:>9s}")
print()
print("-"*44)
print()
print("Issued: 2023-02-04")
print("HST Reg No: 549-33-5849-4720-9885")
print()
cancelfeeDSP = "${:.2f}".format(cancelfee)
print(f"Cancellation fee:                  {cancelfeeDSP:>9s}")

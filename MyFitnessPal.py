import datetime
import myfitnesspal
import gspread
import os
import sys

mfp = myfitnesspal.Client()

# Get the path to the temporary folder containing the bundled files
bundle_dir = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

# Construct the path to the service account file
service_account_file = os.path.join(bundle_dir, "service_account.json")

# Load the service account credentials
sheets = gspread.service_account(service_account_file)

# Replace "HealthTracking" with the name of your spreadsheet
sh = sheets.open("HealthTracking")

# Replace "Sheet1" with the name of your worksheet
worksheet = sh.worksheet("Sheet1")

# Get the last date in the first column
if len(worksheet.col_values(1)) < 1:  # Check if the first cell is empty
    print("First cell is empty")
    worksheet.update(
        f"A1", [["Date", "Total calories", "Carbohydrates", "Fat", "Protein"]]
    )  # Update the first row with the column names
    worksheet.update(f"A2", "2023-01-01")  # Update the first data cell with the date
    last_date_str = worksheet.col_values(1)[-1]
else:
    last_date_str = worksheet.col_values(1)[-1]
print(f"Last date as string in the worksheet is {last_date_str}")

# Convert the last date from string to datetime format
last_date = datetime.datetime.strptime(last_date_str, "%Y-%m-%d").date()
print(f"Last date in the worksheet is {last_date}")

# Get the index of the last date in the col_values list
start_index = worksheet.col_values(1).index(last_date_str) + 1
print(f"Index of the last date in the worksheet is {start_index}")

# Start from the row after the last date
start_date = last_date + datetime.timedelta(days=0)
print(f"Starting from {start_date.strftime('%Y-%m-%d')}")

# End at today's date
end_date = datetime.date.today()
print(f"Ending at {end_date.strftime('%Y-%m-%d')}")

# Change this number to the maximum number of rows you want to update
max_num_updated = 9999

i = 1  # counter variable

print("Starting loop")

for date in (
    start_date + datetime.timedelta(n)
    for n in range(0, (end_date - start_date).days + 1)
):
    # Check if the number of updated rows is greater than max_num_updated
    if max_num_updated < 1:
        print("Stopping because maximum number to update is reached")
        break  # Exit the loop if the condition is true
    print(f"Update operation number {i}")

    i += 1

    try:
        # Get the MyFitnessPal data for the specified date
        day = mfp.get_date(date.year, date.month, date.day)
        print(f"Data from MyFitnessPal is {day}")
        print(
            f"Updating worksheet for {(date - start_date).days + start_index , 1, date.strftime('%Y-%m-%d')} <-- (row, col, date))"
        )
        # Update the worksheet with the MyFitnessPal data for the current date
        worksheet.update(
            f"A{(date - start_date).days + start_index}",
            [
                [
                    date.strftime("%Y-%m-%d"),
                    day.totals["calories"],
                    day.totals["carbohydrates"],
                    day.totals["fat"],
                    day.totals["protein"],
                ]
            ],
        )
        # worksheet.update_cell((date - start_date).days + start_index , 1, date.strftime('%Y-%m-%d'))  # Update the first cell with the date
        # worksheet.update_cell((date - start_date).days + start_index, 2, day.totals['calories'])  # Update the second cell with the total calories
        # worksheet.update_cell((date - start_date).days + start_index, 3, day.totals['carbohydrates'])  # Update the third cell with the total carbohydrates
        # worksheet.update_cell((date - start_date).days + start_index, 4, day.totals['fat'])  # Update the fourth cell with the total fat
        # worksheet.update_cell((date - start_date).days + start_index, 5, day.totals['protein'])  # Update the fifth cell with the total protein
        print(f"Successfully updated worksheet for {date.strftime('%Y-%m-%d')}")
        max_num_updated -= 1  # Decrement the counter variable

    except:
        print(f"Something went wrong or no data for {date.strftime('%Y-%m-%d')}")
        print(f"Data from MyFitnessPal was {day}")
        # Update the first cell with the date
        worksheet.update(
            f"A{(date - start_date).days + start_index}", [[date.strftime("%Y-%m-%d")]]
        )


print(f"updated {i} rows, happy tracking!")


# os.system("pause")

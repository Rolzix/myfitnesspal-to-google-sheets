# MyFitnessPal to Google Sheets

This Python script will take your MyFitnessPal data and put it into a Google Sheet.

![mfptosheets](https://github.com/Rolzix/myfitnesspal-to-google-sheets/assets/107266349/922f3eef-8366-4388-9303-13247a376fb6)

## How to use:

### You need:

- python-myfitnesspal ![python-myfitnesspal](https://github.com/coddingtonbear/python-myfitnesspal)

```bash
pip install myfitnesspal
```

- gspread ![gspread](https://github.com/burnash/gspread)

```bash
pip install gspread
```

### For the first time:

- Follow the instructions on the gspread github page here :

  https://docs.gspread.org/en/v5.10.0/oauth2.html#for-bots-using-service-account

or watch this video here (first 2 minutes and 40 seconds is enough):

![video](https://www.youtube.com/watch?v=bu5wXjz2KvU)

- Copy the service account key JSON file into the same directory as the script.

- Log in to MyFitnessPal in your browser. python-myfitnesspal will use your cookies for logging in.

- Change the spreadsheet and sheet names to your own in these two places:

```python
# Replace "HealthTracking" with the name of your spreadsheet
sh = sheets.open("HealthTracking")

# Replace "Sheet1" with the name of your worksheet
worksheet = sh.worksheet("Sheet1")
```

- Then run the script!

### General usage tips:

- The script will start updating the spreadsheet from the second to last row. So yesterdays data will always be updated.
- If you miss more than 1 day, just delete the spreadsheet rows until the day you want to start updating from. The script will know which day to start from by reading the date on the last cell of the first column.

## Future Improvements:

- [] Change the script to use oauth2 instead of a service account.

- [] Include standalone .exe to run the script without coding knowledge.

  - [] Include variables to remember and change the spreadsheet and sheet names

  - [] Include GUI

## Lessons Learned:

Notable Firsts:

- First project with Python.
-
- First time using a Python library to access data on a website.
-
- First time using a Python library to access a Google API.

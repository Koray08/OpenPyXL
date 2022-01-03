from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
ws.title = "Data"

ws.append(["Koray", "Is", "Great", "!"])
ws.append(["Koray", "Is", "Great", "!"])
ws.append(["Koray", "Is", "Great", "!"])

wb.save("Grades.xlsx")

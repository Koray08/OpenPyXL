from openpyxl import Workbook, load_workbook

wb = load_workbook("Grades.xlsx")
ws = wb.active

ws.insert_rows(7)
ws.insert_rows(7)
ws.delete_rows(7)
ws.insert_cols(2)

# ws.move_range("C1:D11", rows=2,cols=2)

wb.save("Grades.xlsx")
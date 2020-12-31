import xlsxwriter


class DiplomaAutomaticoTestCase():
    def setUp(self):
        return True

if __name__ == "__main__":  
    workbook = xlsxwriter.Workbook('tests.xlsx')
    worksheet = workbook.add_worksheet("Worksheet")

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)
    workbook.close()
pass
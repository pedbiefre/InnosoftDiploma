import pandas as pd


class DiplomaAutomaticoTestCase():
    def setUp(self):
        return True

if __name__ == "__main__":  
    # Create a Pandas dataframe from the data.
    df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('tests.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Worksheet', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
pass
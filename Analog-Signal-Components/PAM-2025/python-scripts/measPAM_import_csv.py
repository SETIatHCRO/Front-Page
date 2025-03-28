import datetime

def importSingleSeriesFromCsvFile(fileName, colDeli=';'):
    '''Reads the contents of a CSV file and translates it into a single data series

    Parameters:
    * fileName: Name/path of the CSV file to be read. The content is expected to be:
        1. Column headers separated by colDeli
        2. Then any number of rows with the actual measured values, also separated by colDeli
    * colDeli: CSV column delimiter with ; as the default value
    
    Return value: Data series as a list consisting of:
    1. Column headers as a list of strings at element [1]
    2. Any number of column lists with the actual measured values in the form of float values from element [2] onwards
    '''
    singleSeries = []
    try:
        # Open the file for reading. If it does not exist, a FileNotFoundError is raised.
        with open(fileName, 'r', encoding='utf-8') as myFile:
            # Read all lines and return them as a string list
            allLines = myFile.readlines()
        # A close() is automatically performed when leaving the with block.
        # Translate string list into a single time data series
        singleSeries = parseSingleSeries(csvLines=allLines, colDeli=colDeli)
    except FileNotFoundError:
        # File does not exist
        print(f'ERROR: File "{fileName}" was not found!')
    except OSError as error:
        # Other errors, e.g., missing permission
        print(f'ERROR READING FILE "{fileName}"')
        print(error)
    except Exception as error:
        # Other errors that occurred during parsing
        print(f'ERROR PARSING FILE "{fileName}"')
        print(error)
    return singleSeries

def parseSingleSeries(csvLines, colDeli=';'):
    '''Translates a list of CSV lines into a single data series

    Parameters:
    * csvLines: List of CSV lines (each with or without a line break at the end) in the following format:
        1. Column headers separated by colDeli
        2. Then any number of rows with the actual values, also separated by colDeli
    * colDeli: CSV column delimiter with ; as the default value
    
    Return value: Data series as a list consisting of:
    1. Column headers as a list of strings at element [1]
    2. Any number of column lists with the actual measured values in the form of float values from element [2] onwards
    '''
    # Parsing only makes sense if there are at least two lines: column headers and at least one data row
    # If not: terminate with an exception
    if len(csvLines) < 2:
        raise Exception(f'ERROR in parseSingleTimeSeries(): Less than two lines: "{csvLines}"')
    
    # Enough lines are available, we can start:
    timeSeries = []

    # The column headers are at csvLines[0]
    headingString = csvLines[0].rstrip()        # First, remove line breaks and whitespace at the right end
    columnTitles = headingString.split(colDeli) # Then split into a list of strings
    timeSeries.append(columnTitles) # Add list of column headers to the time data series
    columnCount = len(columnTitles)   # Remember the number of columns
    # Create as many column lists as there are columns and add them to the time data series:
    for i in range(columnCount): # e.g., 0, 1, 2 if columnCount=3
        colList = []
        timeSeries.append(colList)

    # Then follow any number of rows with data
    for line in csvLines[1:]: # From index 1 to the end
        # Split the current line into a string list using the column delimiter:
        lineString       = line.rstrip()             # First, remove line breaks and whitespace at the right end
        columnStringList = lineString.split(colDeli) # Then split into a list of strings
        # Ensure the number of columns matches. If not: terminate with an exception
        if len(columnStringList) != columnCount:
            raise Exception(f'Parsing error in parseSingleTimeSeries(): {len(columnStringList)} instead of {columnCount} columns in line "{line}"')
        # Each value from the columnStringList is interpreted and added to the corresponding colList.
        for i in range(columnCount): # e.g., 0, 1, 2 if columnCount has the value 3
            # All columns are interpreted as floating-point numbers
            value = float(columnStringList[i])
            # Add the interpreted value to the corresponding colList.
            # In timeSeries, the colLists start at index 1:
            timeSeries[i+1].append(value)

    return timeSeries
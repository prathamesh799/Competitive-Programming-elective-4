# # DataTable and DataColumn classes
# This exercise converts a csv string (a multi-line string 
# of comma-separated values) into a table, and then allows 
# us to extract individual columns to do some data analysis 
# (here, just taking the average for now).

# Note: you may assume:
# the table is nonempty (so it has at least one row and 
# at least one column) the table is rectangular (so each 
# row has the same number of columns) the first row contains 
# the column labels, which are strings the first column contains 
# the row labels, which are strings all other columns contain 
# data, which are ints, and legally formatted Also:
# ignore empty rows, and ignore leading and trailing
# whitespace on any row

# Here is an example of such data:
# csvData = '''
#     Name,Hw1,Hw2,Quiz1,Quiz2
#     Fred,94,88,82,92
#     Wilma,98,80,80,100
#     '''
# With this in mind, write the class DataTable and also 
# the class DataColumn so the following test function passes 
# (without hardcoding any test cases):

class DataColumn:
    def __init__(self, col) -> None:
        self.label = col[0]
        col = col[1:]
        self.data = list(map(int, col))

    def average(self):
        data = self.data
        return sum(data) // len(data)

class DataTable:
    def __init__(self, data) -> None:
        data = data.strip()
        self.rows = data.split('\n')
        for i in range(len(self.rows)):
            self.rows[i] = self.rows[i].strip().split(',')
        # print('rows', self.rows)
        self.cols = []
        for i in range(len(self.rows[0])):
            col = []
            for j in range(len(self.rows)):
                col.append(self.rows[j][i])
            self.cols.append(col)
        # print('cols',self.cols)
        self.cols_ = [DataColumn(each) for each in self.cols[1:]]
    
    def getColumn(self, ind):
        return self.cols_[ind-1]

    def getDims(self):
        return len(self.rows), len(self.cols)

def almostEqual(a, b):
    return a == b

def testDataTableAndDataColumnClasses():
    print('Testing DataTable and DataColumn classes...', end='')
    csvData = '''
    Name,Hw1,Hw2,Quiz1,Quiz2
    Fred,94,88,82,92
    Wilma,98,80,80,100
    '''
    dataTable = DataTable(csvData)
    rows, cols = dataTable.getDims()
    # print(rows, cols)
    assert((rows == 3) and (cols == 5))

    column3 = dataTable.getColumn(3)
    assert(isinstance(column3, DataColumn))
    # print('col 3 label', column3.label)
    assert(column3.label == 'Quiz1')
    assert(column3.data == [82, 80])
    assert(almostEqual(column3.average(), 81))

    column4 = dataTable.getColumn(4)
    assert(isinstance(column4, DataColumn))
    assert(column4.label == 'Quiz2')
    assert(column4.data == [92, 100])
    assert(almostEqual(column4.average(), 96))
    print('All test cases passed....!')

print(testDataTableAndDataColumnClasses())
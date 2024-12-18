class StudentData:
    def __init__(self):
        self.Total = 0.00
        self.Average = 0.00
        self.Percentage = 0.00
        self.Marks = []
        self.MaxMarks = 0.00

    def main(self):
        print("Enter the marks of five subjects::")

        for i in range(5):
            self.Marks.append( float (input ()))

    def CalcMaxMarks (self):
        return len (self.Marks) * 100

    def CalcTotal (self):
        self.Total = 0
        for i in self.Marks:
            self.Total += i
        return self.Total

    def CalcAvg (self):
        self.Average = self.Total / len (self.Marks)
        return self.Average

    def CalcPercentage (self):
        return (self.Total * 100) / (len (self.Marks) * 100)

    def CalcGrade (self):
        Grade = None
        if self.Average >= 90:
            Grade = 'A'
        elif self.Average >= 80 and self.Average < 90:
            Grade = 'B'
        elif self.Average >= 70 and self.Average < 80:
            Grade = 'C'
        elif self.Average >= 60 and self.Average < 70:
            Grade = 'D'
        else:
            Grade = 'E'
        return Grade

    def CalcResult (self):
        c = 0
        for i in self.Marks:
            if i >= 40:
                c += 1

        if c == len (self.Marks):
            return 'Passed'
        else:
            return 'Failed'



StudentData = StudentData()

StudentData.main()


print ("\nThe Total marks is:   \t", StudentData.CalcTotal(), "/", StudentData.CalcMaxMarks())
print ("\nThe Average marks is: \t", StudentData.CalcAvg())
print ("\nThe Percentage is:    \t", StudentData.CalcPercentage(), "%")
print ("\nThe Grade is:         \t", StudentData.CalcGrade())
print ("\nThe Result is:        \t", StudentData.CalcResult())

def findColumnSum(matrix):
    columnSums = []

    for j in range(len(matrix[0])):
        columnSum = 0
        for i in range(len(matrix)):
            columnSum += matrix[i][j]
        columnSums.append(columnSum)

    return columnSums


if __name__ == "__main__":
    noOfRows = int(input("Enter the no.of rows : "))

    matrix = []
    for i in range(noOfRows):
        matrix.append(list(map(int, input().strip('[').strip(']').split(','))))

    print(findColumnSum(matrix))

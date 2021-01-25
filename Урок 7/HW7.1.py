class Matrix:
    def __init__(self, lst):
        self.my_matrix = lst

    def __str__(self):
        res = ""
        for i in self.my_matrix:
            res += str(i) + '\n'
        return res

    def __add__(self, other):
        return [(lambda i: [self.my_matrix[i][s] + other.my_matrix[i][s] for s in range(len(self.my_matrix[i]))])(i) for i in range(len(self.my_matrix))]


one = [[1, 2], [3, 4], [5, 6]]
two = [[12, 8], [3, 7], [14, 1]]
test_one = Matrix(one)
tes_two = Matrix(two)
print(f'Первый экземпляр класса \n{test_one}')
print(f'Второй экземпляр класса \n{tes_two}')
print(f'Сумма всех экземплят=ров класса = {test_one + tes_two}')

#print([(lambda i: [lst1[i][b] + lst2[i][b] for b in range(len(lst1[i]))])(i) for i in range(len(lst1))])
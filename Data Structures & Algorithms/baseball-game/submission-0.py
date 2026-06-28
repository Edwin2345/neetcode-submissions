class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        rec_sum = 0

        for i in range(len(operations)):
            if operations[i] == '+':
                operation = int(record[-1]) + int(record[-2])
                rec_sum += operation
                record.append(operation)

            elif operations[i] == 'D':
                operation = int(record[-1])*2
                rec_sum += operation
                record.append(operation)
            
            elif operations[i] == 'C':
                rec_sum -= record.pop()
            
            else:
                record.append(int(operations[i]))
                rec_sum += int(operations[i])
        
        return rec_sum
        
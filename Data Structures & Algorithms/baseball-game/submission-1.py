class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        rec_sum = 0

        for op in operations:
            if op == '+':
                operation = record[-1]+ record[-2]
                rec_sum += operation
                record.append(operation)

            elif op == 'D':
                operation = record[-1]*2
                rec_sum += operation
                record.append(operation)
            
            elif op == 'C':
                rec_sum -= record.pop()
            
            else:
                record.append(int(op))
                rec_sum += int(op)
        
        return rec_sum
        
class MathList:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        list = self.value

        for index in range(len(list)):
            list[index] = list[index] + other
        
        return list
    
    def __sub__(self, other):
        list = self.value
        
        for index in range(len(list)):
            list[index] = list[index] - other
        
        return list
    
m_list= MathList([1, 2, 3, 4, 5])
print(m_list)

m_list += 2
print(m_list)

# m_list -= 2
# print(m_list)
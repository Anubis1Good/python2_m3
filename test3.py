class Child():
    def __init__(self,name ):
        self.name = name
    
    def __str__(self) -> str:
        return f'Child is {self.name}'
    
print(Child('Ivan'))
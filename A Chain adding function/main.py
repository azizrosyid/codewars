class ChainInteger(int):
    def __call__(self,v):
        return ChainInteger(self+v)

def add(number):
    return ChainInteger(number)

print(add(341)(213))
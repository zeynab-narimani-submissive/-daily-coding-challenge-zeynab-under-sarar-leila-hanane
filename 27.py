class animal:
    def WhereToSleep(self,place):
        return "I sleep in " + place
    def WhatToEat(self,food):
        return "I eat " + food
class cat(animal):
    def WhatToSay(self):
        return "I Say meow"
obj1 = animal()
obj2 = cat()
print(obj1.WhereToSleep("house"), obj1.WhatToEat("carrot"))
print(obj2.WhereToSleep("bed"), obj2.WhatToEat("chicken"))
print(obj2.WhatToSay())
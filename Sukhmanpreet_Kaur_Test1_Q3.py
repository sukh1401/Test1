class Temperatures:
    
    def __init__(self,city):
        self.temps=[]
        self.city=city

    def enterTemp(self):
        for n in range(3):
            temp=input(f"Enter temperature for day {n+1}  in  {self.city}: ")
            temp=float(temp)
            self.temps.append(temp)
        print()

    def displayTemp(self):
        print(f"{self.city} recorded the following temperatures {self.temps}\n")

    def calcAverageTemp(self):
        total=0
        for temp in self.temps:
            total+=temp
        
        avg=total/3
        avg=round(avg,1)
        print(f"The average temperature for {self.city} across three days was {avg}\n")



cities =["Berlin","Tokyo","Nairobi"]
cities_temps=[]


for city in cities:
    city_temp=Temperatures(city)
    city_temp.enterTemp()
    cities_temps.append(city_temp)


for city_temp in cities_temps:
    city_temp.displayTemp()


for city_temp in cities_temps:
    city_temp.calcAverageTemp()


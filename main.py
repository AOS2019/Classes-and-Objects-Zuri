class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
    # Adds an instance variable 
    def change_name(self, name):
        print(name)
        # Retrieves instance variable
    def change_age(self, age):
        print(int(age))
        
    def add_track(self, tracks):
       
        self.tracks += [tracks]
        print(str(self.tracks))
    
    def get_score(self):
        print(self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

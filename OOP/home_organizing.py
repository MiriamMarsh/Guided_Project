class Home_Organizer:
    def __init__(self,num_shirts_to_fold):
        self.num_shirts_to_fold = num_shirts_to_fold


    def sweep(self):
        print("Please sweep the floor")
    def fold_laundry(self):
        print("Please fold the laundry with a total number shirts to fold or", self.num_shirts_to_fold)
    def wash_dishes(self):
        print("wash dishes")      
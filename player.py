class Player:
    
    
 
    def __init__(self, name):
        self.name = name
        self.points = 99
        self.used_points_history = []
        self.points_indicator_mapping = {range(1,20): '1~19',
                                        range(20,40): '20~39',
                                        range(40,60): '40~59',
                                        range(60,80): '60~79',
                                        range(80,100): '80~99'}
        self.used_points_indicator_mapping = {range(1,10): 'Black', range(10,100): 'White' }
   
    def displayLeftPointsIndicator(self):
        for i in self.points_indicator_mapping:
            if self.points in i:
                indicator = self.points_indicator_mapping[i]
        print(f"{self.name}'s left points fall within {indicator}")
 
    def usePoints(self, used_points):
        self.points = self.points - used_points
        self.used_points_history.append(used_points)
        for i in self.used_points_indicator_mapping:
            if used_points in i:
                print(self.used_points_indicator_mapping[i])

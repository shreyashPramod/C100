class Car (object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model

    def start(self):
        print("started")

    def stop(self):
        print("stopped")
    
    def accelerate(self):
        print("accelereating....")

    def change_gear(self,gear_type):
        print("gear changed")

    
audi=Car("a6","red","audi","80")
audi.start()
audi.stop()
audi.accelerate()
audi.change_gear("2 gear")


        
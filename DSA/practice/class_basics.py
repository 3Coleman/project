class cookies:
    def __init__(self,color):
        self.color=color
    def current_color(self):
        return self.color
    def replace(self,color):
        self.color=color
        
cookie1=cookies("yellow")
cookie1.replace("blue")
print(cookie1.current_color())
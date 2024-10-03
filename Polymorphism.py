class Android1:
    def button(self):
        return "color red" 
    
    def speed(self):
        return "1.5"

    def logo(self):
        return "virus logo"
    
class Android2(Android1):
    def sizee(self):
        return "100"
        
    def button(self):          #method overRiding
        return "color green"
    
os = Android2()
print(os.button())
print(os.logo())
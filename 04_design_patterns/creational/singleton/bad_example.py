class Logger:
        
    def __int__(self,file_name:str):
        self.file_name = file_name
        self.log_count = 0

    def log(self,text:str):
        print(f"Logger is logging {text} in {self.file_name}")
        self.log_count += 1

log1 = Logger("app.log")
log2 = Logger("app.log")
log3 = Logger("app.log")



log1.log("User  is checking balance")

log2.log("Staff is blocking someone")

log3.log("User3 is blocked")

print(log1.log_count)  # 1
print(log2.log_count)  # 1
print(log3.log_count)    #1


print(id(log1))  
print(id(log2))  
print(id(log3))  

# all should have  same object id




# all should be  print 3 instead of 1
      
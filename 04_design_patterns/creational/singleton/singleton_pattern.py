class Logger:
    _instance = None

    def __new__(cls, file_name: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.file_name = file_name
            cls._instance.log_count = 0

        return cls._instance

    def log(self, msg: str):
        print(f"Logging {msg} in {self.file_name}")
        self.log_count += 1

    def get_log_count(self) -> int:
        return self.log_count


# Client
logger1 = Logger("app.log")
logger2 = Logger("error.log")

logger1.log("Application started")
logger2.log("Something went wrong")

print(logger1 is logger2)       # True
print(logger1.get_log_count())  # 2
class Logger:
    def __init__(self):
        print("Logger object created")

    def __del__(self):
        print("Logger object destroyed")

log = Logger()
del log
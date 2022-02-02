from numpy import true_divide
import psutil

class Dashboard():
    def __init__(self) -> None:
        self.fristRun = True
        self._cpu_threads = psutil.cpu_count()
        self._cpu_cores = psutil.cpu_count(logical=False)
        self.showCPU()
       # self.showLoadAVG()
        self.monitor()
    def showCPU(self):
        print(f"CPU: {self._cpu_cores}/{self._cpu_threads}")
    def showLoadAVG(self):
        print(psutil.getloadavg())
    def monitor(self):
        while True:
            if self.fristRun is True:
                self.fristRun = False
                print(f"Threads:[]")
            else:
                print(f"Threads:{psutil.cpu_percent(percpu=True, interval=1)}")
        
        
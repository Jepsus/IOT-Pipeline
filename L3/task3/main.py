from Components.counter import Counter
from Components.dashboard import Dashboard




def main():
    counter1 = Counter()
    print(counter1.getCount()) # 0
    counter1.addCount()
    print(counter1.getCount()) # 1
    myDash = Dashboard()

if __name__ == "__main__":
    main()
    
#In the name of GOD
# Time in python

import time

##start = time.time()
##for i in range(1000000):
##    pass
##end = time.time()
##print("Elapsed time is {}".format(end-start))






##import threading
##end = None
##start = None
##def hello():
##    global start, end
##    start = time.thread_time()
##    x = 0
##    while x < 10000000:
##        pass
##        x += 1
##    end = time.thread_time()
##t = threading.Thread(target = hello, args = () )
##t.start()
##t.join()
##print("The time spent is {}".format(end - start ) )






##from time import process_time, sleep
##iterations = 1000
##start = process_time()
##for i in range(iterations):
##    print(i, end=" ")
## Stop the stopwatch / counter
##end = process_time()
##print(end, start)
##print("Elapsed time in seconds:" , end-start)




##from time import perf_counter, sleep
### integer input from user, 2 input in single line
##n = 3
### Start the stopwatch / counter 
##start = perf_counter()
##for i in range(n):
##    sleep(1)
##end = perf_counter()
##print("Elapsed time in seconds:", end-start) 





##from time import monotonic, sleep
### integer input from user, 2 input in single line
##n = 3
### Start the stopwatch / counter
##start = monotonic()
##for i in range(n):
##    sleep(1)
##end = monotonic()
##
##print("Elapsed time in seconds:", end-start)




##class Timer:
##    def __init__(self):
##        self.start = time.time()
##    def start(self):
##        self.start = time.time()
##    def log(self):
##        logger = time.time() - self.start
##        print('Time log -',logger)
##    def milestone(self):
##        self.start = time.time()
##
##time1 = Timer()
##for i in range(1000000):
##    pass
##    p = 1
##time1.log()
##for i in range(1000000):
##    pass
##    p = 1
##time1.log()
##        



##
### Importing the Timer subclass from the threading Class
##from threading import Timer
### creating a basic function that will print "hello"
##def hello():
##    print ("hello, world")
### creating the object of the Timer subclass
### Here, 5 sec means that the execution of the function="hello" after 5 seconds
##t = Timer(interval=5.0, function=hello)
### starting the execution
##t.start() # after 30 seconds, "hello, world" will be printed
##
##
##print("Execution begins")
##
### cancelling the execution of the 'hello' function
##t.cancel()
##print("END")
##
##import threading
##
### To take multiple inputs we can use *before the parameter.
##def print_name(*names):
##    # From the array of names pick one name and print it
##    for name in names:
##        print("Hello",name)
### In the args parameter, give an array of names 
##t = threading.Timer(3, print_name,["Ashwini","Vandy","Arijit"])
### start the execution
##t.start()
##print("Execution begins...")



### We will use the time module
##import time
### Create a function that will print the time
##def create_countdown_timer(time):
##    print(time,"......")
##
##time_in_sec=int(input("Please entert the time in seconds:"))
##
##for times in range(time_in_sec):
##    # call the function and pass the current time left
##    create_countdown_timer(time_in_sec-times)
##    # call the function in every 1 second.
##    time.sleep(1)
##
##print("Time is up")
##
##
##from threading import Timer
### Create a function that will print the time
##def create_countdown_timer(time):
##    print(time,"......")
##   
### Here you have to enter the time for which the timer will run
##time_in_sec=int(input("Please enter the time in seconds:"))
### For the first time we will call the function manually
##create_countdown_timer(time_in_sec) 
##for times in range(1,time_in_sec):
##    # calling the Timer class every second
##    t = Timer(1,create_countdown_timer,[str(time_in_sec-times)])
##    t.start()
##    time.sleep(1)
##
##print("\n Time is up")


##import time
##def check_time(func):
##    def inner(*args, **kwargs):
##        start = time.time()
##        func(*args, **kwargs)
##        end = time.time()
##        print("Time taken to execute function is ", end-start)
##    return inner
##
##@check_time
##def task():
##    # do something
##    for i in range(10000000):
##        x = 0
##        pass
##task()




class Timer:
    """
    Timer class
    """
    def __init__(self):
        self.start = time.time()
    '''
    Restarts the timer.
    '''
    def restart(self):
        self.start = time.time()

    '''
    Returns the time elapsed and resets the counter.
    '''
    def get_new_time(self):
        value = time.time() - self.start
        self.restart()
        return value

    '''
    Prints the time elapsed and resets the counter.
    '''
    def print_new_time(self):
        print (self.get_new_time())

    '''
    Returns the time elapsed (Does not reset the counter).
    '''
    def get_time(self):
        return time.time() - self.start
        self.restart()

    '''
    Prints the time elapsed (Does not reset the counter).
    '''
    def print_time(self):
        print(self.get_time())

    '''
    Returns the time elapsed in HH:mm:ss (Does not reset the counter).
    '''
    def get_time_hhmmss(self):
        end = time.time()
        m, s = divmod(end - self.start, 60)
        h, m = divmod(m, 60)
        time_str = "%02d:%02d:%02d" % (h, m, s)
        return time_str

timer = Timer() #Initialize the timer
#wash clothes for 5 seconds
timer.print_time() #Print the time elapsed since Initialization (in seconds)
#dry clothes for 3 seconds
timer.print_new_time() #Print the time elapsed since Initialization and reset the timer
#burn clothes for 10 seconds
print(str('Task done for ' + str(timer.get_time()) + ' seconds.'))

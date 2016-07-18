'''
Multi-pourpace timer class to, well, track time.
Each timer has a couple of key varibles:
	Handler,
	Repeat,
	and delay

The handler is the code that runs when the timer gets to 0.

The repeat is a bool that tells weather the timer should reset iteself automaticialy when it runs down

and finally, the delay is how long the timer will run for.

#
# Version 1.2
#
'''
# Timer class
# Make shure to import time
import time
# Gooood
class Timer(object):

    timers = []  # create an empty list of all timers

    def process():
    # Timer processor, called from the main loop at the class
    # level to process timers
        for timer_object in Timer.timers:
            if timer_object.delay > 0.0: # timer is active
                if (time.time() - timer_object.start_time) > timer_object.delay:
                    # timer has timed out
                    timer_object.state = True
                    #timer_object.start_time = time.time()
                    if not (timer_object.handler == ''): # see if handler exists
                        timer_object.handler() # call the handler
                    if not timer_object.repeat:
                        timer_object.delay = 0.0
                    # else leave the delay in place so it will repeat

    def __init__(self,name='',handler='',repeat=False):
    # constructor for timer, must set with .set() method
        self.name = name
        self.start_time = time.time()
        self.delay = 0.0
        self.handler = ''
        self.repeat = repeat
        self.state = False  # show time not timed out
        Timer.timers += [self] # add timer object to the list of timers
        

    def set(self,delay,handler='',repeat=False):
    # set a timer, optionally associate a handler with it
        self.delay = delay    # time period in seconds
        self.handler = handler
        self.repeat = repeat
        self.start_time = time.time()

    def check_state(self):
    # check the state of the timer, return true if timed out
        return self.state

    def reset_state(self):
    # reset the state of the counter to false
        self.state = False
        
    def cancel(self):
    # cancel a timer
        self.delay = 0.0
        self.state = False
    def return_eta(self):
        #Returns the Time sence start of a timer, in secounds
        temp_eta = int(time.time() - self.start_time)
        return str(temp_eta)



        
#------------------ End of Timer Class -------------------------------------        


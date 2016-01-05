import subprocess as sp
import time

class Animation(object): 
    
    def __init__(self,file_name,lines_per_frame):
        
        #Open the file and put the lines in a list
        with open (file_name, "r") as text_file:
            data = text_file.readlines()
            
        #Create a spot for each frame in the list
        self.frames = [""] * len(data)
        
        #Add the frames to the frames list
        for block_number in range( len(data) / lines_per_frame ):
            for line_number in range(len(data)):
                if line_number < (block_number + 1 * lines_per_frame) and line_number > (block_number - 1 * lines_per_frame):
                    self.frames[block_number] += data[line_number]
                
                
            
        
        
    def run_animation(self,loops,fps):
        #Runs the animation at a desired framerate and loops it a given amount of times
        delay = 1.0/fps
        for _ in range(0,loops):
            for frame in self.frames:
                #The following line clears the shell
                sp.call('clear',shell=True)
                print frame
                time.sleep(delay)

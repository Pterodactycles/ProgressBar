
import os
import time

###############################################################################

class ProgressBar():
    
    
    
    def __init__(self):
        self.starttime = time.time()
    
    
    
    def compute_time_elapsed(self):
        self.time_elapsed = time.time() - self.starttime
        if self.time_elapsed < 60:
            self.time_elapsed_str = '\033[1;35m' + f'{self.time_elapsed:.2f} s' + '\033[0m'
        elif self.time_elapsed >= 60:
            self.time_elapsed_str = '\033[1;35m' + f'{self.time_elapsed / 60:.2f} mins' + '\033[0m'
    
    
    
    def compute_time_remaining(self,progress_fraction):
        self.total_time = 1 / progress_fraction * self.time_elapsed
        self.time_remaining = self.total_time - self.time_elapsed
        if self.time_remaining < 60:
            self.time_remaining_str = '\033[1;36m' + f'{self.time_remaining:.2f} s' + '\033[0m'
        elif self.time_remaining >= 60:
            self.time_remaining_str = '\033[1;36m' + f'{self.time_remaining / 60:.2f} mins' + '\033[0m'
    
    
    
    def print_progress_with_time(self,iteration,total):
        
        progress_fraction = iteration / total
        progress = int(self.width * progress_fraction)
        packer = int(self.width - progress)
        progress_str = "=" * progress
        packer_str = "-" * packer
        
        if progress_fraction < 0.1:
            self.progress_fraction_str = '|  ' + '\033[1;33m' + f'{progress_fraction*100:.1f}%' + '\033[0m'
        elif progress_fraction >= 0.1 and progress_fraction < 1:
            self.progress_fraction_str = '| ' + '\033[1;33m' + f'{progress_fraction*100:.1f}%' + '\033[0m'
        else:
            self.progress_fraction_str = '|' + '\033[1;32m' + f'{progress_fraction*100:.1f}%' + '\033[0m'
        
        self.compute_time_elapsed()
        self.compute_time_remaining(progress_fraction)
        
        if self.inline == True:
            if iteration != total:
                ending = "\r"
            elif iteration == total:
                ending = "\n"
            print('Progress: 0%|' + 
                  '\033[0;32;40m' + f'{progress_str}' +'\033[0m' + 
                  '\033[5;33;40m' + f'{packer_str}' + '\033[0m' + 
                  self.progress_fraction_str + '|' + 
                  self.time_elapsed_str +'|' + 'eta ' +
                  self.time_remaining_str + '|     ',
                  sep='',
                  end=ending,
                  flush=True)
        
        elif self.inline == False:
            ending = "\n"
            print('Progress: 0%|' + 
                  '\033[0;32;40m' + f'{progress_str}' +'\033[0m' + 
                  '\033[1;33;40m' + f'{packer_str}' + '\033[0m' + 
                  self.progress_fraction_str + '|' + 
                  self.time_elapsed_str +'|' + 'eta ' +
                  self.time_remaining_str + '|     ',
                  sep='',
                  end=ending,
                  flush=True)
    
    
    
    def print_progress_without_time(self,iteration,total):
        
        progress_fraction = iteration / total
        progress = int(self.width * progress_fraction)
        packer = int(self.width - progress)
        progress_str = "=" * progress
        packer_str = "-" * packer
        
        if progress_fraction < 0.1:
            self.progress_fraction_str = '|  ' + '\033[1;33m' + f'{progress_fraction*100:.1f}%' + '\033[0m'
        elif progress_fraction >= 0.1 and progress_fraction < 1:
            self.progress_fraction_str = '| ' + '\033[1;33m' + f'{progress_fraction*100:.1f}%' + '\033[0m'
        else:
            self.progress_fraction_str = '|' + '\033[1;32m' + f'{progress_fraction*100:.1f}%' + '\033[0m'
        
        if self.inline == True:
            if iteration != total:
                ending = "\r"
            elif iteration == total:
                ending = "\n"
            print('Progress: 0%|' + 
                  '\033[0;32;40m' + f'{progress_str}' +'\033[0m' + 
                  '\033[5;33;40m' + f'{packer_str}' + '\033[0m' + 
                  self.progress_fraction_str,
                  sep='',
                  end=ending,
                  flush=True)
        
        elif self.inline == False:
            ending = "\n"
            print('Progress: 0%|' + 
                  '\033[0;32;40m' + f'{progress_str}' +'\033[0m' + 
                  '\033[1;33;40m' + f'{packer_str}' + '\033[0m' + 
                  self.progress_fraction_str,
                  sep='',
                  end=ending,
                  flush=True)
    
    
    
    def display_progress(self,iteration,total,width=50,inline=True,time=False):
        
        self.width = width
        self.inline = inline

        if time == True:
            self.print_progress_with_time(iteration,total)
        
        elif time == False:
            self.print_progress_without_time(iteration,total)









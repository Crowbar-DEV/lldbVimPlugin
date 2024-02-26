import pynvim
import os

@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function
    def step_over(self):
        os.system('python3 ~/shithole/CrowCave/vimtest/testsrc/lldbAdapter/client.py')



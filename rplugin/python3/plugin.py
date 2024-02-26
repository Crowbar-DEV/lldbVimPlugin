import neovim
import os

@neovim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('step_over')
    def step_over(self, args):
        os.system('python3 ~/shithole/CrowCave/vimtest/testsrc/lldbAdapter/client.py')



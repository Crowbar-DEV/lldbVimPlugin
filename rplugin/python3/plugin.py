import neovim
import os

@neovim.plugin
class Main(object):
    def __init__(self, vim):
        self.vim = vim

    @neovim.function('StepOver')
    def StepOver(self, args):
        os.system("python3 ~/shithole/CrowCave/vimtest/testsrc/lldbAdapter/client.py")


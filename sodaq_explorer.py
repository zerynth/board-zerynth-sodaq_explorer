from base import *
from devices import *
import time

class SodaqExplorer(Board):

    vendor_pid = [("2341", "824E")]   
    #vendor_pid = ("2341", "004E")

    @staticmethod
    def match(dev):
        return (dev["vid"], dev["pid"]) in SodaqExplorer.vendor_pid

    def reset(self):
        pass

    def burn(self,bin):
        return False,"Must be put in virtualization mode first!"

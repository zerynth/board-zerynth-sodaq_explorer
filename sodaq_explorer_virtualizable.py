from base import *
from devices import *

class SodaqExplorerVirtualizable(Board):
    #vendor_pid = ("2341", "024E")
    vendor_pid = [("2341", "004E"),("2341", "024E"), ("2341", "024D")]

    @staticmethod
    def match(dev):
        return (dev["vid"], dev["pid"]) in SodaqExplorerVirtualizable.vendor_pid

    def reset(self):
        pass

    def burn(self,bin,outfn=None):
        fname = fs.get_tempfile(bin)
        res,out,err = proc.runcmd("bossac_d21","-i","-d","-e","-w","-v","-R", "-p", self.port,fname,outfn=outfn)
        fs.del_tempfile(fname)
        if res:
            return False,out
        return True,out


    def __init__(self,info={},dev={}):
        super().__init__(info,dev)
        self._info["name"] = "SODAQ ExpLoRer Virtualizable"

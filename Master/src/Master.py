#!/usr/bin/python3

import MasterConfig
import PowerBoxProxy
import MusicPlayer
import ShowRunner
import time

class MasterController:
    def __init__(self):
        # Create objects
        self.cfg = MasterConfig.MasterConfig()

        # Create the MusicPlayer to handle the music.  This will be passed to the ShowRunner.
        self.player = MusicPlayer.MusicPlayer(self.cfg.getMusicDir())

        # Using the list of configured Power Boxes, instantiate the power box list
        self.powerBoxList = {}
        self.powerBoxConfig = self.cfg.getPowerBoxList()
        for box in self.powerBoxConfig:
            self.powerBoxList[box['id']] = PowerBoxProxy.PowerBoxProxy(box['address'], box['port'], box['channels'])

        # Connect each PowerBoxProxy to its associated Power Box
        print("The following Power Boxes have been configured:")
        for box in self.powerBoxList:
            print("    Box #" + str(box) + ", address: " + self.powerBoxList[box].address + ", port: " + str(self.powerBoxList[box].port) + ", channels: " + str(self.powerBoxList[box].numChannels))
            self.powerBoxList[box].connect()

        # Create the Show runner that will reach each script and run the show.
        self.showRunner = ShowRunner.ShowRunner(self.powerBoxList, self.player, self.cfg.getMusicDir())

        return

    def allLightsOn(self):
        for box in self.powerBoxList:
            self.powerBoxList[box].sendCmd('*', 'ON')
        return

    def allLightsOff(self):
        for box in self.powerBoxList:
            self.powerBoxList[box].sendCmd('*', 'OFF')
        return

    def Main(self):
        #TODO

#        self.powerBoxList[1].sendCmd(1,"ON")
#        self.powerBoxList[2].sendCmd(5,"OFF")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[2].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")
#        self.powerBoxList[1].sendCmd(8,"ON")

#        self.powerBoxList[2].sendCmd(16,"OFF")

#        self.player.playSong("carol-of-the-bells.mp3")
#        time.sleep(10)
#        self.player.stop()

        self.allLightsOn()
        self.allLightsOff()
        self.showRunner.readScript("carol-of-the-bells")
        self.showRunner.runScript()


if __name__== '__main__':
    mcp = MasterController()
    mcp.Main()

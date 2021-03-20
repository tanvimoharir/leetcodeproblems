class UndergroundSystem:

    def __init__(self):
        #checkins[id]={startSation,time}
        self.checkins={}
        #trips[start+end]={totalduration,count}
        self.trips={}        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id]=(stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start,startTime=self.checkins[id]
        if (start+stationName) not in self.trips:
            self.trips[start+stationName]=(t-startTime,1)
        else:
            timeTillNow,count=self.trips[start+stationName]
            self.trips[start+stationName]=(timeTillNow+(t-startTime),count+1)
            

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalDuration,count=self.trips[startStation+endStation]
        return float(totalDuration/count)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

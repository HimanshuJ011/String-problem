input = "2?:??"

class Solution:
    def getmax(self, time):
        if "?" not in time[:2] and time[:2] >= "24": return -1
        maxrg = 24*60-1
        newtime = ""
        for i in range(len(time)):
            if time[i] != "?":
                newtime += time[i]
            else:
                if i == 0:
                    newtime += "2"
                elif i == 1:
                    if time[0] != "?" and int(time[0]) < 2:
                        newtime += "9"
                    else:
                        newtime += "4"
                elif i == 3:
                    newtime += "5"
                elif i == 4:
                    newtime += "9"

        if int(newtime[:2])*60 + int(newtime[3:]) > maxrg:
            for i in range(1, -1, -1):
                if time[i] == "?":
                    if i == 1:
                        newtime = newtime[0] + str(int(newtime[1])-1) + newtime[2:]
                        break
                    elif i == 0:
                        newtime = "1" + newtime[1:]
                        break
        return newtime

getmax = Solution()
print(getmax.getmax(input))

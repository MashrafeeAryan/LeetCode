from collections import defaultdict
class TimeMap:
    """
    U: We are creating a data structure similar to a dictioanry with key and values. However, one key can have multiple values because the differentiator will be the timestamp.
    M:
    P:
    data will be a dict variable
    Set stores the value in the dict. I would assume a siple way is nested dicts.
    so a simple way would be 
    {key: {timestamp: value, timestamp: value}}
    to set it
    data[key][timestamp] = value
    use defaultdict
    """
    def __init__(self):
        self.data = defaultdict(list)        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        right = len(self.data[key]) - 1
        values = self.data[key]
        while left <= right:
            mid = (left+right)//2

            if values[mid][0] == timestamp:
                return values[mid][1]
            
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right == -1:
            return ""

        return values[right][1]
        #if it exists 
        #if key in self.data and if timestamp not in self.data[key]:
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
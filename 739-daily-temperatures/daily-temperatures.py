class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize result array with all zeros
        answer = [0] * len(temperatures)
        
        # Stack holds indices of days waiting for a warmer day
        waiting_days = []
        
        # Go through each day
        for today in range(len(temperatures)):
            today_temp = temperatures[today]
            

            while waiting_days:

                waiting_day = waiting_days[-1]
                waiting_day_temp = temperatures[waiting_day]
                

                if today_temp > waiting_day_temp:

                    waiting_days.pop()
                    days_waited = today - waiting_day
                    answer[waiting_day] = days_waited
                else:

                    break
            

            waiting_days.append(today)
        
        return answer
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
        Calculate minimum cost of tickets needed for traveling on given days.
        
        Args:
            days (List[int]): List of days when travel is needed (sorted in ascending order)
            costs (List[int]): Cost of passes [1-day pass, 7-day pass, 30-day pass]
        
        Returns:
            int: Minimum cost to cover all travel days
        """
        # Create a set of travel days for O(1) lookup
        travel_days = set(days)
        
        # Dynamic programming cache
        dp = {}
        
        def dp_solve(day):
            # Base cases
            if day > days[-1]:
                return 0
            if day not in travel_days:
                return dp_solve(day + 1)
            if day in dp:
                return dp[day]
            
            # Calculate minimum cost considering all three pass options
            one_day = dp_solve(day + 1) + costs[0]
            seven_day = dp_solve(day + 7) + costs[1]
            thirty_day = dp_solve(day + 30) + costs[2]
            
            # Store and return minimum cost
            dp[day] = min(one_day, seven_day, thirty_day)
            return dp[day]
        
        return dp_solve(days[0])
import heapq

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def calculate_pass_ratio_gain(passed: int, total: int) -> float:

            return (passed + 1) / (total + 1) - passed / total

        # Create a max heap (using negative values to simulate max heap in Python)
        # Each heap entry is (-pass_ratio_gain, passed_students, total_students)
        max_heap = [
            (-calculate_pass_ratio_gain(passed, total), passed, total) 
            for passed, total in classes
        ]
        heapq.heapify(max_heap)

        # Distribute extra students to maximize pass ratio
        for _ in range(extraStudents):
            # Pop the class with the highest potential pass ratio improvement
            _, passed, total = heapq.heappop(max_heap)
            
            # Add a student to this class and recalculate
            heapq.heappush(
                max_heap, 
                (-calculate_pass_ratio_gain(passed + 1, total + 1), passed + 1, total + 1)
            )

        # Calculate and return the final average pass ratio
        return sum(passed / total for _, passed, total in max_heap) / len(max_heap)
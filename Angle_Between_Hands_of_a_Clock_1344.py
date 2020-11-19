class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # there are 60 mins in a clock, so each minute corresponds to 360/60 = 6 degrees
        # there are 12 hrs in a clock, so each hr corresponds to 360/12 = 30 degrees

        # the idea is to first find out what degree the hour points and what degree the minute points
        # e.g if - hr = 5, we get 5*30 = 150
        #     if - minute = 40, we get 40*6 = 240

        # now, we also need to note that the hour clock will not exactly point to 5, it will be a little more than half way ahead of 5, since its 5:40 and 40 > 30
        # the way we find out how much 5 is ahead is, we know each hr corresponds to 30 degrees so if minutes are 30, it means we have covered half of an hr, that means out of 30 degrees of an hr we have covered 15 degrees, by same logic, we get for 40mins, we cover 20 degrees, we add this 20 degrees to our 5 hr degree

        # so, we get hr = 5, we get 5*30 = 150 + 20 = 170 degree
        # and minute = 40, 40 * 6 = 240

        # final ans = 240 - 170 = 70
        # p.s - if our angle was greater than 180 degree we return 360 - 180 since we need to return smaller angle

        minute_degrees = minutes * 6

        hour_degrees = hour * 30
        hour_hand_movement = (minutes/60) * 30
        total_hour_movement = hour_degrees + hour_hand_movement

        angle = abs(minute_degrees - total_hour_movement)
        # we use abs because there can be times when hour clock is ahead, e.g - hr = 10, minute = 20, in this case hour hand would be ahead, so we will get negative angle, to fix this we use abs

        return angle if angle < 180 else 360 - angle


obj = Solution()
print("Test case: hour: 12, minutes: 30, Expected result = 165.0, Got result =",
      obj.angleClock(12, 30))
print("Test case: hour: 5, minutes: 40, Expected result = 70.0, Got result =",
      obj.angleClock(5, 40))
print("Test case: hour: 10, minutes: 36, Expected result = 102.0, Got result =",
      obj.angleClock(10, 36))

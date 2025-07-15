class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        '''
        yearBefore = year - 1
        leapYears = yearBefore/4 - yearBefore/100 - yearBefore/400
        daysBefore = (year - leapYears) * 365 + leapYears * 366
        return daysBefore
        '''
        day_code = ["Saturday","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        month_code = [1,4,4,0,2,5,0,3,6,1,4,6]
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            month_code[0] = 0
            month_code[1] = 3
        
        if year >= 1900 and year < 2000:
            century_code = 0
        if year >= 2000 and year < 2100:
            century_code = 6
        if year >= 2100:
            century_code = 4
        last_two_digit = year % 100
        leap_year = last_two_digit // 4
        
        odd_day = (day + month_code[month - 1] + century_code + last_two_digit + leap_year) % 7

        return day_code[odd_day]
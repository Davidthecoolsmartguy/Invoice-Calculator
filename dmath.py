def RegularPay(Hours,HourlyRate):
    if Hours <= 8:
        return Hours * HourlyRate
    elif Hours > 8:
        return (HourlyRate * 8)
    else: return 0
def RegularHours(Hours):
    if Hours <= 8:
        return Hours
    elif Hours > 8:
        return abs((Hours-8)-Hours) 
    else: return 0
def OverTimePay(Hours,HourlyRate):
	if Hours > 8 and Hours <= 12:
		return (Hours - 8) * (HourlyRate * 1.5)
	elif Hours > 12:
	    return (4 * HourlyRate) * 1.5
	else: return 0
def OverTimeHours(Hours):
    if Hours > 8 and Hours <= 12:
        return (Hours - 8)
    elif Hours > 12:
        return 4
    else: return 0
def DoubleTimePay(Hours,HourlyRate):
        if Hours > 12:
            return (Hours - 12) * (HourlyRate * 2)
        else: return 0
def DoubleTimeHours(Hours):
        if Hours > 12:
            return (Hours - 12)
        else: return 0
        






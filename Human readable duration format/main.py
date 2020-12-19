def format_duration(seconds):
    year, seconds = divmod(seconds, 3600 * 24 * 365)
    day, seconds = divmod(seconds, 3600 * 24)
    hour, seconds = divmod(seconds, 3600)
    minute, seconds = divmod(seconds, 60)
    time = {
        "year": str(year),
        "day": str(day),
        "hour": str(hour),
        "minute": str(minute),
        "second": str(seconds)
    }
    result = []
    for index, data in enumerate(time):
        if time[data] != '0':
            strAppend = f"{time[data]} {data}"
            if int(time[data]) > 1:
                strAppend += 's'
            result.append(strAppend)
    if len(result) == 0:
        return "now"
    elif len(result) == 1:
        return result[0]
    elif len(result) == 2:
        return f"{result[0]} and {result[1]}"
    elif len(result) == 3:
        return f"{result[0]}, {result[1]} and {result[2]}"
    elif len(result) == 4:
        return f"{result[0]}, {result[1]}, {result[2]} and {result[3]}"
    elif len(result) == 5:
        return f"{result[0]}, {result[1]}, {result[2]}, {result[3]} and {result[4]}"


print(format_duration(62))

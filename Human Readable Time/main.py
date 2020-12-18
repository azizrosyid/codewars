def make_readable(seconds):
    hour = seconds // 3600
    seconds -= hour * 3600
    minute = seconds // 60
    seconds -= minute * 60
    second = seconds

    result = [str(hour), str(minute), str(second)]
    for i in range(len(result)):
        result[i] = "0" + result[i] if len(result[i]) == 1 else result[i]
    return ":".join(result)


make_readable(86399)

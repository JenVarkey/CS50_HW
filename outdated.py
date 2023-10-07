months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
month = 0
day = 0
year = 0
while True:
    date = input("Date: ")
    try:
        if date.find("/") > 0:
            month = int(date[0:date.find("/")])
            if month > 12 or month < 1:
                continue
            date = date[date.find("/") + 1:]
            day = int(date[0:date.find("/")])
            if day > 31 or day < 1:
                continue
            date = date[date.find("/") + 1:]
            year = int(date)
            print(f"{year}-{month:02d}-{day:02d}")
            break
        elif date.find(",") > 0:
            month = date[0:date.find(" ")]
            if not(month.isalpha()):
                continue
            count = 0
            for x in months:
                count+=1
                if x == month:
                    month = count
            month = int(month)
            if month > 12 or month < 1:
                continue
            date = date[date.find(" ") + 1:]
            day = int(date[0:date.find(",")])
            if day > 31 or day < 1:
                continue
            date = date[date.find(","):]
            year = date[date.find(",") + 2:]
            year = int(year)
            print(f"{year}-{month:02d}-{day:02d}")
            break
    except IndexError:
        continue
    except ValueError:
        continue
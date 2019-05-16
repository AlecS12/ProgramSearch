import random

# ========================== ADDRESS ==============================
def street_number():
    return random.choice([_ for _ in range(400)])

def street():
    return random.choice(['Pine', "Brook", "Foothill", "Broadway"])

def street_type():
    return random.choice(["Street", "Road", "Way", "Ave", "ST"])

def street_zip():
    return random.choice( range(10000, 100000))

def street_state():
    return random.choice(['CA','PA','IL'])

def address_info():
    return street_number(), street(), street_type(), street_zip(), street_state()

def street_ex1(st_num, st, st_type, st_zip, st_state):
    return [f"{st_num} {st} {st_type} {st_zip}", f"Num:{st_num} Street:{st}"]
def street_ex2(st_num, st, st_type, st_zip, st_state):
    return [f"{st_num}, {st} {st_type}, {st_state}", f"{st} {st_type} ({st_state})"]
def street_ex3(st_num, st, st_type, st_zip, st_state):
    return [f"{st_num}, {st} {st_type}, {st_state}, {st_zip}", f"{st_state},{st_zip}"]
def street_ex4(st_num, st, st_type, st_zip, st_state):
    zip_suffix = street_zip()
    return [f"{st_num}, {st} {st_type}, {st_state}, {st_zip}-{zip_suffix}", f"{st_state} {st_zip}"]

def street_ex(n_io):
    infos = [address_info() for _ in range(n_io)]
    ex_kind = random.choice([street_ex1, street_ex2, street_ex3, street_ex4])
    return [ex_kind(*info) for info in infos]

# ========================= NAMES ============================
def names_first():
    return random.choice(["Alex", "Sasha", "Taylor", "Jackie"])

def names_last():
    return random.choice(["Lennon", "Smith", "Einstein", "Schmidhuber"])

def names_middle():
    return random.choice([names_last(), ""])

def names_title():
    return random.choice(["Dr", "Sir", "Mr", "Mrs"])

def names_suffix():
    return random.choice([random.choice(["Esq", "I", "II", "Jr"]), ""])

def name_info():
    return names_first(), names_last(), names_middle(), names_title(), names_suffix()

def name_ex1(first, last, middle, title, suffix):
    return [f"{title} {first} {middle} {last} {suffix}", f"{first} : {last}"]
def name_ex2(first, last, middle, title, suffix):
    return [f"{first} {middle} {last}", f"Dr {last}"]
def name_ex3(first, last, middle, title, suffix):
    return [f"{title} {first} {middle} {last}", f"{last}, {first} ({title})"]
def name_ex4(first, last, middle, title, suffix):
    last_letter = last[0]
    first_letter = first[0]
    return [f"{title} {first} {middle} {last}", f"{last}, {first_letter})"]

def name_ex(n_io):
    infos = [name_info() for _ in range(n_io)]
    ex_kind = random.choice([name_ex1, name_ex2, name_ex3, name_ex4])
    return [ex_kind(*info) for info in infos]



###Phone number stuff
def threeD():
    return "".join(str(d) for d in random.choices(range(10), k=3))

def fourD():
    return "".join(str(d) for d in random.choices(range(10), k=4))

def phone_info():
    return threeD(), threeD(), fourD()

def phone_ex1(area, three, four):
    return [f"{area}{three}{four}", f"({area}) {three}-{four}"] 

def phone_ex2(area, three, four):
    return [f"({area}) {three} {four}", f"area code: {area}, num: {three}{four}"] 

#def phone_ex3(area, three, four):
#    return [f"({area}) {three} {four}", f"Area: {area}, Num: {three}{four}"] 



def phone_ex(n_io):
    tasks = []
    for fn in [phone_ex1, phone_ex2]:
        infos = [phone_info() for _ in range(n_io)]
        tasks.append( list(zip(*[fn(*info) for info in infos])))
    return tasks

#### date and time
def day():
    return random.choice( range(32) )

def weekday():
    return random.choice(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

def month():
    return random.choice(["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"] )

def year():
    return random.choice( range(1970, 2030) )

def hour():
    return random.choice(range(1,13))

def minute():
    return str(random.choice(range(7))) + str(random.choice(range(10)))


def date_info():
    return day(), weekday(), month(), year(), hour(), minute()

def date_ex1(day, weekday, month, year, hour, minute):
    return [f"{weekday}, {month} {day} {hour}:{minute}", f"{month} {day} at {hour} o'clock"]

def date_ex2(day, weekday, month, year, hour, minute):
    return [f"{weekday}, {month} {day}-{hour}:{minute}", f"{weekday} at {hour} o'clock"]

def date_ex3(day, weekday, month, year, hour, minute):
    return [f"{day} {month} {year}", f"year: {year}; month: {month}"]

def date_ex4(day, weekday, month, year, hour, minute):
    return [f"{day} {month} {year}", f"{month} {day} ({year})"]

def date_ex5(day, weekday, month, year, hour, minute):
    return [f"{day}-{month} ({weekday})", f"{weekday} ({month} {day})"]


def date_ex(n_io):
    tasks = []

    for fn in [date_ex1, date_ex2, date_ex3, date_ex4, date_ex5]:
        infos = [date_info() for _ in range(n_io)]
        tasks.append( list(zip(*[fn(*info) for info in infos])))

    return tasks


if __name__ == '__main__':
    print (street_ex(4))
    print (name_ex(4))
    # print (street_ex(4))
    tasks = date_ex(4)
    print(tasks)

    print(phone_ex(4))

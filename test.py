"""
-------------------- 1 - loop

hora = 09:00

1 - while:

hora.time() = 09:00

1 - for:

if 09:00 >= 12:00 and 09:00 < (12:00 + 01:00) ==> false
elif 09:00 >= (17:00+ 01:00) ==> false

lecture = 09:00AM - lecture 1 60min
lectures = [09:00AM lecture 1 60min]

hora  += 09:00 + 01:00

-------------------- 2 - loop

hora = 10:00

- while:

hora.time() = 10:00

- for:

if 10:00 >= 12:00 and 10:00 < (12:00 + 01:00) ==> false
elif 10:00 >= (17:00+ 01:00) ==> false

lecture = 10:00AM - lecture 1 45min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min]

hora  += 10:00 + 00:45

-------------------- 3 - loop

hora = 10:45

- while:

hora.time() = 10:45

- for:

if 10:45 >= 12:00 and 10:45 < (12:00 + 01:00) ==> false
elif 10:45 >= (17:00+ 01:00) ==> false

lecture = 10:45AM - lecture 3 30min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min]

hora  += 10:45 + 00:30

-------------------- 4 - loop

hora = 11:15

- while:

hora.time() = 11:15

- for:

if 11:15 >= 12:00 and 11:15 < (12:00 + 01:00) ==> false
elif 11:15 >= (17:00+ 01:00) ==> false

lecture = 11:15AM - lecture 4 45min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min]

hora  += 11:15 + 00:45

-------------------- 5 - loop

hora = 12:00

- while:

hora.time() = 12:00

- for:

if 12:00 >= 12:00 and 12:00 < (12:00 + 01:00) ==> true
lecure = 12:00PM Lunch
hora += 12:00 + 01:00
elif 13:00 >= (17:00+ 01:00) ==> false

lecture = 13:00PM - lecture 5 45min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min]

hora  += 13:00 + 00:45

-------------------- 6 - loop

hora = 13:45

- while:

hora.time() = 13:45

- for:

if 13:45 >= 12:00 and 13:45 < (12:00 + 01:00) ==> false

elif 13:45 >= (17:00+ 01:00) ==> false

lecture = 13:45PM - lecture 6 5min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min]

hora  += 13:45PM + 00:05

-------------------- 7 - loop

hora = 13:50

- while:

hora.time() = 13:50

- for:

if 13:50 >= 12:00 and 13:50 < (12:00 + 01:00) ==> false

elif 13:50 >= (17:00+ 01:00) ==> false

lecture = 13:50PM - lecture 7 60min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min,
            13:50PM - lecture 7 60min]

hora  += 13:50PM + 01:00

-------------------- 8 - loop

hora = 14:50

- while:

hora.time() = 14:50

- for:

if 14:50 >= 12:00 and 14:50 < (12:00 + 01:00) ==> false

elif 14:50 >= (17:00+ 01:00) ==> false

lecture = 14:50PM - lecture 8 45min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min,
            13:50PM - lecture 7 60min,
            14:50PM - lecture 8 45min]

hora  += 14:50PM + 00:45

-------------------- 9 - loop

hora = 15:35

- while:

hora.time() = 15:35

- for:

if 15:35 >= 12:00 and 15:35 < (12:00 + 01:00) ==> false

elif 15:35 >= (17:00+ 01:00) ==> false

lecture = 15:35PM - lecture 9 30min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min,
            13:50PM - lecture 7 60min,
            14:50PM - lecture 8 45min,
            15:35PM - lecture 9 30min]

hora  += 15:35PM + 00:30

-------------------- 10 - loop

hora = 16:05

- while:

hora.time() = 16:05

- for:

if 16:05 >= 12:00 and 16:05 < (12:00 + 01:00) ==> false

elif 16:05 >= (17:00+ 01:00) ==> false

lecture = 16:05PM - lecture 10 30min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min,
            13:50PM - lecture 7 60min,
            14:50PM - lecture 8 45min,
            15:35PM - lecture 9 30min,
            16:05PM - lecture 10 30min]

hora  += 16:05PM + 00:30

-------------------- 11 - loop

hora = 16:35

- while:

hora.time() = 16:35

- for:

if 16:35 >= 12:00 and 16:35 < (12:00 + 01:00) ==> false

elif 16:35 >= (17:00+ 01:00) ==> false

lecture = 16:35PM - lecture 11 45min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min,
            13:50PM - lecture 7 60min,
            14:50PM - lecture 8 45min,
            15:35PM - lecture 9 30min,
            16:05PM - lecture 10 30min,
            16:35PM - lecture 11 45min]

hora  += 16:35PM + 00:45

-------------------- 12 - loop

hora = 17:20

- while:

hora.time() = 17:20

- for:

if 17:20 >= 12:00 and 17:20 < (12:00 + 01:00) ==> false

elif 17:20 >= (17:00+ 01:00) ==> true
lecture = 17:00PM Network Event
hora = 17:00

-------------> parei aqui.

lecture = 16:35PM - lecture 11 45min
lectures = [09:00AM lecture 1 60min, 
            10:00AM - lecture 2 45min,
            10:45AM - lecture 3 30min,
            11:15AM - lecture 4 45min,
            12:00PM - Lunch,
            13:00PM - lecture 5 45min,
            13:45PM - lecture 6 5min,
            13:50PM - lecture 7 60min,
            14:50PM - lecture 8 45min,
            15:35PM - lecture 9 30min,
            16:05PM - lecture 10 30min,
            16:35PM - lecture 11 45min,
            17:00PM Network Event]

hora  += 16:35PM + 00:45


--------------------------------------

-------------------- 1 - loop

hora = 09:00

- for:

hora.time() = 09:00

- while 09:00 <= 17:00 :

if 09:00 >= 12:00 and 09:00 < (12:00 + 01:00) ==> false
elif 09:00 >= (17:00+ 01:00) ==> false

lecture = 09:00AM - lecture 1 60min
lectures = [09:00AM lecture 1 60min]

hora  += 09:00 + 01:00

-------------------- 2 - loop

hora = 10:00

- for:

hora.time() = 10:00

- while 10:00 <= 17:00 :

if 10:00 >= 12:00 and 10:00 < (12:00 + 01:00) ==> false
elif 10:00 >= (17:00+ 01:00) ==> false

lecture = 09:00AM - lecture 1 60min
lectures = [09:00AM lecture 1 60min]

hora  += 09:00 + 01:00

################----------------####################

-------------------- 1 - loop

hora = 09:00

- for:

hora.time() = 09:00

- while 09:00 <= 17:00 :

if 09:00 >= 12:00 and 09:00 < (12:00 + 01:00) ==> false
elif 09:00 >= (17:00+ 01:00) ==> false

lecture = 09:00AM - lecture 1 60min
lectures = [09:00AM lecture 1 60min]
del dados[0] --> lecture 1 60min

hora  += 09:00 + 01:00

-------------------- 2 - loop

hora = 10:00

- for:

hora.time() = 10:00

- while 10:00 <= 17:00 :

if 10:00 >= 12:00 and 10:00 < (12:00 + 01:00) ==> false
elif 10:00 >= (17:00+ 01:00) ==> false

lecture = 10:00AM - lecture 2 45min
lectures = [09:00AM lecture 1 60min,
            10:00AM - lecture 2 45min]
del dados[0] --> lecture 2 45min

hora  += 09:00 + 01:00

"""
from datetime import datetime, timedelta, time
import re

class Lecture():

    def __init__(self, data):
        self.data = data
        self.hr_inicio = datetime(2019, 1, 1, 9, 0, 0)
        self.hr_lunch = datetime(2019, 1, 1, 12, 0, 0)
        self.hr_network = datetime(2019, 1, 1, 17, 0, 0)

    def set_timing_lectures(self):
        """
        List the lectures with their timing.
        """

        lectures = self.data['data']
        lista = []
        for lecture in lectures:
            timing = ''.join(el for el in lecture if el.isdigit())
            if re.search('min', lecture):
                dict_ = {
                    'lecture': lecture,
                    'timing': timing
                }
            elif re.search('lightning', lecture):
                dict_ = {
                    'lecture': lecture,
                    'timing': '5'
                }
            lista.append(dict_)
       
        return lista

    def set_tracks(self):
        """
        Make a one track with all lecture times ordered.
        """
        dados = self.set_timing_lectures()
        hr_atual = self.hr_inicio.time().strftime('%H:%M')
        hora = self.hr_inicio

        lectures = []
        cronograma = {
                "data": []
            }
        track = 0
        
        for dado in dados:
            lunch = f"{self.set_hour(self.hr_lunch.time())} Lunch"
            happy_hour = f"{self.set_hour(self.hr_network.time())} Networking Event"
            if hora.time() >= self.hr_lunch.time() and hora.time() < (self.hr_lunch + timedelta(hours=1)).time():
                lectures.append(lunch)
                hora += timedelta(hours=1)
            elif hora.time() >= (self.hr_network + timedelta(hours=1)).time():
                lectures.append(happy_hour)
                hora = self.hr_network
            lecture = f"{self.set_hour(hora.time())} {dado['lecture']}"
            lectures.append(lecture)
            hora += timedelta(minutes=int(dado['timing']))
            del dados[0]
        track += 1

        tracks = {
            "title": f"track {track}",
            "data": lectures
        }
        cronograma['data'].append(tracks)            

        return cronograma
    
    def set_hour(self, hour):
        """
        Change the hour format from 24h to 12h.
        """
        formated = hour.strftime('%H:%M')
        am_pm = "AM" if formated < '12:00' else "PM"
        hr = f"{formated}{am_pm}"

        return hr
        
    def make_cronogram(self, lectures, track):
        
        cronograma = {
                "data": []
            }

        tracks = {
                "title": f"track {track}",
                "data": lectures
            }

        cronograma['data'].append(tracks)

        print(cronograma)
        return cronograma
        


if __name__ == "__main__":
    hr_inicio = datetime(2019, 1, 1, 9, 0, 0)
    data = {
        "data":[
        "Writing Fast Tests Against Enterprise Rails 60min",
        "Overdoing it in Python 45min",
        "Lua for the Masses 30min",
        "Ruby Errors from Mismatched Gem Versions 45min",
        "Common Ruby Errors 45min",
        "Rails for Python Developers lightning",
        "Communicating Over Distance 60min",
        "Accounting-Driven Development 45min",
        "Woah 30min",
        "Sit Down and Write 30min",
        "Pair Programming vs Noise 45min",
        "Rails Magic 60min",
        "Ruby on Rails: Why We Should Move On 60min",
        "Clojure Ate Scala (on my project) 45min",
        "Programming in the Boondocks of Seattle 30min",
        "Ruby vs. Clojure for Back-End Development 30min",
        "Ruby on Rails Legacy App Maintenance 60min",
        "A World Without HackerNews 30min",
        "User Interface CSS in Rails Apps 30min"
        ]
    }
    l = Lecture(data)
    # l.get_timing_lectures()
    l.set_tracks()
    # l.set_hour(hr_inicio.time())
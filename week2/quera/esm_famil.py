import csv

all_words = {}
sections = ['esm', 'famil', 'keshvar', 'rang', 'ashia', 'ghaza']
participants = []
for i in sections:
    all_words[i] = []


def remove_space(space):
    return space.replace(' ', '')


def ready_up(csv_data):
    csv_read = csv.reader(csv_data)
    for row in csv_read:
        all_words['esm'].append(remove_space(row[0]))
        all_words['famil'].append(remove_space(row[1]))
        all_words['keshvar'].append(remove_space(row[2]))
        all_words['rang'].append(remove_space(row[3]))
        all_words['ashia'].append(remove_space(row[4]))
        all_words['ghaza'].append(remove_space(row[5]))


ready_up(csv_data=open("esm_famil_data.csv"))


def add_participant(participant, answers):
    participants.append({'name': participant, 'answers': answers})


add_participant(participant='salib',
                answers={'esm': 'بردیا', 'famil': 'بابایی', 'keshvar': 'باربادوس',
                         'rang': 'بنفش', 'ashia': 'بمب', 'ghaza': 'باقالی پلو'})
add_participant(participant='kianoush',
                answers={'esm': 'بهرام', 'famil': 'بهرامی', 'keshvar': 'برزیل',
                         'rang': 'بلوطی', 'ashia': 'بیل', 'ghaza': 'به   پلو'})
add_participant(participant='sajjad',
                answers={'esm': 'بابک', 'famil': 'بهشتی', 'keshvar': 'باهاما',
                         'rang': 'بژ', 'ashia': '        ', 'ghaza': 'برنج خورشت'})
add_participant(participant='farhad',
                answers={'esm': 'بهرام', 'famil': 'براتی', 'keshvar': 'بببببب',
                         'rang': 'بژ', 'ashia': 'بیل', 'ghaza': 'باقلوا'})


def calculate_all():
    scores = {}
    for participant in participants:
        name = participant['name']
        answers = participant['answers']

        scores[name] = 0
        for elm in sections:
            answer = remove_space(answers.get(elm))
            if not answer or answer not in all_words[elm]:
                score = 0

            else:
                same_answer = False
                all_answered = True
                for another_name in participants:
                    if name == another_name['name']:
                        continue
                    another_answer = remove_space(another_name['answers'][elm])
                    if another_answer == answer:
                        same_answer = True
                    if not remove_space(another_answer):
                        all_answered = False

                if all_answered and same_answer:
                    score = 5
                if all_answered and not same_answer:
                    score = 10
                if not all_answered and same_answer:
                    score = 10
                if not all_answered and not same_answer:
                    score = 15
            scores[name] += score

    return scores


print(calculate_all())


def stack_of_q_loader():
    import time
    import requests
    import json
    from pprint import pprint

    def stack_of_q_counter(two_days_ago, page, two_days_questions):

        response = requests.get('https://api.stackexchange.com/2.2/questions?page=' +
                                str(page) +
                                '&pagesize=50&fromdate=' +
                                str(round(two_days_ago)) +
                                '&order=desc&sort=creation&tagged=python&site=stackoverflow')

        q_list = response.json()['items']

        if q_list == []:
            return two_days_questions

        for question in q_list:
            two_days_questions.append(question)
        print(len(two_days_questions))
        print(page)
        page += 1

        return stack_of_q_counter(two_days_ago, page, two_days_questions)

    two_days_ago = time.time() - 60 * 60 * 48
    page = 53
    two_days_questions = []

    stack_of_q_counter(two_days_ago, page, two_days_questions)

    print(len(two_days_questions))
    # pprint(q_list)
    return two_days_questions

stack_of_q_loader()


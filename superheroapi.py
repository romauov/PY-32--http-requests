def smartest_hero(heroes_list):

    import requests
    import json
    from pprint import pprint

    max_intelligence = 0
    smart_hero = None

    for hero in heroes_list:

        url_for_request = 'https://www.superheroapi.com/api.php/2619421814940190/search/' + hero

        response = requests.get('https://www.superheroapi.com/api.php/2619421814940190/search/' + hero)

        resp_json = response.json()

        if resp_json['response'] == 'success':
            for result in resp_json['results']:

                intelligence = int(result['powerstats']['intelligence'])

                if intelligence > max_intelligence:
                    max_intelligence = intelligence
                    smart_hero = result['name'] + ', id ' + result['id']

        else:
            print(f'Герой {hero} отсутствует в нашей базе данных')
    print(f'Наибольшим интеллектом ({max_intelligence}) среди {len(heroes_list)} героев, представленных в списке, обладает {smart_hero}.')


    return smart_hero

smartest_hero(['Captain America', 'Hulk', 'Thanos', 'Harley Quinn', 'Piton Vitaliy'])




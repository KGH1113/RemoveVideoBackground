import requests

frame_cnt = int(input("Frame count: "))

for cnt in range(205, frame_cnt):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('/Users/gang-guhyeon1/Desktop/Python/Frame{0}.jpg'.format(cnt), 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'RSizW12tAJjZEMhGi4HkeJ8X'},
    )
    if response.status_code == requests.codes.ok:
        with open('Frame{0} - erased_background.png'.format(cnt), 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
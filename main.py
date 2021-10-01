from Run import Run

boat = []
start_coast = ['wolf', 'goat', 'cabbage']
finish_coast = []
move_yn = 'start'

data = open('data.txt', 'r')

for line in data:
    try:
        objects = line.split()

        if len(objects) >= 3:
            raise Exception(f'Too much objects')

        elif len(objects) == 0:
            raise Exception(f'Objects not found')

        else:
            action = objects[0]
            if len(objects) == 2:
                beast = objects[1]
            else:
                beast = None
            r = Run(boat, start_coast, finish_coast, move_yn)
            move_yn = r.run(action, beast)

    except Exception as e:
        print(f'#ERROR: In {line} : {e}')

if finish_coast == [
    'wolf', 'cabbage', 'goat'] or finish_coast == [
    'cabbage', 'wolf', 'goat'] or finish_coast == [
    'wolf', 'goat', 'cabbage'] or finish_coast == [
    'goat', 'cabbage', 'wolf'] or finish_coast == [
    'cabbage', 'goat', 'wolf'] or finish_coast == [
    'goat', 'wolf', 'cabbage']:
    print('\nЗадача выполнена верно, все перебрались на другой берег!')
else:
    print('Задача выполнена неверно!')
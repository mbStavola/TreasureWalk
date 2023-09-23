import os, random, argparse, string

user_path = os.path.expanduser('~')
root_name = f"{user_path}/hunt"
flag_file_extension = '.txt'

directions = ['up', 'down', 'left', 'right']

letters = string.ascii_letters

def create_path_component(depth):
    direction_index = random.randint(0, len(directions) - 1)
    direction = directions[direction_index]
    return f"level-{depth}-{direction}"

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--max-depth", help="how deep down the directories can go", default=3)
argParser.add_argument("-f", "--max-fakes", help="how many fake directories we will create total", default=3)
argParser.add_argument("-r", "--random-flag-name", help="makes the flag file name random", action='store_true')

args = argParser.parse_args()

depth = random.randint(0, int(args.max_depth))
max_fakes = int(args.max_fakes)

flag_file_name = "".join(random.sample(letters, 5)) if args.random_flag_name else 'flag'
flag_file_name = f"{flag_file_name}.txt"

fake_paths = []
flag_path = [root_name]

while depth > 0:
    for _ in range(random.randint(0, max_fakes)):
        fake_path = flag_path.copy()
        path_component = create_path_component(depth)
        fake_path.append(path_component)
        
        fake_paths.append(fake_path)

        for i in range(random.randint(0, min(depth, 3))):
            new_depth = depth - 1
            faker_path = fake_path.copy()
            path_component = create_path_component(new_depth)
            faker_path.append(path_component)
            fake_paths.append(faker_path)
            
        max_fakes -= 1

    path_component = create_path_component(depth)
    flag_path.append(path_component)

    depth -= 1

flag_path = "/".join(flag_path)
os.makedirs(flag_path, exist_ok=True)

file_contents = "".join(random.sample(letters, 16))

file = open(f"{flag_path}/{flag_file_name}", "a")
file.write(file_contents)
file.close()

for fake_path in fake_paths:
    fake_path = "/".join(fake_path)
    os.makedirs(fake_path, exist_ok=True)

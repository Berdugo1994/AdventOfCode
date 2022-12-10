import os
import requests
from dotenv import load_dotenv
load_dotenv()

config = {
    "session_id": os.environ.get("MY_SESSION_ID")
}


def check_if_file_exists(input_file):
    if os.path.isfile(input_file):
        return True
    return False



def import_input_file(riddle_file: str, year: str = "2022"):
    riddle_num = str(riddle_file.split("/")[-1][3:-3])
    input_file = f"../inputs/{riddle_num}.txt"
    if check_if_file_exists(input_file):
        print(f"Input file for riddle {riddle_num} already exists...")
        return True
    url = f"https://adventofcode.com/{year}/day/{riddle_num}/input"
    r = requests.get(url, cookies={'session': config['session_id']})
    if r.status_code != 200:
        print("request for input file failed.")
        return False
    os.makedirs(os.path.dirname(input_file), exist_ok=True)
    f = open(input_file, "a")
    f.write(r.text)
    f.close()
    print(f"Input file for riddle {riddle_num} created successfully!")
    return True

if __name__=="__main__":
    import_input_file("sa")


def read_input(riddle_file: str):
    riddle_num = str(riddle_file.split("/")[-1][3:-3])
    f = open(riddle_file[:37]+"inputs/"+riddle_num+".txt", "r")
    file_as_str = f.read()
    f.close()
    return file_as_str

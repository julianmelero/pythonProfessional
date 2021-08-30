from typing import Dict, List,Tuple

def make_repetear_of(n):
    def repeter(string):
        return string * n
    return repeter




def run():
    repeat_5 = make_repetear_of(5)
    print(repeat_5("Hello"))



if __name__ == "__main__":
    run()
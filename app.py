import time
from typing import List, Union

import chess
from dotenv import load_dotenv
from os import getenv
import pandas as pd
from pandas.core.frame import DataFrame
from Oracle import Oracle
from mixins import get_error_message
from Gui import Gui
from threading import Thread
from random import choice

load_dotenv()
data_1: DataFrame = pd.read_csv(getenv('MATCHES_FILE_1'), usecols=['Moves'])
data_2: DataFrame = pd.read_csv(getenv('MATCHES_FILE_2'), usecols=['Moves'])

data_3 = []
for data in data_1['Moves']:
    data_3.append(data)

for data in data_2['Moves']:
    data_3.append(data)

data_3 = pd.DataFrame(data_3, columns=['Moves'])

main_oracle: Oracle = Oracle(matches=data_3['Moves'])


gui: Gui = Gui()
Thread(target=gui.show).start()
context: List[str] = []

while True:
    move: str = input('Enter Move: ')

    try:
        gui.update(move)
        context.append(move)
    except:
        print('Invalid Move')
        print('Try Again...')
        continue

    prediction: Union[str, None] = main_oracle.predict(context=context)

    if prediction is None:
        prediction: Union[str, None] = main_oracle.get_result_force(move, gui)
    else:
        gui.update(prediction)

    if prediction is None:
        print(get_error_message())
        exit()

    print(f'My Move: {prediction}')


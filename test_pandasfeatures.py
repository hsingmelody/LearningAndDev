"""Start Sequence."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


randrating = np.random.randint(1, 11, size=(4, 3))
randrating

TVseries = pd.DataFrame(randrating)
TVseries.rename(columns={0: 'Game of Thrones',
                         1: 'The Witcher',
                         2: 'Solar Opposites'},
                index={0: 'Winter',
                       1: 'Spring',
                       2: 'Summer',
                       3: 'Fall'},
                inplace=True)
TVseries

result = TVseries.plot(kind='bar',
                       title='TV Popularity',
                       figsize=(8, 3),
                       colormap='PuRd')

result.set_facecolor((0.18, 0.20, 0.31, 1.0))
leg = result.legend(loc='best', framealpha=1, markerscale=50,
                    borderpad=1)
for text in leg.get_texts():
    plt.setp(text, color='w', fontname='Century Gothic', weight='light',
             style='italic', size=9)

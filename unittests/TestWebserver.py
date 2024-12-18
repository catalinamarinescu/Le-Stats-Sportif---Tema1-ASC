import unittest
from app import DataIngestor

class TestStringMethods(unittest.TestCase):
    def test_states_mean(self):
        data = {"question": "Percent of adults who achieve \
                at least 150 minutes a week of moderate-intensity \
                aerobic physical activity or 75 minutes a week of\
                vigorous-intensity aerobic activity (or an equivalent combination)"}
        assert DataIngestor.states_mean(data) == {"District of Columbia": 30.746875, 
                "Missouri": 32.76268656716418, "Arkansas": 32.99516129032258, "Kentucky": 33.071641791044776, 
                "Vermont": 33.118181818181824, "Louisiana": 33.179310344827584, "Ohio": 33.25753424657535, 
                "South Carolina": 33.25909090909091, "Virgin Islands": 33.296875, "Illinois": 33.521875, 
                "Indiana": 33.58701298701298, "Michigan": 33.73734939759036, "West Virginia": 33.861111111111114, 
                "Iowa": 33.96455696202531, "Washington": 33.96842105263158, "Hawaii": 34.0046875, "Kansas": 34.05625, 
                "Oklahoma": 34.05833333333333, "Tennessee": 34.10945945945946, "Oregon": 34.1421875, "Alabama": 34.1551724137931, 
                "Wisconsin": 34.15542168674699, "Utah": 34.19508196721311, "Florida": 34.27333333333333, 
                "Georgia": 34.30126582278481, "Mississippi": 34.315625, "Maine": 34.31612903225806, 
                "Texas": 34.37692307692308, "North Carolina": 34.377631578947366, "Virginia": 34.45882352941176, 
                "Guam": 34.485454545454544, "Maryland": 34.528395061728396, "Pennsylvania": 34.54354838709677, 
                "Massachusetts": 34.6203125, "Delaware": 34.673846153846156, "Colorado": 34.78536585365854, 
                "New Hampshire": 34.84415584415584, "New York": 34.86, "North Dakota": 34.891666666666666, 
                "National": 35.0859375, "Rhode Island": 35.17878787878788, "Idaho": 35.19090909090909, 
                "South Dakota": 35.19565217391305, "Arizona": 35.4046875, "Wyoming": 35.5169014084507, 
                "Minnesota": 35.545762711864406, "Nebraska": 35.691428571428574, "California": 35.72459016393442, 
                "Connecticut": 35.754285714285714, "New Mexico": 35.86349206349207, "Alaska": 35.90277777777778, 
                "New Jersey": 36.080597014925374, "Montana": 36.17826086956522, "Nevada": 36.358333333333334, 
                "Puerto Rico": 36.986363636363635}

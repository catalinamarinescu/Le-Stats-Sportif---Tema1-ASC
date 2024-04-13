import pandas

class DataIngestor:
    def __init__(self, csv_path: str):

        self.questions_best_is_min = [
            'Percent of adults aged 18 years and older who have an overweight classification',
            'Percent of adults aged 18 years and older who have obesity',
            'Percent of adults who engage in no leisure-time physical activity',
            'Percent of adults who report consuming fruit less than one time daily',
            'Percent of adults who report consuming vegetables less than one time daily'
        ]

        self.questions_best_is_max = [
            'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity and engage in muscle-strengthening activities on 2 or more days a week',
            'Percent of adults who achieve at least 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who engage in muscle-strengthening activities on 2 or more days a week',
        ]

        self.csv_path = csv_path
        self.data_set = pandas.read_csv(self.csv_path)

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       question - the question received from input
    def helper_for_states(self, question):
        filtered_data = self.data_set[(self.data_set['Question'] == question)]
        result = self.helper_for_state(filtered_data)
        return result

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       data - a filtered data set with only the question received from input
    def helper_for_state(self, data):
        filtered_data = data[(data['YearStart'] >= 2011)]
        filtered_data1 = filtered_data[(filtered_data['YearEnd'] <= 2022)]
        filtered_data1['Data_Value'] = pandas.to_numeric(filtered_data1['Data_Value'],
                                                        errors='coerce')
        state_mean_data = filtered_data1.groupby('LocationDesc')['Data_Value'].mean()
        states_mean_data_sorted = state_mean_data.sort_values(ascending = True)
        result = states_mean_data_sorted.to_dict()
        return result

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       data - json with the question received from input
    def states_mean(self, data):
        question = data['question']
        result = self.helper_for_states(question)
        return result

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       data - json with the question and the state received from input
    def state_mean(self, data):
        question = data['question']
        state = data['state']

        filtered_data = self.data_set.loc[(self.data_set['Question'] == question)]
        if state in filtered_data['LocationDesc'].values:
            filtered_data1 = filtered_data[(filtered_data['LocationDesc'] == state)]
            result = self.helper_for_state(filtered_data1)
            return result
        # Empty dictionary in case the state specified doesn't exist for the question
        return {}

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       data - json with the question received from input
    def best5(self, data):
        question = data['question']
        result = self.states_mean(data)
        list_result = list(result.items())

        if question in self.questions_best_is_min:
            best_5 = dict(list_result[:5])
        elif question in self.questions_best_is_max:
            best_5 = dict(reversed(list_result[-5:]))
        return best_5

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       data - json with the question received from input
    def worst5(self, data):
        question = data['question']
        result = self.states_mean(data)
        list_result = list(result.items())

        if question in self.questions_best_is_max:
            worst_5 = dict(list_result[:5])
        elif question in self.questions_best_is_min:
            worst_5 = dict(reversed(list_result[-5:]))
        return worst_5

    # Returns a dictionary formed with the state as key and the mean value
    # as value
    #       data - json with the question and the state received from input
    def global_mean(self, data):
        question = data['question']
        filtered_data = self.data_set.loc[(self.data_set['Question'] == question)]
        global_mean_data = pandas.to_numeric(filtered_data['Data_Value']).mean()
        result = {}
        result['global_mean'] = global_mean_data
        return result

    # Returns a dictionary formed with the state as key and the difference
    # between global_mean and state_mean value
    #       data - json with the question received from input
    def diff_from_mean(self, data):
        # New data with the question and the state that will e used
        # as argument to the state_mean function
        new_data = {}
        new_data['question'] = data['question']
        # List of all the states
        states = self.data_set['LocationDesc'].unique()
        glb_mean = self.global_mean(data)
        result = {}
        for state in states:
            diff = 0
            new_data['state'] = state
            st_mean = self.state_mean(new_data)
            if st_mean:
                diff = glb_mean['global_mean'] - st_mean[state]
                result[state] = diff

            del new_data['state']
        return result

    # Returns a dictionary formed with the state as key and the difference
    # between global_mean and state_mean value
    #       data - json with the question and the state received from input
    def state_diff_from_mean(self, data):
        new_data = {}
        new_data['question'] = data['question']
        glb_mean = self.global_mean(new_data)
        st_mean = self.state_mean(data)
        result = {}
        diff = glb_mean['global_mean'] - st_mean[data['state']]
        result[data['state']] = diff
        return result

    # Returns a dictionary formed with the state as key and the difference
    # between global_mean and state_mean value
    #       data - json with the question and the state received from input
    def state_mean_by_category(self, data):
        question = data['question']
        state = data['state']
        filtered_data = self.data_set.loc[(self.data_set['Question'] == question)]
        if state in filtered_data['LocationDesc'].values:
            filtered_data1 = filtered_data[(filtered_data['LocationDesc'] == state)]
            filtered_data1['Data_Value'] = pandas.to_numeric(filtered_data1['Data_Value'],
                                                            errors='coerce')
            state_mean_data_category = filtered_data1.groupby(['StratificationCategory1',
                        'Stratification1'])['Data_Value'].mean()
            result = {}
            state_mean_data_category_dict = {}
            # Makes the tuple a string so it can be used as key
            for index, mean_value in state_mean_data_category.items():
                key_tuple = str(index)
                state_mean_data_category_dict[key_tuple] = mean_value
            result[state] = state_mean_data_category_dict
            return result
        return {}

    # Returns a dictionary formed with the state as key and the difference
    # between global_mean and state_mean value
    #       data - json with the question and the state received from input
    def mean_by_category(self, data):
        question = data['question']
        filtered_data = self.data_set.loc[(self.data_set['Question'] == question)]
        filtered_data['Data_Value'] = pandas.to_numeric(filtered_data['Data_Value'],
                                                        errors='coerce')
        states_mean_data = filtered_data.groupby(['LocationDesc', 'StratificationCategory1',
                                                'Stratification1'])['Data_Value'].mean()
        result = {}
        # Makes the tuple a string so it can be used as key
        for index, mean_value in states_mean_data.items():
            key = str(index)
            result[key] = mean_value
        return result

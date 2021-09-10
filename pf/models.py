import joblib
import pandas as pd
import numpy as np


class FoodPredictor:
    def __init__(self):
        self.model, self.encoders, self.x_cols = joblib.load('media/model.joblib')

        # parse out encoders
        for i in range(len(self.encoders)):
            if self.encoders[i][0] == 'y_encoder':
                self.y_encoder = self.encoders[i][1]

            if self.encoders[i][0] == 'dow':
                self.dow_encoder = self.encoders[i][1]
                self.list_dow = ['Mon', 'Tues', 'Weds', 'Thurs', 'Fri', 'Sat', 'Sun']  # 0 is mon

    @staticmethod
    def day2scale(datestamp):
        # currently hardcoded: will need to update if SQL db is updated with more recent data preferably
        start_day = pd.Timestamp('2014-02-24 00:00:00')
        n_days = pd.Timedelta('2533 days 00:00:00')
        return (datestamp - start_day) / n_days

    def input_model(self, datestamp):
        # assumes one input, reshaped to fit model
        # only accepts dow input for now
        date_scale = self.day2scale(datestamp)
        try:
            dow = datestamp.dayofweek
            inputarray = self.dow_encoder.transform([dow])
        except Exception as err:
            print('error - {}'.format(err))

        inputarray = np.append(inputarray, date_scale)
        return inputarray.reshape(1, -1)

    def predict_past_week(self):
        # predict last 7 days
        inputarr2 = self.input_model(pd.Timestamp.today())
        list_timestamps = [pd.Timestamp.today().strftime('%a, %b %d, %Y')]
        for i in range(1, 7):
            timestamp = pd.Timestamp.today() - pd.Timedelta(days=i)
            list_timestamps.append(timestamp.strftime('%a, %b %d, %Y'))
            inputarr = self.input_model(timestamp)
            inputarr2 = np.vstack([inputarr2, inputarr])
        predicted = self.model.predict(inputarr2)
        result = self.y_encoder.inverse_transform(predicted)

        today = {'todays_date': list_timestamps[0], 'todays_result': result[0]}
        past_week = dict(zip(list_timestamps[1:], result[1:]))

        return today, past_week

    def predict_today(self):
        # grab today's result
        datestamp = pd.Timestamp.today() + pd.Timedelta(days=0)
        inputarr = self.input_model(datestamp)
        predicted = self.model.predict(inputarr)
        result = self.y_encoder.inverse_transform(predicted)

        return {'todays_date': datestamp.strftime('%a, %b %d, %Y'), 'todays_result': result}

    # @app.route('/predict', methods=['POST'])
    # def predict():
    #     # pre
    #     json_ = request.json
    #     query_df = pd.DataFrame(json_)
    #     query = pd.get_dummies(query_df)
    #     for col in model_columns:
    #          if col not in query.columns:
    #               query[col] = 0
    #               prediction = clf.predict(query)
    #     return jsonify({'prediction': list(prediction)})

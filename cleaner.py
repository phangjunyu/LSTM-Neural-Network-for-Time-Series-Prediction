import pandas as pd

def main_func():
    df = pd.read_csv('data/test.csv')

    df.Category = df['Category'].replace(["Work", "Entertainment", "Miscellaneous", "Social Networking"], [0,1,2,3])
    df.Eyes = df['Eyes'].astype(int)

    # for i in ['Category', 'Gaze', 'Emotion', 'Eyes']:
    #     # df[i] = df[i] + 1
    #     df = pd.concat([df,pd.get_dummies(df[i])],axis=1)

    df.Keystrokes = df.Keystrokes/(max(df.Keystrokes) - min(df.Keystrokes))

    df.to_csv('data/testedited.csv')

if __name__ == "__main__":
    main_func()

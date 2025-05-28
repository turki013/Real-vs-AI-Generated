import pandas as pd   
import matplotlib.pyplot as plt  
import config as cfg                 


def data():
  """ Reads the dataset from a CSV file named 'tweets_dataset.csv'.

    This function attempts to load the tweet dataset using pandas.
    If the file is not found or any error occurs, it prints a friendly error message.
    It also prints the first 10 rows for a quick preview and returns the full DataFrame
    for further analysis and visualization.

    Returns:
        pd.DataFrame: A pandas DataFrame containing the tweet dataset with columns:
                      'name', 'tweet', and 'is_real'.

    Raises:
        FileNotFoundError: If the CSV file is not found in the project directory.
        Exception: If any other unexpected error occurs during file reading."""
  try:  
     df = pd.read_csv("assets/Datasets/tweets_dataset.csv")
     return df
  except FileNotFoundError:
      print("Sorry file not found")
  except Exception as e:
      print(f"Error: something went wrong {e}") 
  finally:
      print("Done")    

def setup_save_on_key(filename):
    def on_key(event):
      if event.key == 'S':
          plt.savefig(filename)
          print(f"📸 Snapshot saved! File: {filename}")
    plt.gcf().canvas.mpl_connect('key_press_event', on_key)
    
                
def bar_chart(df):
   """Displays a horizontal stacked bar chart of real vs AI-generated tweets for each celebrity.

    This function uses the pandas groupby method to count how many tweets are real (`True`)
    or AI-generated (`False`) per celebrity. It then uses matplotlib to display
    a horizontal bar chart where each bar is stacked to compare the two categories visually.

    Args:
        df (pd.DataFrame): A DataFrame containing the tweet dataset, with at least two columns:
                           'name' (celebrity name) and 'is_real' (boolean).

    Output:
        Saves the chart as 'tweets_bar.png' and displays it in a separate window."""
         
   grouped = df.groupby(["name","is_real"]).size().unstack(fill_value =0)
   colors = []
   for col in grouped.columns:
       if col == True:
           colors.append(cfg.color_Real)
       else:
           colors.append(cfg.color_Ai)   
   ax = grouped.plot(kind='bar' , stacked=True , color = colors)
   ax.legend(["AI-Generated" , "Real"], title="Tweet Type")
   plt.title(cfg.title)
   plt.xlabel("Celebrity" , fontsize=14)
   plt.ylabel("Tweet Count " , fontsize=14)
   plt.xticks(rotation=45)
   plt.tight_layout()
   setup_save_on_key(cfg.filename_Bar)
   plt.show()
   
def scatter_chart(df):
    """ Displays a scatter plot of all tweets colored by whether they're real or AI-generated.

    Each point in the chart represents a single tweet.
    The X-axis shows the celebrity name, and the Y-axis shows whether the tweet is real (1)
    or AI-generated (0). The color of each point is determined by the 'is_real' value:
    typically blue for AI-generated and red for real tweets using a 'coolwarm' color map.

    Args:
        df (pd.DataFrame): A DataFrame with 'name' and 'is_real' columns.

    Output:
        Saves the chart as 'tweets_scatter.png' and displays it in a separate window."""
    colors = []
    for col in df["is_real"]:
        if col == True:
            colors.append(cfg.color_Real)
        else:
            colors.append(cfg.color_Ai)
                
    plt.figure(figsize= cfg.figs_size)
    name = df["name"].tolist()
    is_real = df["is_real"].tolist()
    plt.title(cfg.title)
    plt.xlabel("Celebrity", fontsize=14)
    plt.ylabel("Tweet Count" , fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.yticks([0, 1], ['AI-Generated', 'Real'])
    plt.scatter(name , is_real ,c=colors)
    setup_save_on_key(cfg.filename_scatter)
    plt.show()
       
def stem_chart(df):
    """Displays a stem plot of tweets to visualize the real vs AI-generated status.

    A stem plot shows vertical lines from a baseline (y=0 or y=1) to each data point.
    This is useful for showing discrete data in a visual and minimal way.
    The X-axis represents the celebrity name, and the Y-axis represents whether the tweet is real.

    Args:
        df (pd.DataFrame): The tweet dataset containing 'name' and 'is_real' columns.

    Output:
        Saves the chart as 'tweets_stem.png' and displays it in a separate window."""
    
               
    plt.figure(figsize= cfg.figs_size)
    name = df["name"].tolist()
    is_real = df["is_real"].tolist()
    plt.title(cfg.title) 
    plt.xlabel("Celebrity", fontsize=14)
    plt.ylabel("Tweet Count" , fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.yticks([0, 1], ['AI-Generated', 'Real'])
    plt.stem(name , is_real)
    setup_save_on_key(cfg.filename_stem)
    plt.show()  
   
   
if __name__ == "__main__":
    df = data()
    while True:
       print("Welcome to visual app ")
       print("1.Bar chart")
       print("2. Scatter chart")
       print("3. stem chart")
       print("4. Exit")
       choice = input("Enter the number :").strip()
       if choice == "1":
           bar_chart(df) 
       elif choice == "2":
           scatter_chart(df)
       elif choice == "3":
           stem_chart(df)
       elif choice == "4":
           print("Exiting the app...")
           break
       else:
           print("invalid number please try again")              
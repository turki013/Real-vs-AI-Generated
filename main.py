import pandas as pd   
import matplotlib.pyplot as plt                   


def data():
  try:  
     df = pd.read_csv("tweets_dataset.csv")
     df.head(10)
     return df
  except FileNotFoundError:
      print("Sorry file not found")
  except Exception as e:
      print(f"Error: something went wrong {e}") 
  finally:
      print("Done")    
    
def bar_chart(df):
   plt.title("Celebrity Tweets Dataset (Real vs AI-Generated) ")
   plt.xlabel("name" , fontsize=14)
   plt.ylabel("is  real" , fontsize=14)
   name = df["name"].tolist()
   is_real = df["is_real"].tolist()
   plt.bar(name , is_real)
   plt.savefig("tweets_bar.png")
   plt.show()
   
def scatter_chart(df):
    plt.title("Celebrity Tweets Dataset (Real vs AI-Generated)")
    plt.xlabel("name", fontsize=14)
    plt.ylabel("is real" , fontsize=14)
    name = df["name"].tolist()
    is_real = df["is_real"].tolist()
    plt.scatter(name , is_real)
    plt.savefig("tweets_scatter.png")
    plt.show()
       
def stem_chart(df):
    plt.title("Celebrity Tweets Dataset (Real vs AI-Generated)") 
    plt.xlabel("name", fontsize=14)
    plt.ylabel("is real" , fontsize=14)
    name = df["name"].tolist()
    is_real = df["is_real"].tolist()
    plt.stem(name , is_real)
    plt.savefig("tweets_stem.png")
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
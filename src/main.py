from langchain_chain import rag_chain
import pandas as pd

def main():
    print("Welcome to the College AI Application")

    # Load the dataset
    df = pd.read_csv('../data/college_test_data.csv')
    
    while True:
        print("\nOptions:")
        print("1. Search for a university by name")
        print("2. Filter universities by country")
        print("3. Show top universities by world rank")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            search_term = input("Enter university name to search: ")
            response = rag_chain.run(search_term)
            print(response)
        
        elif choice == '2':
            country = input("Enter country to filter by: ")
            filtered_df = df[df['country'] == country].sort_values(by='world_rank')
            print(f"Top Universities in {country}:")
            print(filtered_df[['institution', 'world_rank']].head(10))  # Display top 10
        
        elif choice == '3':
            sorted_df = df.sort_values(by='world_rank')
            print("Top Universities by World Rank:")
            print(sorted_df[['institution', 'world_rank']].head(10))  # Display top 10
        
        elif choice == '4':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

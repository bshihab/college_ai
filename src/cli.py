from langchain_chain import rag_chain

def main():
    while True:
        query = input("Enter university name (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        response = rag_chain.run(query)
        print(response)

if __name__ == "__main__":
    main()

# College Data Management and Search System

This project provides a comprehensive system for managing and searching college data. It includes functionalities to fetch college data from a public API, upload and update this data in Firestore, generate embeddings for semantic search, and perform advanced queries using a language model.

## Features

-   **Fetch College Data**: Retrieves college information from a public API, organized by state.
-   **Firestore Integration**: Uploads, updates, and manages college data in Google Cloud Firestore.
-   **Embedding Generation**: Creates embeddings for college descriptions using OpenAI's language models, enabling semantic search capabilities.
-   **Advanced Search Functionality**: Utilizes LangChain's RetrievalQA and a ChatOpenAI model to perform sophisticated queries on the college data.

## Project Structure

-   `fetch_colleges.py`: Contains the logic to fetch college data from the API and manage the update process in Firestore.
-   `upload_to_firestore.py`: Handles the uploading and updating of college data in Firestore.
-   `generate_embeddings.py`: Generates and updates embeddings for college data stored in Firestore.
-   `search_colleges.py`: Implements the search functionality using LangChain, allowing users to query the college data.

## Setup and Installation

### Prerequisites

-   Python 3.7 or higher
-   A Google Cloud Platform project with Firestore enabled
-   An OpenAI API key

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone [repository-url]
    cd [repository-name]
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root directory of the project and add your OpenAI API key and any other necessary configuration:

    ```
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

### Fetching and Uploading College Data

To fetch college data from the API and upload it to Firestore, you can use the `fetch_colleges.py` script. This script is designed to be triggered as a Cloud Function, but you can also run it locally for testing:

1. **Run the script**:

    ```bash
    python src/fetch_colleges.py
    ```

    This will fetch college data for all states and upload it to Firestore.

### Generating Embeddings

After uploading the data, you can generate embeddings for the college descriptions:

1. **Run the script**:

    ```bash
    python src/generate_embeddings.py
    ```

    This script fetches each college document from Firestore, generates an embedding for its description, and updates the document with this embedding.

### Searching College Data

To search the college data using natural language queries:

1. **Run the script**:

    ```bash
    python src/search_colleges.py
    ```

2. **Enter your query** when prompted. The script will use the RetrievalQA chain to find relevant college data based on your query.

## Deployment

The `fetch_colleges.py` script is designed to be deployed as a Google Cloud Function. You can deploy it using the Google Cloud SDK:

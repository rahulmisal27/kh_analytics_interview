For the provided exercise, I implemented below solution:

1. **Discount Percentage Model**:
    - I have trained the regression model using Xgboost Regressor. The model is trained to predict the discount percentage based on features like product category, original price, rating and number of ratings.
    - The model is saved using pickle for future use in models folder.
    - I have implemeted the API using FastAPI framework. The API has an endpoint /predict_discount which takes user id and and product id as input and returns the predicted discount percentage.
    Here is the curl command to test the API:
    ```
    curl --request POST \
        --url http://localhost:8000/api/get_discount \
        --header 'content-type: application/json' \
        --data '{
        "user_id" : "AFM3PEUDKST5I4ABCDADACT6UJCQ,AHIWDTUXZ2KUNE2BAZOWMZVDSS3A,AF6UHDAZK4ZALHNOJKQAZH6HISTA,AFUGI4MVDD6UIXUSOAONN3CJGO5Q,AHIVOVS2S5CODJ473W3ABVHSPSMA,AEC3N2HJPRWIDJRQNOE4CO6JCVUA,AHXODZHY6I6ZB3I5IUMGMLXCX2KQ,AEKIKDXW3S2LXR6V6BAV5LKQSYQA",
        "product_ids" : ["B0162LYSFS"]
        
        }'
    ```

    Here is response from the API:
        
    ```
        {
        "discount_percentage": [
            54.97692108154297
        ]
        }
        
    ```

    - The API returns the predicted discount percentage for the given user and product ids.

2. **Product Answer Generation RAG Pipeline**:
    - I have implemented a Retrieval Augmented Generation (RAG) pipeline using product details.
    - The model uses a pre-trained language model (SmolLM2-135M-Instruct) and a milvus as vector database for retrieval.
    - I  have implemented the hybrid RAG with dense vector generated using Snowflake/snowflake-arctic-embed-s model and sparse vector using BM25 algorithm.
    - The RAG model takes a user query as input, retrieves relevant product information from the file vector database (stored in models folder), and generates an answer using the language model.
    - I have implemeted the API using FastAPI framework. The API has an endpoint /generate_answer which takes user query as input and returns the generated answer.
    Here is the curl command to test the API:
    ```
    curl --request POST \
    --url http://localhost:8000/api/answer_question \
    --header 'content-type: application/json' \
    --data '{
    "question" : "Tell me about Wayona Nylon Braided USB"
    }'

    ```

    Here is response from the API:
        
    ```
        {
        "answer": "Based on the context, Wayona Nylon Braided USB is an innovative and durable cable designed for use with Apple devices. It features a high-quality nylon braided design with premium aluminum housing and a toughened nylon fiber wound tightly around the cord, providing superior durability and protecting the device from excessive current. The cable is designed to be compatible with any charging adaptor, multi-port charging station, and power bank, ensuring a seamless and fast charging experience. The product is also designed to be durable and resistant to damage, making it suitable for use with any Apple device."
        }
        
    ```

    - The API returns the generated answer for the given user query.

## Marketing Data Intelligence

### Objective

Design and implement an intelligent machine learning system that enhances data-driven decision-making for a digital platform.

The system should:

Predict key business outcomes (such as pricing, demand, or performance metrics) using historical and descriptive data.
Provide an LLM-powered assistant capable of answering user or customer queries by leveraging relevant textual content
Dataset

Use an e-commerce dataset similar to the Amazon Sales Dataset on Kaggle. 
example https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset 
You can use any other dataset if needed
 

### Key Requirements

- Develop an AI Assistant powered by open-source LLMs capable of generating accurate, context-aware responses using marketing and customer data.
- Implement LLM fine-tuning or adaptation on domain-specific datasets to enhance accuracy, tone alignment, and domain understanding.
- Integrate predictive modeling to forecast key marketing outcomes (e.g., optimal discounts, conversions, or campaign performance).
- Ensure scalability, security, and monitoring through containerized APIs and performance tracking for production readiness.

#### Nice to have

- Add a Retrieval-Augmented Generation (RAG) layer to enrich the assistant with grounded responses from structured and unstructured marketing data.
- Incorporate automated retraining and drift detection for continuous model improvement.
- Include explainability and observability features for transparency and reliability.
- Perform unit, integration, and load testing, and validate safety rules
- Deployment & Testing


### Containerize the solution with Docker and expose APIs using FastAPI or Flask:
Example
/predict_discount → Predicts product discount percentage

/answer_question → Answers product-related user queries via RAG + LLM

### Evaluate performance using:

Regression metrics: RMSE, MAE, R²,..

RAG grounding accuracy & factuality rate
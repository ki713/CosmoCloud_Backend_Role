# Backend Task of CosmoCloud By Kiranpreet Sethi
# Problem Statement

You are tasked with creating a sample backend application using FastAPI, Python, and MongoDB. This challenge assumes a basic understanding of Python and some knowledge of Flask/Django/FastAPI, as well as MongoDB.

## Brief

### Building an Ecommerce Application

You are developing an ecommerce application similar to Flipkart or Amazon. The objective is to implement the following APIs:

#### 1. List Products API:

- **Endpoint:** `/api/products`
- **Method:** `GET`
- **Description:** Retrieve a list of all available products in the system.
- **Query Parameters:**
  - `limit`: Pagination limit
  - `offset`: Pagination offset
  - `min_price`: Minimum product price filter
  - `max_price`: Maximum product price filter
- **Response Format:**
  
  {
    "data": [
      {
        "id": "product_id",
        "name": "product_name",
        "price": "product_price",
        "quantity": "product_quantity"
      },
      
    ],
    "page": {
      "limit": "current_limit",
      "nextOffset": "next_offset_if_more_records_present",
      "prevOffset": "prev_offset_if_previous_records_present",
      "total": "total_number_of_records"
    }
  }

#### 2. Create Order API:

- **Endpoint:** `/api/orders`
- **Method:** `POST`
- **Description:** Create a new order.
- **Request Payload:**
  
  {
    "items": [
      {
        "productId": "product_id",
        "boughtQuantity": "quantity",
        "totalAmount": "total_amount"
      },
      
    ],
    "userAddress": {
      "city": "user_city",
      "country": "user_country",
      "zipCode": "user_zip_code"
    }
  }
#### 3.Response Format:


{
  "orderId": "order_id",
  "createdOn": "auto_generated_timestamp"
}

## Tech Stack

- **Python Version:** 3.10 or above
- **Framework:** FastAPI
- **Database:** MongoDB
- **MongoDB Drivers:** Pymongo or Motor

## Steps

1. **Clone this repository:**
   git clone https://github.com/your-username/ecommerce-backend.git
   cd ecommerce-backend

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Set up MongoDB:**
   Configure MongoDB connection details in the FastAPI application.

4. **Run the FastAPI application:**
   uvicorn main:app --reload

5. **Access the API documentation:**
    Visit http://127.0.0.1:8000/docs to test and interact with the APIs.

## Demo Video
https://youtu.be/Rn75Br6Ql8k?si=pD2mw-kW7fcv1O8w







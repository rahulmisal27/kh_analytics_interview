from core.requests import DiscountRequest, DiscountResponse
from fastapi import APIRouter
import pickle
import pandas as pd

discount_router = APIRouter()

discount_model = pickle.load(open("models/discount_model_xgb.pkl", "rb"))
encoder = pickle.load(open("models/multi_label_encoder.pkl", "rb"))
df = pd.read_csv("data/processed/amazon.csv")


@discount_router.post("/get_discount", response_model=DiscountResponse)
def get_discount(request: DiscountRequest):

    temp_df = df[
        (df["user_id"] == request.user_id)
        & (df["product_id"].isin(request.product_ids))
    ].copy()
    temp_df = pd.concat(
        [
            temp_df.reset_index(drop=True),
            pd.DataFrame(
                encoder.transform(temp_df["category"].str.split("|")),
                columns=encoder.classes_,
            ),
        ],
        axis=1,
    )
    features = temp_df[discount_model.feature_names_in_]
    discounts = discount_model.predict(features)

    return DiscountResponse(discount_percentage=discounts.tolist())

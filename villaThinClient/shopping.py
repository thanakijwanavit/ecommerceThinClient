# AUTOGENERATED! DO NOT EDIT! File to edit: shopping.ipynb (unless otherwise specified).

__all__ = ['Browser']

# Cell
from villaProductSdk.products import ProductSdk
from villaBackendSdk.basket import BasketSdk
from awsSchema.apigateway import Response, Event
from nicHelper.wrappers import add_class_method, add_method, add_static_method
from typing import List
from s3bz.s3bz import S3
import json
from requests import post, get
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

# Cell
class Browser:
  def __init__(
    self,
    searchEndpoint = 'https://8av9li9v82.execute-api.ap-southeast-1.amazonaws.com/Prod/orismaSearch/',
    branch = 'dev-manual'
    ):
    self.searchEndpoint = searchEndpoint
    self.productSdk = ProductSdk(branch = branch)

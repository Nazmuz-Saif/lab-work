from django.test import TestCase

from .models import Product

URL = "/api/v1/products/"


class ProductTests(TestCase):
    def test_successful_insertion(self):
        data = {"product_code": "00123", "product_name": "Blue Pen", "price": "12.50"}
        response = self.client.post(URL, data)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(Product.objects.filter(product_code="00123").exists())

        codes = [p["product_code"] for p in self.client.get(URL).json()]
        self.assertIn("00123", codes)

    def test_invalid_price_is_rejected(self):
        for bad_price in ["0", "-5", "abc"]:
            data = {"product_code": "00123", "product_name": "Blue Pen", "price": bad_price}
            response = self.client.post(URL, data)

            self.assertEqual(response.status_code, 400)
            self.assertIn("price", response.json())

        self.assertEqual(Product.objects.count(), 0)

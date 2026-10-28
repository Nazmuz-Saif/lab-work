from django.test import TestCase


class HealthTests(TestCase):
    def test_health_endpoint_is_ok(self):
        response = self.client.get("/api/v1/health/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Farm


class FarmTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_farm = Farm.objects.create(
            name="rake",
            reviewer=testuser1,
            description="Better for collecting leaves than a shovel.",
            average_rating="4.00"
        )
        test_farm.save()


    def test_farms_model(self):
        farm = Farm.objects.get(id=1)
        actual_reviewer = str(farm.reviewer)
        actual_name = str(farm.name)
        actual_description = str(farm.description)
        actual_average_rating = str(farm.average_rating)
        self.assertEqual(actual_reviewer, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_description, "Better for collecting leaves than a shovel.")
        self.assertEqual(
            actual_average_rating, "4.00"
        )

    def test_get_farm_list(self):
        url = reverse("farm_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        farms = response.data
        self.assertEqual(len(farms), 1)
        self.assertEqual(farms[0]["name"], "rake")

    def test_get_farm_by_id(self):
        url = reverse("farm_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        farm = response.data
        self.assertEqual(farm["name"], "rake")

    def test_create_farm(self):
        url = reverse("farm_list")
        data = {"reviewer": 1, "name": "spoon", "description": "good for cereal and soup", "average_rating": "4",}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        farms = Farm.objects.all()
        self.assertEqual(len(farms), 2)
        self.assertEqual(Farm.objects.get(id=2).name, "spoon")

    def test_update_farm(self):
        url = reverse("farm_detail", args=(1,))
        data = {
            "reviewer": 1,
            "name": "rake",
            "description": "pole with a crossbar toothed like a comb.",
            "average_rating": "4.00",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        farm = Farm.objects.get(id=1)
        self.assertEqual(farm.name, data["name"])
        self.assertEqual(farm.reviewer.id, data["reviewer"])
        self.assertEqual(farm.description, data["description"])
        self.assertEqual(farm.average_rating, data["average_rating"])

    def test_delete_farm(self):
        url = reverse("farm_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        farms = Farm.objects.all()
        self.assertEqual(len(farms), 0)

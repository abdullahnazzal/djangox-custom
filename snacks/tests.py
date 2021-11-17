from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snacks

# Create your tests here.
class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username= "tester", email = "tester@email.com", password = "pass"
        )
        self.snack = Snacks.objects.create(
            title = "snack3", purchaser = self.user, description = "snack3"
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "snack3")
    
    def test_thing_content(self):
        self.assertEqual(f"{self.snack.title}", "snack3")
        self.assertEqual(f"{self.snack.purchaser}", "tester@email.com")
        self.assertEqual(self.snack.description, "snack3")
    
    def test_snack_list_view(self):
        url = reverse("snack-list")
        response = self.client.get(url)
        self.assertEquals(response.status_code,200)
        # self.assertContains(response,"snack3")
        # self.assertTemplateUsed(response,"snacks/snack_list.html")
    
    # def test_snack_detail_view(self):
    #     url = reverse("snack-detail",args="1")
    #     response = self.client.get(url)
    #     no_response = self.client.get("/200000/")
    #     self.assertEquals(response.status_code,200)
    #     self.assertEquals(no_response.status_code,404)
    #     self.assertContains(response,"Purchaser: tester")
    #     self.assertTemplateUsed(response,"snack_detail.html")
    
    # def test_snack_create_view(self):
    #     response = self.client.post(
    #         reverse("snack-create"),
    #         {
    #             "title":"snackTest",
    #             "purchaser":self.user.id,
    #             "description":"snackTest",
    #         },
    #         follow=True
    #     )
    #     self.assertRedirects(response,reverse("snack-detail",args="2"))
    #     self.assertContains(response,"Title: snackTest")

    # def test_snack_update_view(self):
    #     response = self.client.post(
    #         reverse("snack-update",args="1"),
    #         {
    #             "title":"SnackUpdateTest",
    #             "purchaser":self.user.id,
    #             "description":"SnackUpdateTest",
    #         }
    #     )
    #     self.assertRedirects(response,reverse("snack-detail",args="1"))
    #     # self.assertContains(response,"Title: SnackUpdateTest") # NOT work

    # def snack_delete_view(self):
    #     response = self.client.get(
    #         reverse("snack_delete",args="1")
    #     )
    #     self.assertEqual(response.status_code,200)



    

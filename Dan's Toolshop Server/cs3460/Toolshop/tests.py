from django.test import TestCase
from .models import Tool, CustomerInfo, Message
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.


class ToolShopTest(TestCase):
    def create_tool(self, name="Hammer", category="Basic Tool", cost=5):
        return Tool(name=name, category=category, cost=cost, times_checked_out=0)

    def test_tool_creation(self):
        t = self.create_tool()
        self.assertTrue(isinstance(t, Tool))
        self.assertTrue(t.__str__(), t.name)

    def test_tool_checkout(self):
        t = self.create_tool()
        t.is_checked_out = True
        t.times_checked_out += 1
        t.who_checked_out = "Steve"
        self.assertTrue(t.is_checked_out)
        self.assertEqual(t.times_checked_out, 1)
        self.assertEqual(t.who_checked_out, "Steve")

    def create_customer_info(self):
        return CustomerInfo(user=User(username="default", password="password"))

    def test_customer_creation(self):
        c = self.create_customer_info()
        self.assertTrue(isinstance(c, CustomerInfo))
        self.assertTrue(isinstance(c.user, User))

    def test_customer_edit(self):
        c = self.create_customer_info()
        c.user.password = "1234"
        c.phone_num = "2089321230"
        self.assertEqual(c.user.password, "1234")
        self.assertEqual(c.phone_num, "2089321230")

    def create_message(self):
        return Message(first_name="test", last_name="another", email="test@gmail.com", subject="test",
                       message="This is a test")

    def test_message_creation(self):
        m = self.create_message()
        self.assertTrue(isinstance(m, Message))
        self.assertTrue(m.__str__(), m.subject)

    def test_reservation_view(self):
        t = self.create_tool()
        t.save()
        url = reverse('Toolshop:reserve')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        self.client.login(username="test", password="testpassword")
        response = self.client.get(url)
        self.assertContains(response, t)
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        url = reverse('Toolshop:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Toolshop/index.html")

    def test_contact_view(self):
        url = reverse('Toolshop:contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Toolshop/contact.html")

    def test_tools_view(self):
        url = reverse('Toolshop:tools')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_projects_view(self):
        url = reverse('Toolshop:projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_database_view(self):
        url = reverse('Toolshop:database_upload')
        self.user = User.objects.create_superuser('admin', 'myemail@test.com', "password")
        self.client.login(username="admin", password="password")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_account_view(self):
        t = Tool(name="name", category="category", cost=5, times_checked_out=0, who_checked_out="test")
        t.save()
        url = reverse('Toolshop:account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        self.client.login(username="test", password="testpassword")
        response = self.client.get(url)
        self.assertContains(response, t)
        self.assertContains(response, self.user)
        self.assertEqual(response.status_code, 200)



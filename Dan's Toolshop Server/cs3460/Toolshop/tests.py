from django.test import TestCase
from .models import Tool, CustomerInfo, Message
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta


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
        t = Tool(name="name", category="category", cost=5, times_checked_out=0, who_checked_out="test",
                 date_checked_out=timezone.now())
        t.save()
        url = reverse('Toolshop:account')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        c = CustomerInfo(user=self.user, current_outstanding_balance=0, this_period_paid=True)
        c.save()
        self.client.login(username="test", password="testpassword")
        response = self.client.get(url)
        self.assertContains(response, t)
        self.assertContains(response, self.user)
        self.assertEqual(response.status_code, 200)

    def test_make_reservation(self):
        t = self.create_tool()
        t.save()
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        c = CustomerInfo(user=self.user, current_outstanding_balance=0, this_period_paid=True)
        c.save()
        self.client.login(username="test", password="testpassword")
        url = reverse('Toolshop:makeReservation', kwargs={'id': t.id})
        response = self.client.get(url, args=[t.id])
        t = Tool.objects.filter(id=t.id)
        self.assertEqual(t[0].who_checked_out, self.user.username)
        self.assertTrue(t[0].is_checked_out)
        self.assertEqual(response.status_code, 200)

    def test_submit_message_no_data(self):
        url = reverse('Toolshop:submitMessage')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('Toolshop:error'))

    def test_submit_message_with_data(self):
        url = reverse('Toolshop:submitMessage')
        response = self.client.post(url, {'firstname': 'test', 'lastname': 'testLast',
                                                 'emailAddress': 'test@test.com',
                                                 'subject': 'Test', 'textBody': 'This is a test'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('Toolshop:redirect'))

    def test_update_user_no_data(self):
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        c = CustomerInfo(user=self.user, current_outstanding_balance=0, this_period_paid=True)
        c.save()
        self.client.login(username="test", password="testpassword")
        url = reverse('Toolshop:update')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('Toolshop:updateError'))

    def test_update_user_with_data(self):
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        c = CustomerInfo(user=self.user, current_outstanding_balance=0, this_period_paid=True)
        c.save()
        self.client.login(username="test", password="testpassword")
        url = reverse('Toolshop:update')
        response = self.client.post(url, {'firstName': 'test', 'lastName': 'testLast',
                                                 'address': '1234 N 344 E',
                                                 'email': 'test@test.com', 'phone': "1234567890",
                                                 'psw': 'password', 'psw-repeat': 'password'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('Toolshop:redirect'))

    def test_update_user_wrong_data(self):
        self.user = User.objects.create_user("test", "test@test.com", "testpassword")
        c = CustomerInfo(user=self.user, current_outstanding_balance=0, this_period_paid=True)
        c.save()
        self.client.login(username="test", password="testpassword")
        url = reverse('Toolshop:update')
        response = self.client.post(url, {'firstName': 'test', 'lastName': 'testLast',
                                                 'address': '1234 N 344 E',
                                                 'email': 'test@test.com', 'phone': "1234567890",
                                                 'psw': 'password', 'psw-repeat': 'word'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('Toolshop:updateError'))

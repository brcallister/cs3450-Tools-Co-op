from django.test import TestCase
from .models import Tool, CustomerInfo
from django.contrib.auth.models import User
# Create your tests here.


class ToolTest(TestCase):
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


class CustomerInfoTest(TestCase):
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



from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email="test@example.com", password="testPass"):
    """Create Sample for testing"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test creating a new user with email is successful"""
        email = "test@gmail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email for a new user is normalized"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that user had an email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_super_user_created(self):
        """Test creating superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "test123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(user=sample_user(), name="Vegan")

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(), name="Cucumber")
        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Test the recipee string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title="State and mushroom sauce",
            time_miniutes=5,
            price=5.00
        )
        self.assertEqual(str(recipe), recipe.title)

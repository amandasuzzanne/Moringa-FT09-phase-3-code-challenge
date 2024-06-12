import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    # Tests for Author Class
    def test_author_creation(self):
        author = Author(1, "Amanda")
        self.assertEqual(author.name, "Amanda")

    def test_init(self):
        author = Author(1, "Amanda")
        self.assertEqual(author.id, 1)
        self.assertEqual(author.name, "Amanda")

    def test_save(self):
        author = Author(None, "Amanda")
        author.save()
        self.assertIsNotNone(author.id)
        self.assertIn(author.id, Author.all)

    def test_get_author_id(self):
        author = Author(1, "Amanda")
        self.assertEqual(author.get_author_id(), 1)

    def test_name_immutable(self):
        author = Author(1, "Amanda")
        with self.assertRaises(AttributeError):
            author.name = "Amanda"

    def test_author_repr(self):
        author = Author(1, "Amanda")
        self.assertEqual(repr(author), "<Author Amanda>")

    def test_author_attributes(self):
        author = Author(2, "Amanda")
        self.assertEqual(author.id, 2)
        self.assertEqual(author.name, "Amanda")

    def test_id_setter(self):
        obj = Author(123, "Amanda")
        obj.id = 123
        self.assertEqual(obj.id, 123)

    def test_name_setter(self):
        obj = Author(123, "Amanda")
        self.assertEqual(obj.name, "Amanda")

    def test_saves_author(self):
        author = Author(None, "Amanda")
        author.save()
        self.assertIsNotNone(author.id)
        self.assertIn(author.id, Author.all)

# Tests for the Article Class
        def test_article_creation(self):
            article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
            self.assertEqual(article.id, 1)
            self.assertEqual(article.title, "Fashion Trends")
            self.assertEqual(article.content, "Content about fashion trends")
            self.assertEqual(article.author_id, 1)
            self.assertEqual(article.magazine_id, 1)

    def test_title_setter(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        with self.assertRaises(AttributeError):
            article.title = "New Title"
    
    def test_title_setter_valid(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        self.assertEqual(article.title, "Fashion Trends")
        
    def test_content_setter(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        article.content = "Updated content"
        self.assertEqual(article.content, "Updated content")

    def test_content_setter_invalid(self):
        with self.assertRaises(ValueError):
            Article(1, "Fashion Trends", "", 1, 1)
    
    def test_author_id_setter_valid(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        self.assertEqual(article.author_id, 1)

    def test_author_id_setter_invalid(self):
        with self.assertRaises(ValueError):
            Article(1, "Fashion Trends", "Content about fashion trends", 99, 1)

    def test_magazine_id_setter_valid(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        self.assertEqual(article.magazine_id, 1)

    def test_magazine_id_setter_invalid(self):
        with self.assertRaises(ValueError):
            Article(1, "Fashion Trends", "Content about fashion trends", 1, 99)
    
    def test_article_repr(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        self.assertEqual(repr(article), "<Article Fashion Trends>")
    
    def test_article_author(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        self.assertEqual(article.author().name, "Amanda")
    
    def test_article_magazine(self):
        article = Article(1, "Fashion Trends", "Content about fashion trends", 1, 1)
        self.assertEqual(article.magazine().name, "Vogue")
# Tests for Magazine class
    def test_magazine_creation(self):
        magazine = Magazine(1, "Vogue", "Fashion")
        self.assertEqual(magazine.name, "Vogue")

    def test_saves_magazine(self):
        magazine = Magazine(None, "Vogue", "Fashion")
        magazine.save()
        self.assertIsNotNone(magazine.id)
        self.assertIn(magazine.id, Magazine.all)

    def test_magazine_repr(self):
        magazine = Magazine(1, "Vogue", "Fashion")
        self.assertEqual(repr(magazine), "<Magazine Vogue>")

    def test_get_magazine_id(self):
        magazine = Magazine(1, "Vogue", "Fashion")
        self.assertEqual(magazine.get_magazine_id(), 1)

    
    def test_id_property(self):
        magazine = Magazine(1, "Vogue", "Fashion")
        self.assertEqual(magazine.id, 1)

    def test_name_property(self):
        magazine = Magazine(1, "Vogue", "FAshion")
        self.assertEqual(magazine.name, "Vogue")

if __name__ == "__main__":
    unittest.main()
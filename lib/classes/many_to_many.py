
class Author:
    def __init__(self, name):
        if isinstance(name, str) and len(name.strip()) > 0:
            self._name = name
        else:
            self._name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # Ignore attempts to change (immutability for core deliverables)
        pass

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if mags:
            return list({mag.category for mag in mags})
        return None


class Magazine:
    all = []

    def __init__(self, name, category):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            self._name = None

        if isinstance(category, str) and len(category.strip()) > 0:
            self._category = category
        else:
            self._category = None

        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category.strip()) > 0:
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        result = [author for author in set(authors) if authors.count(author) > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if isinstance(author, Author):
            self._author = author
        else:
            self._author = None

        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            self._magazine = None

        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            self._title = None

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        # Ignore attempts to change (immutability for core deliverables)
        pass

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine

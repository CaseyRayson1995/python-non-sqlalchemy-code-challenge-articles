class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title 

    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise AttributeError("title cannot be changed")
        elif not isinstance(value, str):
            raise TypeError("title must be of type string")
        elif len(value) < 5 or len(value) > 50:
            raise ValueError("title must be between 5 and 50 characters")
        self._title = value


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            raise AttributeError("name cannot be changed")
        elif not isinstance(value, str):
            raise TypeError("name must be of type string")
        elif len(value) <= 0:
            raise ValueError("name must be greater than zero")
        self._name = value

    def articles(self):
        return self._articles  

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article

    def magazines(self):
        return list({article.magazine for article in self._articles})

    def topic_areas(self):
        if not self._articles:
            return None  
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be of type string")
        elif not (2 <= len(value) <= 16):
            raise ValueError("name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("category must be of type string")
        elif len(value) == 0:
            raise ValueError("category must have length greater than 0")
        self._category = value

    def articles(self):
        return self._articles

    def add_article(self, article):
        if isinstance(article, Article) and article not in self._articles:
            self._articles.append(article)

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None


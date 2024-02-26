class NewsSystem:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Guest(User):
    def __init__(self, name):
        super().__init__(name)
    
    def view_news(self):
        print(f"{self.name} is viewing news.")
    
    def search_news(self):
        print("Searching for news.")

    def share_news(self):
        print("Sharing news.")
    
    def manage_profile(self):
        print(f"{self.name} is managing their profile.")
        self.personalize_news_preferences()

    def personalize_news_preferences(self):
        print(f"{self.name} is personalizing their news preferences.")


class PaidSubscriber(Guest):
    def __init__(self, name):
        super().__init__(name)

    def access_weekly_content(self):
        print(f"{self.name} is accessing weekly content.")

    def access_exclusive_content(self):
        print(f"{self.name} is accessing exclusive content.")




class Editor(User):
    def __init__(self, name):
        super().__init__(name)

    def review_and_fix(self):
        print(f"{self.name} is reviewing and fixing news articles.")
        self.oversee_future_articles()

    def oversee_future_articles(self):
        print(f"{self.name} is overseeing future articles.")


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    def update_news(self):
        print(f"{self.name} is updating news.")

    def delete_news(self):
        print(f"{self.name} is deleting news.")

    def hide_news(self):
        print(f"{self.name} is hiding news.")
    
    def publish_news(self):
        print(f"{self.name} is publishing news.")


# Test the News System
news_system = NewsSystem()

guest_user = Guest("GuestUser")
paid_subscriber = PaidSubscriber("Paid Subscriber")
editor = Editor("Editor")
admin = Admin("Admin")

news_system.add_user(guest_user)
news_system.add_user(paid_subscriber)
news_system.add_user(editor)
news_system.add_user(admin)

guest_user.view_news()
guest_user.search_news()
paid_subscriber.share_news()
paid_subscriber.manage_profile()
paid_subscriber.personalize_news_preferences()
paid_subscriber.access_weekly_content()
paid_subscriber.access_exclusive_content()
editor.review_and_fix()
editor.oversee_future_articles()
admin.publish_news()
admin.update_news()
admin.delete_news()
admin.hide_news()

from unittest import TestCase, main
from project.social_media import SocialMedia



class TestSocialMedia(TestCase):
    def setUp(self):
        self.social_media = SocialMedia("test_user", "Instagram", 1000, "photo")

    def test_correct_init(self):
        self.assertEqual(self.social_media.platform, "Instagram")
        self.assertEqual(self.social_media._username, "test_user")
        self.assertEqual(self.social_media._content_type, "photo")
        self.assertEqual(self.social_media.followers, 1000)
        self.assertEqual(self.social_media._posts, [])

    def test_platform_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "fake"
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    def test_followers_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1
        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_post(self):
        self.assertEqual(self.social_media.create_post("Test post"), "New photo post created by test_user on Instagram.")
        self.assertIn({'content': 'Test post', 'likes': 0, 'comments': []}, self.social_media._posts)

    def test_like_post(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.like_post(0), "Post liked by test_user.")
        post = self.social_media._posts[0]
        self.assertEqual(post['likes'], 1)

    def test_like_post_max_likes(self):
        self.social_media.create_post("Test post")
        post = self.social_media._posts[0]
        self.assertEqual(post['likes'], 0)
        post["likes"] = 10
        result = self.social_media.like_post(0)
        self.assertEqual(result, "Post has reached the maximum number of likes.")
        self.assertEqual(post['likes'], 10)

    def test_like_post_invalid_index(self):
        self.assertEqual(self.social_media.like_post(1), "Invalid post index.")


    def test_comment_on_post(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Great post!"), "Comment added by test_user on the post.")

    def test_comment_on_post_short_comment(self):
        self.social_media.create_post("Test post")
        self.assertEqual(self.social_media.comment_on_post(0, "Nice"), "Comment should be more than 10 characters.")


if __name__ == "__main__":
    main()
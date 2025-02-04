# ローカルの画像をアップロードするサンプルコード
# 例): 画像を添付して投稿する場合


email = "your_email"
password = "your_password"


import yaylib


api = yaylib.Client()
api.login(email, password)

# 画像のパスを指定
image_paths = [
    "./test1.jpg",
    "./test2.jpg",
    "./test3.jpg",
]

# 画像の使い道を指定
image_type = yaylib.IMAGE_TYPE_POST

# サーバー上にアップロード
attachments = api.upload_image(image_paths, image_type)

# サーバー上のファイル名を指定する
# attachmentsが一つ飛ばしなのはオリジナル品質の画像のみを指定するため
api.create_post(
    "Hello with yaylib!",
    attachment_filename=attachments[0].filename,
    attachment_2_filename=attachments[2].filename,
    attachment_3_filename=attachments[4].filename,
)

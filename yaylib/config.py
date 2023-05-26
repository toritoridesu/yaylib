class Configs:

    YAYLIB_VERSION = "0.0.1"
    YAY_API_VERSION = "3.16"
    YAY_VERSION_NAME = "3.16.1"
    YAY_API_VERSION_KEY = "e83a1d2588918c2061280427c88e6f56"
    YAY_API_KEY = "ccd59ee269c01511ba763467045c115779fcae3050238a252f1bd1a4b65cfec6"
    YAY_SHARED_KEY = "yayZ1"
    YAY_STORE_KEY = "yayZ1payment"
    ID_CARD_CHECK_SECRET_KEY = "4aa6d1c301a97154bc1098c2"
    YAY_REVIEW_HOST_1 = "review.yay.space"
    YAY_REVIEW_HOST_2 = "cas-stg.yay.space"
    YAY_STAGING_HOST_1 = "stg.yay.space"
    YAY_STAGING_HOST_2 = "cas.yay.space"
    YAY_PRODUCTION_HOST = "api.yay.space"
    YAY_API_URL = "https://" + YAY_PRODUCTION_HOST
    ID_CARD_CHECK_HOST_PRODUCTION = "idcardcheck.com"
    ID_CARD_CHECK_HOST_STAGING = "stg.idcardcheck.com"
    REQUEST_HEADERS = {
        "Host": YAY_PRODUCTION_HOST,
        "X-App-Version": YAY_API_VERSION,
        "User-Agent": "android 11 (3.5x 1440x2960 Galaxy S9)",
        "X-Device-Info": f"yay {YAY_VERSION_NAME} android 11 (3.5x 1440x2960 Galaxy S9)",
        "X-Device-Uuid": "",
        "X-Connection-Type": "wifi",
        "Accept-Language": "ja",
        "Content-Type": "application/json;charset=UTF-8"
    }


class Endpoints:

    # v1 endpoints
    USER_V1 = Configs.YAY_API_URL + "/v1/users/"
    PAYMENTS_V1 = Configs.YAY_API_URL + "/v1/payments/"
    THREADS_V1 = Configs.YAY_API_URL + "/v1/threads/"
    PINNED_V1 = Configs.YAY_API_URL + "/v1/pinned/"
    POSTS_V1 = Configs.YAY_API_URL + "/v1/posts/"
    CONVERSATIONS_V1 = Configs.YAY_API_URL + "/v1/conversations/"
    HIDDEN_V1 = Configs.YAY_API_URL + "/v1/hidden/"
    GROUPS_V1 = Configs.YAY_API_URL + "/v1/groups/"
    CHAT_ROOMS_V1 = Configs.YAY_API_URL + "/v1/chat_rooms/"
    CALLS_V1 = Configs.YAY_API_URL + "/v1/calls/"
    SURVEYS_V1 = Configs.YAY_API_URL + "/v1/surveys/"

    # v2 endpoints
    USER_V2 = Configs.YAY_API_URL + "/v2/users/"
    PAYMENTS_V2 = Configs.YAY_API_URL + "/v2/payments/"
    THREADS_V2 = Configs.YAY_API_URL + "/v2/threads/"
    PINNED_V2 = Configs.YAY_API_URL + "/v2/pinned/"
    POSTS_V2 = Configs.YAY_API_URL + "/v2/posts/"
    CONVERSATIONS_V2 = Configs.YAY_API_URL + "/v2/conversations/"
    HIDDEN_V2 = Configs.YAY_API_URL + "/v2/hidden/"
    GROUPS_V2 = Configs.YAY_API_URL + "/v2/groups/"
    CHAT_ROOMS_V2 = Configs.YAY_API_URL + "/v2/chat_rooms/"
    CALLS_V2 = Configs.YAY_API_URL + "/v2/calls/"
    SURVEYS_V2 = Configs.YAY_API_URL + "/v2/surveys/"

    # v3 endpoints
    USER_V3 = Configs.YAY_API_URL + "/v3/users/"
    PAYMENTS_V3 = Configs.YAY_API_URL + "/v3/payments/"
    THREADS_V3 = Configs.YAY_API_URL + "/v3/threads/"
    PINNED_V3 = Configs.YAY_API_URL + "/v3/pinned/"
    POSTS_V3 = Configs.YAY_API_URL + "/v3/posts/"
    CONVERSATIONS_V3 = Configs.YAY_API_URL + "/v3/conversations/"
    HIDDEN_V3 = Configs.YAY_API_URL + "/v3/hidden/"
    GROUPS_V3 = Configs.YAY_API_URL + "/v3/groups/"
    CHAT_ROOMS_V3 = Configs.YAY_API_URL + "/v3/chat_rooms/"
    CALLS_V3 = Configs.YAY_API_URL + "/v3/calls/"
    SURVEYS_V3 = Configs.YAY_API_URL + "/v3/surveys/"

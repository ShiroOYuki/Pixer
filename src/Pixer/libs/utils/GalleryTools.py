from Gallery.models import PixerImages, PixerFavorites
from User.models import PixerUser

def get_image_data(image_id: str, uid=None):
    image_data = PixerImages.get_image_data(image_id)
    if image_data is None: return None
    
    username = PixerUser.get_username(image_data.get("uid"))
    if username is None: username = "unknown"
    
    is_favorite = PixerFavorites.objects.filter(uid=uid, image_id=image_id).exists()
    
    res = image_data.copy()
    res["username"] = username
    res["is_favorite"] = is_favorite
    return res
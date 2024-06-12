from Gallery.models import PixerImages, PixerFavorites
from User.models import PixerUser
from typing import Literal, Optional

def get_image_data(image_id: str, uid: Optional[str]=None, mode: Literal["abs", "rel"]="abs"):
    image_data = PixerImages.get_image_data(image_id)
    if image_data is None: return None
    
    username = PixerUser.get_username(image_data.get("uid"))
    if username is None: username = "unknown"
    
    is_favorite = PixerFavorites.objects.filter(uid=uid, image_id=image_id).exists()
    
    res = image_data.copy()
    res["username"] = username
    res["is_favorite"] = is_favorite
    
    if mode == "rel": res["filepath"] = "/static" + res["filepath"].split("/static")[-1]
    return res
import comfy.utils
class ImageDouble:


    @classmethod
    def INPUT_TYPES(s):

        return{"required":
                    {"images": ("IMAGE", ),"upscale_method": (s.upscale_methods,),}
                }

    upscale_methods = ["nearest-exact", "bilinear", "area", "bicubic", "lanczos"]
    RETURN_TYPES = ('IMAGE',)
    FUNCTION = "image_double"
    CATEGORY = "zt/image"

    def image_double(self, images,upscale_method):
        samples = images.movedim(-1, 1)
        width = max(1, round(samples.shape[3] * 1024 / samples.shape[2]))
        height = max(1, round(images.shape[2] * 1024 / samples.shape[3]))
        s = comfy.utils.common_upscale(samples, width, height, upscale_method, "disabled")
        s = s.movedim(1, -1)
        return (s,)


    # @classmethod
    # def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""



# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
# NODE_CLASS_MAPPINGS = {
#     "Example": ImageDouble
# }

# A dictionary that contains the friendly/humanly readable titles for the nodes
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "Example": "图片放大一倍"
# }

from .models import Comment,Image
from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

admin.site.register(Image)


# Register your models here.
class FileAdmin(ModelAdmin):#wagtailを経由せずに、modelを定義し、管理ページに反映させる
    model = Image#modelのクラス
    menu_label = "アップロードImage"#モデルのlabel
    menu_icon = "snippet"#icon
    menu_order=200#1~999の整数、メニューの場所を返す。100より小さい場合トップに表示
    add_to_settings_menu=False#menuのサブに入れる場合は、True
    exclude_from_explorer=False#検索に入れる場合、True
    list_display=("answer","univ","subject_year")#表示するフィールド
    search_fields=("answer","univ","subject_year")#検索結果を返すフィールド

modeladmin_register(FileAdmin)#登録してるclassを返す

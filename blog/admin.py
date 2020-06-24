from django.contrib import admin
from .models import Banner, Category, Recommend, Tag, Article, Link


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'recommend', 'user', 'views', 'created_time')
    # 分页，50一页
    list_per_page = 50
    # 排序， 按照 created_time 降序
    ordering = ('-created_time',)
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')

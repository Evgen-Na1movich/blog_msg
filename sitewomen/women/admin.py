from django.contrib import admin, messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщин'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'content', 'cat', 'tags') # поля которые будут отображаться поля при редактировании записи
    # exclude = ('tags', 'is_published') # поля которые не будут отображаться при редактировании записи
    # readonly_fields = ('slug',) # только чтение
    prepopulated_fields = {"slug": ("title",)} # автозаполнени на основе других полей

    list_display = (
        'title', 'time_create', 'is_published', 'cat', 'brief_info')  # какие поля будут показываться в админке
    list_display_links = ('title',)  # какие поля будут кликабельными
    ordering = ('-time_create', 'title')  # порядок сортировки записей по убыванию поля
    list_editable = ('is_published',) # редактируемые поля
    list_per_page = 5  # максимальное число отображаемых записей на странице
    actions = ['set_published', 'set_draft']
    search_fields = ('title', 'cat__name')
    list_filter = (MarriedFilter, 'cat__name', 'is_published')

    @admin.display(description="Краткое описание", ordering='content')
    def brief_info(self, women: Women):
        return f"Описание {len(women.content)} символов."

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request,
                      queryset):  # request – объект запроса; queryset – объект QuerySet с выбранными записями
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записи(ей).")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request,
                  queryset):  # request – объект запроса; queryset – объект QuerySet с выбранными записями
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"Изменено {count} записи(ей).", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
